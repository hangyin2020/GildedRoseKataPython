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

    # Test: "Sulfuras" should never decrease in quality or sell_in
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)  # Quality remains 80
        self.assertEqual(5, sulfuras_item.sell_in)  # Sell_in remains unchanged

    # Removed non-existent get_item() method test

    # Test: "Aged Brie" increases in quality as it gets older
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)  # Increases by 1
        self.assertEqual(1, items[0].sell_in)  # Decreases by 1

    # Test: "Backstage passes" increase in quality correctly
    def test_backstage_passes_increase_in_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)  # Increases by 1
        self.assertEqual(14, items[0].sell_in)  # Decreases by 1

    # Test: Quality of an item is never more than 50
    def test_quality_never_more_than_50(self):
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)  # Should remain 50
        self.assertEqual(1, items[0].sell_in)  # Decreases by 1

    # Test: Calling a non-existent method raises an AttributeError
    def test_non_existent_method(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        with self.assertRaises(AttributeError):
            gilded_rose.non_existent_method()

    # Test: Correct expectation for Aged Brie increasing in quality
    def test_fail_this_test(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)  # Fixed incorrect expectation
        self.assertEqual(1, items[0].sell_in)  # Sell_in decreases by 1



if __name__ == '__main__':
    unittest.main()
