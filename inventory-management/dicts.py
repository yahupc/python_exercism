"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    """>>> create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
    {"coal":1, "wood":2, "diamond":3}
    """
    claves = []
    diccionario = {}
    for item in items:
        if item not in claves:
            claves.append(item)
    for clave in claves:
        diccionario[clave] = items.count(clave)
    return diccionario


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    inventario_previo = create_inventory(items)
    for key, value in inventory.items():
        for clave, valor in inventario_previo.items():
            if inventory[key] == inventario_previo[clave]:
                inventory[key] = value + valor

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if item in inventory:
            inventory[item] = max(0, inventory[item] - 1)
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        del inventory[item]

    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    lista = []
    for key, value in inventory.items():
        if value > 0:
            lista.append((key, value))

    return lista
