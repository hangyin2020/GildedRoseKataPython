# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Legendary item does not change
            
            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_passes(item)
            elif item.name.startswith("Conjured"):
                self._update_conjured_item(item)
            else:
                self._update_regular_item(item)

            item.sell_in -= 1

            if item.sell_in < 0:
                self._handle_expired_item(item)

    def _update_aged_brie(self, item):
        self._increase_quality(item)
    
    def _update_backstage_passes(self, item):
        self._increase_quality(item)
        if item.sell_in < 11:
            self._increase_quality(item)
        if item.sell_in < 6:
            self._increase_quality(item)
    
    def _update_conjured_item(self, item):
        self._decrease_quality(item, amount=2)
    
    def _update_regular_item(self, item):
        self._decrease_quality(item)
    
    def _handle_expired_item(self, item):
        if item.name == "Aged Brie":
            self._increase_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.quality = 0  # Expired backstage pass drops to 0
        elif item.name.startswith("Conjured"):
            self._decrease_quality(item, amount=2)
        else:
            self._decrease_quality(item)
    
    def _increase_quality(self, item):
        if item.quality < 50:
            item.quality += 1
    
    def _decrease_quality(self, item, amount=1):
        if item.quality > 0:
            item.quality -= amount
            if item.quality < 0:
                item.quality = 0

    def get_item(self):
        """Returns a list of item names"""
        return [item.name for item in self.items]
    