# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            handler = self.get_handler(item)
            handler.update_quality()

    def get_handler(self, item):
        """Returns the appropriate handler for the given item."""
        if item.name == "Aged Brie":
            return AgedBrieHandler(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassHandler(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasHandler(item)
        elif item.name == "Conjured Mana Cake":
            return ConjuredItemHandler(item)
        elif item.name == "New Product":
            return NewProductItemHandler(item)
        else:
            return NormalItemHandler(item)


class ItemHandler:
    """Base class for item-specific behavior."""
    def __init__(self, item):
        self.item = item

    def update_quality(self):
        """Default behavior for normal items."""
        self.update_sell_in()
        self.update_quality_value()

    def update_sell_in(self):
        self.item.sell_in -= 1

    def update_quality_value(self):
        if self.item.quality > 0:
            self.item.quality -= 1
            if self.item.sell_in < 0:
                self.item.quality -= 1
        self.item.quality = max(0, self.item.quality)  # Ensure quality doesn't drop below 0

class NormalItemHandler(ItemHandler):
    """Handler for normal items with default behavior."""
    def update_quality_value(self):
        if self.item.quality > 0:
            self.item.quality -= 1
            if self.item.sell_in < 0:
                self.item.quality -= 1
        self.item.quality = max(0, self.item.quality)  # Ensure quality doesn't drop below 0

class NewProductItemHandler(ItemHandler):
    """Handler for normal items with default behavior."""
    def update_quality_value(self):
        if self.item.quality > 0:
            self.item.quality -= 2
            if self.item.sell_in < 0:
                self.item.quality -= 1
        self.item.quality = max(0, self.item.quality)  # Ensure quality doesn't drop below 0

class AgedBrieHandler(ItemHandler):
    def update_quality_value(self):
        if self.item.quality < 50:
            self.item.quality += 1
            if self.item.sell_in < 0:
                self.item.quality += 1
        self.item.quality = min(50, self.item.quality)  # Ensure quality doesn't exceed 50


class BackstagePassHandler(ItemHandler):
    def update_quality_value(self):
        if self.item.sell_in < 0:
            self.item.quality = 0
        elif self.item.sell_in < 5:
            self.item.quality += 3
        elif self.item.sell_in < 10:
            self.item.quality += 2
        else:
            self.item.quality += 1
        self.item.quality = min(50, self.item.quality)  # Ensure quality doesn't exceed 50


class SulfurasHandler(ItemHandler):
    def update_sell_in(self):
        """Sulfuras does not decrease in sell_in."""
        pass

    def update_quality_value(self):
        """Sulfuras quality does not change."""
        pass


class ConjuredItemHandler(ItemHandler):
    def update_quality_value(self):
        if self.item.quality > 0:
            self.item.quality -= 2
            if self.item.sell_in < 0:
                self.item.quality -= 2
        self.item.quality = max(0, self.item.quality)  # Ensure quality doesn't drop below 0
       

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
