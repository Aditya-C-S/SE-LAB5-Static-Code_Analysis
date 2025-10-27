import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Adds item and quantity to stock."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid item or quantity")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Removes quantity of an item from stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found.")


def get_qty(item):
    """Returns quantity of item if exists."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Loads stock data from JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error loading inventory file")


def save_data(file="inventory.json"):
    """Saves stock data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=2)


def print_data():
    """Prints all items and quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Finds items below threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("chips", 5)

    remove_item("apple", 3)
    remove_item("orange", 1)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())

    save_data()
    load_data()

    print_data()
    print("Static analysis fixes applied successfully!")  # Removed eval()


if __name__ == "__main__":
    main()
