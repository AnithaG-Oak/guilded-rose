# -*- coding: utf-8 -*-
import unittest
from guilded_rose import Item, update_quality


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=2, quality=80)]
        update_quality(items)
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(80, items[0].quality)
        self.assertEqual(2, items[0].sell_in)
    

    def test_backstage_passes_quality(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=30),
            Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=33),
            Item("Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=40),
            Item("Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=12),
            Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=12),
            Item("Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=30),
        ]
        update_quality(items)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(33, items[0].quality)
        self.assertEqual(1, items[0].sell_in)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[1].name)
        self.assertEqual(36, items[1].quality)
        self.assertEqual(-1, items[1].sell_in)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[2].name)
        self.assertEqual(41, items[2].quality)
        self.assertEqual(10, items[2].sell_in)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[3].name)
        self.assertEqual(14, items[3].quality)
        self.assertEqual(8, items[3].sell_in)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[4].name)
        self.assertEqual(14, items[4].quality)
        self.assertEqual(9, items[4].sell_in)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[5].name)
        self.assertEqual(0, items[5].quality)
        self.assertEqual(-2, items[5].sell_in)

    def test_non_special_item_quantity(self):
        items = [
            Item("Scented candle", 5, 40),
            Item("Scented candle", 0, 30),
            Item("Scented candle", -1, 28),
            Item("Scented candle", 1, 0),
            Item("Scented candle", -1, 1),
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

        self.assertEqual("Scented candle", items[3].name)
        self.assertEqual(0, items[3].quality)
        self.assertEqual(0, items[3].sell_in)

        self.assertEqual("Scented candle", items[4].name)
        self.assertEqual(0, items[4].quality)
        self.assertEqual(-2, items[4].sell_in)

    def test_aged_brie_quality(self):
        items = [
            Item("Aged Brie", 5, 40),
            Item("Aged Brie", 0, 20),
            Item("Aged Brie", 0, 50),
            Item("Aged Brie", -1, 49),
        ]
        update_quality(items)
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(41, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

        self.assertEqual("Aged Brie", items[1].name)
        self.assertEqual(22, items[1].quality)
        self.assertEqual(-1, items[1].sell_in)

        self.assertEqual("Aged Brie", items[2].name)
        self.assertEqual(50, items[2].quality)
        self.assertEqual(-1, items[2].sell_in)

        self.assertEqual("Aged Brie", items[3].name)
        self.assertEqual(50, items[3].quality)
        self.assertEqual(-2, items[3].sell_in)


if __name__ == "__main__":
    unittest.main()
