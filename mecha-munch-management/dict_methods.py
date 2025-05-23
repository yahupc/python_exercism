"""Functions to manage a users shopping cart items."""

from collections import OrderedDict


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.

    """

    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    dict = {}
    for item in notes:
        if item not in dict:
            dict.setdefault(item, notes.count(item))
    return dict


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.

    """
    nuevo_diccionario = {}
    for item, value in cart.items():
        if item in aisle_mapping:
            nuevo_diccionario[item] = [
                value,
                aisle_mapping[item][0],
                aisle_mapping[item][1],
            ]
        else:
            nuevo_diccionario[item] = [
                value,
                None,
                None,
            ]
    nuevo1 = OrderedDict(reversed(sorted(nuevo_diccionario.items())))

    return nuevo1


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for index, value in fulfillment_cart.items():
        if index in store_inventory:
            nuevo_valor = store_inventory[index][0] - value[0]
            if nuevo_valor > 0:
                store_inventory[index][0] = nuevo_valor
            else:
                store_inventory[index][0] = "Out of Stock"
    return store_inventory
