# -*- coding: utf-8 -*-
import unittest
from guilded_rose import AgedBrie, BackstagePasses, Item, Sulphuras, update_quality


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras_quality(self):
        items = [
                Sulphuras("Sulfuras, Hand of Ragnaros", 2, 80),
                Sulphuras("Sulfuras, Hand of Ragnaros", 2, 60)
                ]
        update_quality(items)
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(80, items[0].quality)
        self.assertEqual(2, items[0].sell_in)

        self.assertEqual("Sulfuras, Hand of Ragnaros", items[1].name)
        self.assertEqual(60, items[1].quality)
        self.assertEqual(2, items[1].sell_in)
    

    def test_backstage_passes_quality(self):
        items = [
            BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 2, 30),
            BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 0, 33),
            BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 11, 40),
            BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 9, 12),
            BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 10, 12),
            BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 10, 49)
        ]
        update_quality(items)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(33, items[0].quality)
        self.assertEqual(1, items[0].sell_in)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[1].name)
        self.assertEqual(0, items[1].quality)
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
        self.assertEqual(50, items[5].quality)
        self.assertEqual(9, items[5].sell_in)

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
            AgedBrie("Aged Brie", 5, 40),
            AgedBrie("Aged Brie", 0, 20),
            AgedBrie("Aged Brie", 0, 50),
            AgedBrie("Aged Brie", -1, 49),
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
