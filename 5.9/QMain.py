import module_library_actions
import module_costants


def manage_library():
    my_library = []
    print("welcome to the library")
    module_library_actions.print_menu()
    user_choice = int(input("Enter choice number"))

    while user_choice != module_costants.EXIT:
        if user_choice == module_costants.PRINT_ALL:
            module_library_actions.print_book_list(my_library)
        else:
            book_name = input("Enter book name")
            if user_choice == module_costants.ADD:
                module_library_actions.add_book(my_library, book_name)
            elif user_choice == module_costants.REMOVE:
                is_found = module_library_actions.remove_book(my_library, book_name)
                if not is_found:
                    print("book does not exist")
            elif user_choice == module_costants.SEARCH:
                result_list = module_library_actions.search_name(my_library, book_name)
                if len(result_list) == 0:
                    print("book does not found")
                else:
                    module_library_actions.print_book_list(result_list)
            else:
                print("choice doesn't found, please try again")

        module_library_actions.print_menu()
        user_choice = int(input("Enter choice number"))


manage_library()