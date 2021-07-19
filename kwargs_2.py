# key word arguments
def add_item(title,*item):
    print(title)
    if item is not None:
        print("\t",item)

add_item("Shopping_list")