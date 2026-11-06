import unittest

from warehouse.sku import normalize_sku


class SkuTests(unittest.TestCase):
    def test_canonical_sku(self):
        self.assertEqual(normalize_sku(" a-12 "), "A-12")

    def test_mixed_case_sku(self):
        self.assertEqual(normalize_sku("\t aB-12c \n"), "AB-12C")

    def test_already_canonical_sku(self):
        self.assertEqual(normalize_sku("AB-12C"), "AB-12C")

    def test_blank_sku(self):
        with self.assertRaises(ValueError):
            normalize_sku("  ")
