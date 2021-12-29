from rich import print

from .holder import Holder

if __name__ == "__main__":
    h = Holder()
    print(h.add_item())
    print(h.add_item())
