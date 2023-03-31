# -*- coding: utf-8 -*-
import unittest
from guilded_rose import Item, update_quality


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 2, 80)]
        update_quality(items)
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEquals(80, items[0].quality)
        self.assertEquals(2, items[0].sell_in)


if __name__ == "__main__":
    unittest.main()
