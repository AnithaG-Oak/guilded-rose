# -*- coding: utf-8 -*-



def update_quality(items):
    
    for item in items:
        item.update()

    return items




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
        if self.quality > 0:
            self.quality = self.quality - 1 
        if self.sell_in < 0 and self.quality > 0:
            self.quality = self.quality - 1  
    
    def check_quality_limit(self):
        if self.quality>50:
            self.quality=50



class Sulphuras(Item):
    def update(self):
        return
    
class AgedBrie(Item):
    def update_quality(self):
        self.quality = self.quality + 1
        if self.sell_in < 0:
            self.quality = self.quality + 1 
        

class BackstagePasses(Item):
    def update_quality(self):
        self.quality = self.quality + 1
        if self.sell_in < 10:
            self.quality = self.quality + 1
        if self.sell_in < 5:
            self.quality = self.quality + 1  
        if self.sell_in < 0:
            self.quality = 0 
        
