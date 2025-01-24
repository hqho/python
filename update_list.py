#!/usr/bin/env python3

import sys
import json
import os

def modify_list(lst, action, element=None, position=None, new_element=None):
    """
    Modify a list by inserting, removing, appending, printing, clearing, finding, or updating an element.

    :param lst: The list to modify or print
    :param action: The action to perform ('insert', 'remove', 'append', 'print', 'clear', 'find', or 'update')
    :param element: The element to insert, remove, or find (required for 'insert', 'remove', and 'find')
    :param position: The index at which to insert or update the element (required for 'insert' and 'update')
    :param new_element: The new element value for 'update'
    :return: The modified list or index if finding
    :raises ValueError: If an invalid action is provided or if parameters are missing for the action
    :raises IndexError: If the position for insertion or update is out of range
    """
    if action == 'insert':
        if element is None or position is None:
            raise ValueError("Both 'element' and 'position' are required for 'insert' action.")
        if position < 0 or position > len(lst):
            raise IndexError("Position out of range")
        lst.insert(position, element)
        return lst
    elif action == 'remove':
        if element is None:
            raise ValueError("'element' is required for 'remove' action.")
        if element not in lst:
            raise ValueError(f"Element {element} not found in the list")
        lst.remove(element)
        return lst
    elif action == 'append':
        if element is None:
            raise ValueError("'element' is required for 'append' action.")
        lst.append(element)
        return lst
    elif action == 'print':
        print(f"Current list: {lst}")
        return lst  # Return the list unchanged
    elif action == 'clear':
        lst.clear()  # Clear the list
        return lst
    elif action == 'find':
        if element is None:
            raise ValueError("'element' is required for 'find' action.")
        try:
            index = lst.index(element)
            return index  # Return the index if found
        except ValueError:
            return -1  # Return -1 if the element is not found
    elif action == 'update':
        if position is None or new_element is None:
            raise ValueError("Both 'position' and 'new_element' are required for 'update' action.")
        if position < 0 or position >= len(lst):
            raise IndexError("Position out of range for update")
        lst[position] = new_element
        return lst
    else:
        raise ValueError("Action must be 'insert', 'remove', 'append', 'print', 'clear', 'find', or 'update'")

def main():
    list_file = 'list_data.json'

    if os.path.exists(list_file):
        with open(list_file, 'r') as f:
            my_list = json.load(f)
    else:
        my_list = []

    if len(sys.argv) < 2:
        print("Usage: python script.py <action> [element] [position] [new_element]")
        print("Actions: insert, remove, append, print, clear, find, update")
        print("For 'insert', provide element and position as arguments.")
        print("For 'remove', 'append', and 'find', provide element.")
        print("For 'update', provide position and new_element.")
        print("For 'print' and 'clear', no additional arguments needed.")
        sys.exit(1)

    action = sys.argv[1]
    element = None
    position = None
    new_element = None

    if action in ['insert', 'remove', 'append', 'find']:
        if len(sys.argv) < 3:
            print(f"For '{action}' action, please provide an element.")
            sys.exit(1)
        try:
            element = int(sys.argv[2])  # Assume elements are integers for simplicity
        except ValueError:
            print("Element must be an integer.")
            sys.exit(1)

    if action in ['insert', 'update']:
        if len(sys.argv) < 4:
            print(f"For '{action}' action, please provide a position.")
            sys.exit(1)
        try:
            position = int(sys.argv[3])
        except ValueError:
            print("Position must be an integer.")
            sys.exit(1)

    if action == 'update':
        if len(sys.argv) < 4:
            print("For 'update' action, please provide a position and a new element.")
            sys.exit(1)
        try:
            new_element = int(sys.argv[3])
        except ValueError:
            print("New element must be an integer.")
            sys.exit(1)

    try:
        result = modify_list(my_list, action, element, position, new_element)
        if action in ['print']:
            pass  # Printing is handled within the function
        elif action == 'clear':
            print("List has been cleared.")
        elif action == 'find':
            if result == -1:
                print(f"Element {element} not found in the list.")
            else:
                print(f"Element {element} found at index: {result}")
        elif action == 'update':
            print(f"Updated list: {result}")
        else:
            print(f"Modified list: {result}")

        # If the list is cleared, remove the file instead of writing an empty list
        if action == 'clear' and os.path.exists(list_file):
            os.remove(list_file)
        elif action != 'clear':  # Write back to file only if not clearing
            with open(list_file, 'w') as f:
                json.dump(result if isinstance(result, list) else my_list, f)
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
