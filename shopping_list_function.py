# create a shopping list program with functions to display help info, append items to list and display current list
# functions: show_help, show_list, append_items,

#lists can be declared using list() or []
shopping_list = []

def show_help():
    print("Type HELP to get help, DONE to stop adding items or SHOW to print current list of items")
    print("Type your items and press the enter key after each item")

def show_list():
    print("Here is your list of items below:")
    for item in shopping_list:
        print(item)

def append_items():
    shopping_list.append(new_item)


show_help()

while True:
    new_item = input(">>> ")
    if new_item == "HELP":
        show_help()
        continue
    elif new_item == "DONE":
        show_list()
        break
    else:
        append_items()
        continue
