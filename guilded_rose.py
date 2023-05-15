# -*- coding: utf-8 -*-
from enum import Enum
class ItemName(str,Enum):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_TAFKAL80ETC ="Backstage passes to a TAFKAL80ETC concert"
    SULFURAS="Sulfuras, Hand of Ragnaros"


    

def update_quality(items):
    for item in items:
        # Normal Item
        if item.name not in [ItemName.AGED_BRIE.value, ItemName.BACKSTAGE_TAFKAL80ETC.value, ItemName.SULFURAS.value]:
            if item.quality > 0:
                item.quality = item.quality - 1
                

        else:
            # Special Item
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == ItemName.BACKSTAGE_TAFKAL80ETC.value:
                    if item.sell_in <= 10 and item.quality < 50:
                        item.quality = item.quality + 1
                    if item.sell_in <=5 and item.quality < 50:
                        item.quality = item.quality + 1

        if item.name != ItemName.SULFURAS.value:
            item.sell_in = item.sell_in - 1

        if item.name == ItemName.AGED_BRIE.value:
            if item.quality < 50 and item.sell_in < 0:
                item.quality = item.quality + 1
         
        if item.name not in [ItemName.AGED_BRIE.value, ItemName.BACKSTAGE_TAFKAL80ETC.value, ItemName.SULFURAS.value]:
            if item.sell_in < 0 and item.quality > 0:
                item.quality = item.quality - 1

        if item.sell_in < 0:
            if item.name != ItemName.AGED_BRIE.value:
                if item.name != ItemName.BACKSTAGE_TAFKAL80ETC.value:
                    pass
                else:
                    item.quality = item.quality - item.quality
                
    return items


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
