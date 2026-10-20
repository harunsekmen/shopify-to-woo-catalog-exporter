import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from migrator import ShopifyCatalogMigrator

class TestMigrator(unittest.TestCase):
    def test_row_mapping(self):
        sample_row = {
            'Title': 'Classic Linen Shirt',
            'Variant SKU': 'CLS-001',
            'Variant Price': '89.00',
            'Image Src': 'https://example.com/shirt.jpg',
            'Option1 Value': 'Medium'
        }
        res = ShopifyCatalogMigrator.map_shopify_row_to_woo(sample_row)
        self.assertEqual(res['Name'], 'Classic Linen Shirt')
        self.assertEqual(res['SKU'], 'CLS-001')
        self.assertEqual(res['Regular price'], '89.00')
        self.assertEqual(res['Type'], 'variable')

if __name__ == '__main__':
    unittest.main()
