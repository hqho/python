#!/usr/bin/env python3

import sys
import json
import os

def modify_list(lst, action, element=None, position=None):
    """
    Modify a list by inserting, removing, appending, printing, or clearing it.

    :param lst: The list to modify or print
    :param action: The action to perform ('insert', 'remove', 'append', 'print', or 'clear')
    :param element: The element to insert or remove (required for 'insert' and 'remove')
    :param position: The index at which to insert the element (only for 'insert')
    :return: The modified list
    :raises ValueError: If an invalid action is provided or if parameters are missing for the action
    :raises IndexError: If the position for insertion is out of range
    """
    if action == 'insert':
        if element is None or position is None:
            raise ValueError("Both 'element' and 'position' are required for 'insert' action.")
        if position < 0 or position > len(lst):
            raise IndexError("Position out of range")
        lst.insert(position, element)
    elif action == 'remove':
        if element is None:
            raise ValueError("'element' is required for 'remove' action.")
        if element not in lst:
            raise ValueError(f"Element {element} not found in the list")
        lst.remove(element)
    elif action == 'append':
        if element is None:
            raise ValueError("'element' is required for 'append' action.")
        lst.append(element)
    elif action == 'print':
        print(f"Current list: {lst}")
        return lst  # Return the list unchanged
    elif action == 'clear':
        lst.clear()  # Clear the list
    else:
        raise ValueError("Action must be 'insert', 'remove', 'append', 'print', or 'clear'")

    return lst

def main():
    list_file = 'list_data.json'

    if os.path.exists(list_file):
        with open(list_file, 'r') as f:
            my_list = json.load(f)
    else:
        my_list = []

    if len(sys.argv) < 2:
        print("Usage: python script.py <action> [element] [<position>]")
        print("Actions: insert, remove, append, print, clear")
        print("For 'insert', provide element and position as arguments.")
        print("For 'remove' and 'append', provide element.")
        print("For 'print' and 'clear', no additional arguments needed.")
        sys.exit(1)

    action = sys.argv[1]
    element = None
    position = None

    if action in ['insert', 'remove', 'append']:
        if len(sys.argv) < 3:
            print(f"For '{action}' action, please provide an element.")
            sys.exit(1)
        try:
            element = int(sys.argv[2])  # Assume elements are integers for simplicity
        except ValueError:
            print("Element must be an integer.")
            sys.exit(1)

    if action == 'insert':
        if len(sys.argv) < 4:
            print("For 'insert' action, please provide a position.")
            sys.exit(1)
        try:
            position = int(sys.argv[3])
        except ValueError:
            print("Position must be an integer.")
            sys.exit(1)

    try:
        modified_list = modify_list(my_list, action, element, position)
        if action not in ['print', 'clear']:
            print(f"Modified list: {modified_list}")
        else:
            if action == 'clear':
                print("List has been cleared.")

        # If the list is cleared, remove the file instead of writing an empty list
        if action == 'clear' and os.path.exists(list_file):
            os.remove(list_file)
        elif action != 'clear':  # Write back to file only if not clearing
            with open(list_file, 'w') as f:
                json.dump(modified_list, f)
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
