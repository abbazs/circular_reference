from attrs import define, field
from .holder import Holder


@define
class Item:
    name: str
    holder: Holder = field(eq=False)
    price: float = field(eq=False, default=0)
