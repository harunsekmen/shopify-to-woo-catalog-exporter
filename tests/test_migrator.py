import unittest
import sys
import os
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from migrator import ShopifyCatalogMigrator, run_migration

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

    def test_e2e_cli_run(self):
        fixture_path = Path(__file__).parent.parent / "fixtures" / "sample-shopify-products.csv"
        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
            tmp_out = tmp.name
        try:
            run_migration(str(fixture_path), tmp_out)
            self.assertTrue(os.path.exists(tmp_out))
            with open(tmp_out, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                self.assertGreaterEqual(len(lines), 3) # Header + 2 rows
                self.assertIn('variable,LS-S,Linen Shirt', lines[1])
        finally:
            if os.path.exists(tmp_out):
                os.remove(tmp_out)

if __name__ == '__main__':
    unittest.main()
