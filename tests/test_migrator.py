import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from migrator import ShopifyCatalogMigrator

class TestMigratorPipeline(unittest.TestCase):
    def test_variable_product_mapping(self):
        rows = [
            {'Handle': 'linen-shirt', 'Title': 'Linen Shirt', 'Variant SKU': 'LS-01', 'Variant Price': '45.00', 'Option1 Name': 'Size', 'Option1 Value': 'S', 'Image Src': 'https://example.com/s.jpg', 'Type': 'Apparel', 'Tags': 'eco, linen', 'Body (HTML)': '<p>Pure linen</p>'},
            {'Handle': 'linen-shirt', 'Title': 'Linen Shirt', 'Variant SKU': 'LS-02', 'Variant Price': '45.00', 'Option1 Name': 'Size', 'Option1 Value': 'M', 'Image Src': 'https://example.com/m.jpg', 'Type': 'Apparel', 'Tags': 'eco, linen', 'Body (HTML)': '<p>Pure linen</p>'}
        ]
        woo_rows = ShopifyCatalogMigrator.convert_shopify_csv_to_woo(rows)
        self.assertEqual(len(woo_rows), 2)
        self.assertEqual(woo_rows[0]['Type'], 'variable')
        self.assertEqual(woo_rows[0]['Name'], 'Linen Shirt')
        self.assertEqual(woo_rows[1]['Type'], 'variation')
        self.assertEqual(woo_rows[1]['Parent'], 'LS-01')

if __name__ == '__main__':
    unittest.main()
