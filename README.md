Python Inventory System

This is a simple command-line inventory management system written in Python. It allows you to add, remove, and check the stock of items. The inventory is saved to and loaded from a inventory.json file.

This project was refactored as part of a software engineering lab to improve code quality, security, and robustness using static analysis tools (Pylint, Bandit, and Flake8).

Features

Add/Remove Items: Change the quantity of items in stock.

Persistent Storage: Inventory is saved to inventory.json automatically.

Logging: All operations are logged to the console.

Safe & Robust: Includes type validation and error handling to prevent crashes.

How to Run

Ensure you have Python 3 installed.

Run the script from your terminal:

python inventory_system.py


The script will automatically create inventory.json if one does not exist and print an item report to the console when it finishes. You can modify the main() function in inventory_system.py to change which items are added or removed.
