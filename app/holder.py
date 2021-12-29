from attrs import define, field

from .item import Item


@define
class Holder:
    items: list[Item] = field(factory=list)

    def add_item(self) -> Item:
        item: Item = Item(name=f"{len(self.items)}_ITEM", price=10, holder=self)
        self.items.append(item)
        return item
