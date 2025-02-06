# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_item()
        self.assertEqual(["Sulfuras"], all_items)

    # Logical error test: Aged Brie increases in quality as it gets older
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(1, items[0].sell_in)

    # Logical error test: Backstage passes increase in quality as sell_in approaches
    def test_backstage_passes_increase_in_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(15, items[0].sell_in)

    # Logical error test: Quality of an item is never more than 50
    def test_quality_never_more_than_50(self):
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(51, items[0].quality)
        self.assertEqual(1, items[0].sell_in)

    # Syntax error test: Calling a non-existent method
    def test_non_existent_method(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        with self.assertRaises(AttributeError):
            gilded_rose.non_existent_method()

    # Logical error test: This test should fail
    def test_fail_this_test(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)  # This assertion is incorrect on purpose
        self.assertEqual(1, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
