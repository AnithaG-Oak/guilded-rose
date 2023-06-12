# -*- coding: utf-8 -*-



def update_quality(items):
    for item in items:
        item.update()


MAX_QUALITY_LIMIT=50
MIN_QUALITY_LIMIT=0

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def update(self):
        self.update_sell_in()
        self.update_quality()
        self.check_quality_limit()

    def update_sell_in(self):
        self.sell_in = self.sell_in - 1 

    def update_quality(self):
        if self.sell_in >= 0:
            self.quality = self.quality - 1 
        else:
            self.quality = self.quality - 2
    
    def check_quality_limit(self):
        if self.quality>MAX_QUALITY_LIMIT:
            self.quality=MAX_QUALITY_LIMIT
        if self.quality < MIN_QUALITY_LIMIT:
            self.quality = MIN_QUALITY_LIMIT

    
class AgedBrie(Item):
    def update_quality(self):
        if self.sell_in >= 0:
            self.quality = self.quality + 1
        else:
            self.quality = self.quality + 2
        
class BackstagePasses(Item):
    def update_quality(self):
        if self.sell_in >= 10:
            self.quality = self.quality + 1
        elif self.sell_in in range(5,10): 
            self.quality = self.quality + 2
        elif self.sell_in in range(0,5): 
            self.quality = self.quality + 3
        elif self.sell_in < 0:
            self.quality = 0 

class Sulphuras(Item):
    def update(self):
        return
    
class Conjured(Item):
    def update_quality(self):
        if self.sell_in >= 0:
            self.quality = self.quality - 2 
        else:
            self.quality = self.quality - 4
        
