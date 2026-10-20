#!/usr/bin/env python3
import csv
import io
import sys
import argparse

class ShopifyCatalogMigrator:
    WOO_HEADERS = [
        'Type', 'SKU', 'Name', 'Published', 'Is featured?',
        'Visibility in catalog', 'Short description', 'Description',
        'In stock?', 'Stock', 'Regular price', 'Categories', 'Tags',
        'Images', 'Parent', 'Attribute 1 name', 'Attribute 1 value(s)'
    ]

    @staticmethod
    def convert_shopify_csv_to_woo(shopify_rows):
        woo_rows = []
        parents = {}

        for row in shopify_rows:
            handle = row.get('Handle', '').strip()
            title = row.get('Title', '').strip()
            sku = row.get('Variant SKU', '').strip()
            price = row.get('Variant Price', '').strip()
            img = row.get('Image Src', '').strip()
            opt1_name = row.get('Option1 Name', '').strip()
            opt1_val = row.get('Option1 Value', '').strip()

            if title and handle not in parents:
                # Parent Variable Product
                parent_sku = f"{handle}-parent" if not sku else sku
                parents[handle] = parent_sku
                woo_rows.append({
                    'Type': 'variable' if opt1_val else 'simple',
                    'SKU': parent_sku,
                    'Name': title,
                    'Published': '1',
                    'Is featured?': '0',
                    'Visibility in catalog': 'visible',
                    'Short description': '',
                    'Description': row.get('Body (HTML)', ''),
                    'In stock?': '1',
                    'Stock': '',
                    'Regular price': price,
                    'Categories': row.get('Type', ''),
                    'Tags': row.get('Tags', ''),
                    'Images': img,
                    'Parent': '',
                    'Attribute 1 name': opt1_name or 'Size',
                    'Attribute 1 value(s)': opt1_val
                })
            elif opt1_val and handle in parents:
                # Child Variation
                woo_rows.append({
                    'Type': 'variation',
                    'SKU': sku or f"{handle}-{opt1_val.lower()}",
                    'Name': f"{row.get('Title', '')} - {opt1_val}",
                    'Published': '1',
                    'Is featured?': '0',
                    'Visibility in catalog': 'visible',
                    'Short description': '',
                    'Description': '',
                    'In stock?': '1',
                    'Stock': row.get('Variant Inventory Qty', '10'),
                    'Regular price': price,
                    'Categories': '',
                    'Tags': '',
                    'Images': img,
                    'Parent': parents[handle],
                    'Attribute 1 name': opt1_name or 'Size',
                    'Attribute 1 value(s)': opt1_val
                })

        return woo_rows

def main():
    parser = argparse.ArgumentParser(description="Shopify to WooCommerce Catalog Migrator")
    parser.add_argument("--input", required=True, help="Input Shopify products.csv")
    parser.add_argument("--output", default="woocommerce_import.csv", help="Output WooCommerce CSV")
    args = parser.parse_args()
    print(f"Migrating {args.input} to {args.output}...")

if __name__ == '__main__':
    main()
