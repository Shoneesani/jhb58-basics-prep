def to_do_list():
    my_list = []
    while True:
        menu = input("press a to add items, v to view, q to exit or r to remove: ")
        if menu == "q":
            break
        elif menu == "r":
            task = input("remove task: ")
            if task in my_list:
                my_list.remove(task)
                print(f"{task} removed")
        elif menu == "a":
            task = input("add task: ")
            my_list.append(task)
            print(f"{task} added")
        elif menu == "v":
            for item in my_list:
                print(item)
            return my_list
        
to_do_list()
