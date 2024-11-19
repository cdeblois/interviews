import sys

from gilded_rose import Item, GildedRose


def assert_same_items(item1: Item, item2: Item):
    assert (
        item1.name == item2.name
        and item1.sell_in == item2.sell_in
        and item1.quality == item2.quality
    ), f"{item1} != {item2}"


def test_gilded_rose(days=1):
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=1, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Elixir of the Mongoose", sell_in=1, quality=5),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=30),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             Item(name="New Product", sell_in=5, quality=10),
             # Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]
    gilded_rose = GildedRose(items)
    updated_items = [
        [
            Item(name="+5 Dexterity Vest", sell_in=9, quality=19),
            Item(name="Aged Brie", sell_in=0, quality=1),
            Item(name="Elixir of the Mongoose", sell_in=4, quality=6),
            Item(name="Elixir of the Mongoose", sell_in=0, quality=4),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=30),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=14, quality=21),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=50),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=50),
            Item(name="New Product", sell_in=4, quality=8),
            # Item(name="Conjured Mana Cake", sell_in=2, quality=4),  # <-- :O
        ],
        [
            Item(name="+5 Dexterity Vest", sell_in=8, quality=18),
            Item(name="Aged Brie", sell_in=-1, quality=3),
            Item(name="Elixir of the Mongoose", sell_in=3, quality=5),
            Item(name="Elixir of the Mongoose", sell_in=-1, quality=2),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=30),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=13, quality=22),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=50),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=50),
            Item(name="New Product", sell_in=3, quality=6),
            # Item(name="Conjured Mana Cake", sell_in=1, quality=2),  # <-- :O
        ],
    ]
    assert days <= len(updated_items), "TODO: handle more days"
    for day in range(days):
        gilded_rose.update_quality()
        for item, updated_item in zip(gilded_rose.items, updated_items[day]):
            assert_same_items(item, updated_item)


if __name__ == "__main__":
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    test_gilded_rose(days)
