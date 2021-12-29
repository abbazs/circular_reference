from __future__ import annotations
from typing import TYPE_CHECKING

from attrs import define, field

if TYPE_CHECKING:
    from .holder import Holder


@define
class Item:
    name: str
    holder: Holder = field(eq=False)
    price: float = field(eq=False, default=0)
