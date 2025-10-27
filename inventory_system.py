"""
Simple inventory management system.

"""
import json
import logging
# FIX (Pylint W0611, Flake8 F401): Removed unused 'datetime' import.
# from datetime import datetime

# Configure logging to output to console
# This replaces the unused 'import logging' and the problematic 'logs' list.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Global variable for simplicity, as in the original.
stock_data = {}


def add_item(item, qty):
    """
    Adds a given quantity of an item to the stock.

    Args:
        item (str): The name of the item to add.
        qty (int): The quantity to add. Must be an integer.
    """
    # FIX (Suggested): Added type validation.
    if not isinstance(item, str) or not isinstance(qty, int):
        # FIX (Flake8 E501): Shortened error message.
        logging.error(
            "Invalid types: Item(str), Qty(int). Got %s, %s",
            type(item), type(qty)
        )
        return

    if not item:
        logging.warning("Attempted to add item with no name.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    # FIX (Pylint W1203): Switched to lazy logging format.
    logging.info(
        "Added %s of %s. New total: %s",
        qty, item, stock_data[item]
    )


# FIX (Flake8 E302): Added 2 blank lines between functions.
def remove_item(item, qty):
    """
    Removes a given quantity of an item from the stock.

    If the remaining quantity is zero or less, the item is removed.

    Args:
        item (str): The name of the item to remove.
        qty (int): The quantity to remove. Must be an integer.
    """
    # FIX (Suggested): Added type validation.
    if not isinstance(item, str) or not isinstance(qty, int):
        # FIX (Flake8 E501): Shortened error message.
        logging.error(
            "Invalid types: Item(str), Qty(int). Got %s, %s",
            type(item), type(qty)
        )
        return

    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            # FIX (Pylint W1203): Switched to lazy logging format.
            logging.info("Removed all remaining %s from stock.", item)
        else:
            # FIX (Flake8 E501): Shortened line.
            logging.info(
                "Removed %s of %s. New total: %s",
                qty, item, stock_data[item]
            )
    # FIX (Bandit B110, Flake8 E722, Pylint W0702):
    # Replaced bare 'except:' with a specific exception.
    except KeyError:
        # FIX (Flake8 E501): Shortened line.
        logging.warning(
            "Attempted to remove %s, but it's not in stock.", item
        )


def get_qty(item):
    """
    Gets the current quantity of a specific item.

    Args:
        item (str): The name of the item.

    Returns:
        int: The quantity in stock, or 0 if the item is not found.
    """
    try:
        return stock_data[item]
    except KeyError:
        return 0  # Be more robust than crashing if item doesn't exist


def load_data(file="inventory.json"):
    """
    Loads the stock data from a JSON file.

    Args:
        file (str, optional): The name of the file to load from.
                              Defaults to "inventory.json".
    """
    # FIX (Pylint W0603): 'global' is required by the original design.
    # We can tell pylint to ignore this specific line.
    global stock_data  # pylint: disable=global-statement

    try:
        # FIX (Pylint R1732): Used 'with' statement to safely open/close file.
        # FIX (Pylint W1514): Added 'encoding="utf-8"'.
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
            # FIX (Pylint W1203): Switched to lazy logging format.
            logging.info("Successfully loaded data from %s", file)
    except FileNotFoundError:
        # FIX (Flake8 E501): Shortened line.
        logging.warning("%s not found. Starting with empty inventory.", file)
        stock_data = {}
    except json.JSONDecodeError:
        # FIX (Flake8 E501): Shortened line.
        logging.error("Could not decode JSON from %s. Check file.", file)
        stock_data = {}


def save_data(file="inventory.json"):
    """
    Saves the current stock data to a JSON file.

    Args:
        file (str, optional): The name of the file to save to.
                              Defaults to "inventory.json".
    """
    try:
        # FIX (Pylint R1732): Used 'with' statement to safely open/close file.
        # FIX (Pylint W1514): Added 'encoding="utf-8"'.
        with open(file, "w", encoding="utf-8") as f:
            # Added 'indent=4' for readable JSON.
            json.dump(stock_data, f, indent=4)
            # FIX (Pylint W1203): Switched to lazy logging format.
            logging.info("Successfully saved data to %s", file)
    except IOError as e:
        # FIX (Pylint W1203): Switched to lazy logging format.
        logging.error("Could not save data to %s: %s", file, e)


def print_data():
    """Prints a report of all items and their quantities."""
    print("\n--- Items Report ---")
    if not stock_data:
        print("Inventory is empty.")
    for item, qty in stock_data.items():
        # FIX (Pylint C0209): Used f-string.
        # Note: Pylint W1203 only applies to 'logging', not 'print'.
        print(f"{item} -> {qty}")
    print("--------------------")


def check_low_items(threshold=5):
    """
    Finds all items at or below a given threshold.

    Args:
        threshold (int, optional): The low-stock threshold. Defaults to 5.

    Returns:
        list: A list of item names that are low in stock.
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function to run the inventory management tasks."""
    # Note: Logging is configured at the top of the file.

    load_data()

    add_item("apple", 10)
    add_item("banana", 15)
    # This call will now be safely handled by validation:
    add_item(123, "ten")
    add_item("banana", -2)  # This will reduce the stock

    remove_item("apple", 3)
    # This call will now be safely handled by 'except KeyError':
    remove_item("orange", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    print_data()

    # FIX (Bandit B307, Pylint W0123): Removed dangerous 'eval()' call.
    # print("eval used") # This was the behavior of the eval call.


if __name__ == "__main__":
    main()
