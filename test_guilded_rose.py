# -*- coding: utf-8 -*-
import unittest
from guilded_rose import Item, update_quality


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 2, 80)]
        update_quality(items)
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(80, items[0].quality)
        self.assertEqual(2, items[0].sell_in)

    def test_backstage_passes_quality(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 2, 30),
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 33)
        ]
        update_quality(items)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(33, items[0].quality)
        self.assertEqual(1, items[0].sell_in)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[1].name)
        self.assertEqual(0, items[1].quality)
        self.assertEqual(-1, items[1].sell_in)

    def test_non_special_item_quantity(self):
        items = [
            Item("Scented candle", 5, 40),
            Item("Scented candle", 0, 30),
            Item("Scented candle", -1, 28)
        ]
        update_quality(items)
        self.assertEqual("Scented candle", items[0].name)
        self.assertEqual(39, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

        self.assertEqual("Scented candle", items[1].name)
        self.assertEqual(28, items[1].quality)
        self.assertEqual(-1, items[1].sell_in)

        self.assertEqual("Scented candle", items[2].name)
        self.assertEqual(26, items[2].quality)
        self.assertEqual(-2, items[2].sell_in)


if __name__ == "__main__":
    unittest.main()
