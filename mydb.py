#!/usr/bin/env python3

import json
import os

# JSON file to store the dictionary
FILE_NAME = "my_inventory.json"

def load_inventory():
    """Load the inventory from the JSON file, or initialize an empty dictionary if the file doesn't exist."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_inventory(inventory):
    """Save the inventory to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file)

def add_item(inventory):
    """Add or update an item in the inventory."""
    item = input("Enter the item name to add/update: ")
    quantity = input(f"Enter the quantity for '{item}': ")

    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid quantity. Please enter a positive number.")
        return

    quantity = int(quantity)

    if item in inventory:
        print(f"Current price for '{item}' is {inventory[item]['price']:.2f}.")
        price = input(f"Enter the price for '{item}' (or press Enter to keep the current price): ")

        if price == "":
            price = inventory[item]['price']
        elif not price.replace('.', '', 1).isdigit() or float(price) <= 0:
            print("Invalid price. Please enter a positive number.")
            return
        else:
            price = float(price)

        inventory[item]["quantity"] += quantity
        inventory[item]["price"] = price
        print(f"Updated '{item}': quantity {inventory[item]['quantity']}, price {inventory[item]['price']:.2f}.")
    else:
        price = input(f"Enter the price for '{item}': ")
        if not price.replace('.', '', 1).isdigit() or float(price) <= 0:
            print("Invalid price. Please enter a positive number.")
            return

        price = float(price)
        inventory[item] = {"quantity": quantity, "price": price}
        print(f"Added '{item}' with quantity {quantity} and price {price:.2f}.")

    save_inventory(inventory)

def adjust_price(inventory):
    """Adjust the price of an item in the inventory."""
    item = input("Enter the item name to adjust the price: ")
    if item in inventory:
        print(f"Current price for '{item}' is {inventory[item]['price']:.2f}.")
        new_price = input(f"Enter the new price for '{item}': ")

        if not new_price.replace('.', '', 1).isdigit() or float(new_price) <= 0:
            print("Invalid price. Please enter a positive number.")
            return

        new_price = float(new_price)
        inventory[item]["price"] = new_price
        print(f"Updated price for '{item}' is now {new_price:.2f}.")
        save_inventory(inventory)
    else:
        print(f"'{item}' is not in the inventory.")

def deduct_quantity(inventory):
    """Deduct a specified quantity from an item in the inventory."""
    item = input("Enter the item name to deduct from: ")
    if item in inventory:
        quantity = input(f"Enter the quantity to deduct from '{item}': ")

        if not quantity.isdigit() or int(quantity) <= 0:
            print("Invalid quantity. Please enter a positive number.")
            return

        quantity = int(quantity)
        if quantity > inventory[item]["quantity"]:
            print(f"Cannot deduct {quantity}. '{item}' only has {inventory[item]['quantity']} in stock.")
        else:
            inventory[item]["quantity"] -= quantity
            print(f"Deducted {quantity} from '{item}'. Remaining quantity: {inventory[item]['quantity']}.")
            if inventory[item]["quantity"] == 0:
                print(f"'{item}' has been removed from the inventory as its quantity is now 0.")
                del inventory[item]

        save_inventory(inventory)
    else:
        print(f"'{item}' is not in the inventory.")

def remove_item(inventory):
    """Remove an item from the inventory, with a warning and confirmation."""
    item = input("Enter the item name to remove: ")
    if item in inventory:
        print(f"Warning: You are about to remove '{item}' from the inventory.")
        confirm = input("Are you sure? (yes/no): ").strip().lower()
        if confirm == "yes":
            del inventory[item]
            save_inventory(inventory)
            print(f"'{item}' has been removed from the inventory.")
        else:
            print(f"'{item}' was not removed.")
    else:
        print(f"'{item}' is not in the inventory.")

def print_inventory(inventory):
    """Print the current inventory in a table format."""
    if inventory:
        print(f"\n{'Item':<20}{'Quantity':<10}{'Price':<10}{'Total':<10}")
        print("-" * 50)
        for item, details in sorted(inventory.items()):
            total = details["quantity"] * details["price"]
            print(f"{item:<20}{details['quantity']:<10}{details['price']:<10.2f}{total:<10.2f}")
        print("-" * 50)
    else:
        print("The inventory is empty.")

def find_item(inventory):
    """Find an item in the inventory and return its quantity, price, and total value."""
    item = input("Enter the item name to find: ")
    if item in inventory:
        quantity = inventory[item]["quantity"]
        price = inventory[item]["price"]
        total = quantity * price
        print(f"'{item}' has quantity {quantity}, price {price:.2f}, and total value {total:.2f}.")
    else:
        print(f"'{item}' is not in the inventory.")

def display_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Print the inventory")
    print("4. Find an item's details")
    print("5. Deduct quantity from an item")
    print("6. Adjust the price of an item")
    print("7. Exit")

def main():
    """Main function to handle the menu and user choices."""
    inventory = load_inventory()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            remove_item(inventory)
        elif choice == "3":
            print_inventory(inventory)
        elif choice == "4":
            find_item(inventory)
        elif choice == "5":
            deduct_quantity(inventory)
        elif choice == "6":
            adjust_price(inventory)
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Run the program
if __name__ == "__main__":
    main()
