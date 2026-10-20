#!/usr/bin/env python3
import csv
import io
import sys
import os
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

def run_migration(input_file: str, output_file: str):
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    with open(input_file, mode='r', encoding='utf-8-sig', errors='replace') as f:
        reader = csv.DictReader(f)
        shopify_rows = list(reader)

    if not shopify_rows:
        print(f"Notice: Input file '{input_file}' contains no product rows.")
        sys.exit(0)

    woo_rows = ShopifyCatalogMigrator.convert_shopify_csv_to_woo(shopify_rows)

    with open(output_file, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=ShopifyCatalogMigrator.WOO_HEADERS)
        writer.writeheader()
        writer.writerows(woo_rows)

    print(f"Success: Converted {len(shopify_rows)} Shopify rows into {len(woo_rows)} WooCommerce HPOS products.")
    print(f"Destination: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Shopify to WooCommerce Catalog Migrator CLI")
    parser.add_argument("--input", "-i", required=True, help="Path to exported Shopify products.csv")
    parser.add_argument("--output", "-o", default="woocommerce_import.csv", help="Destination path for WooCommerce import CSV")
    args = parser.parse_args()

    run_migration(args.input, args.output)

if __name__ == '__main__':
    main()
