shopping_list = []


def view_list():
    if shopping_list:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")


def add_item():
    item = input("Enter an item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' added to the list.")
    else:
        print("Item cannot be empty.")


def remove_item():
    if shopping_list:
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
        try:
            index = int(input("Enter the item number to remove: "))
            if 1 <= index <= len(shopping_list):
                removed_item = shopping_list.pop(index - 1)
                print(f"'{removed_item}' removed from the list.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Your shopping list is empty.")


def search_item():
    search_term = input("Enter the item to search for: ").strip().lower()
    found_items = [item for item in shopping_list if search_term in item.lower()]
    if found_items:
        print("\nFound items:")
        for item in found_items:
            print(item)
    else:
        print("No matching items found.")


while True:
    print("\n--- Shopping List ---")
    print("1. View List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Search Item")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        view_list()

    elif choice == "2":
        add_item()

    elif choice == "3":
        remove_item()

    elif choice == "4":
        search_item()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
