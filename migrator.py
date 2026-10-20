#!/usr/bin/env python3
import csv
import io

class ShopifyCatalogMigrator:
    @staticmethod
    def map_shopify_row_to_woo(row):
        return {
            'ID': '',
            'Type': 'variable' if row.get('Option1 Value') else 'simple',
            'SKU': row.get('Variant SKU', ''),
            'Name': row.get('Title', ''),
            'Regular price': row.get('Variant Price', ''),
            'Images': row.get('Image Src', ''),
            'Description': row.get('Body (HTML)', '')
        }

if __name__ == '__main__':
    print('Shopify to WooCommerce Migrator ready.')
