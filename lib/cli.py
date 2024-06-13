
from helpers import (
    # import functions from helpers
    exit_program,
    list_restaurants,
    find_restaurant_by_name,
    find_restaurant_by_id,
    create_restaurant,
    update_restaurant,
    delete_restaurant,  
    list_dishes,  
    find_dish_by_name,
    find_dish_by_id,
    create_dish,
    update_dish,
    delete_dish,
    list_dishes_by_restaurant_id,
)

def menu():
    #Print the menu that the user will be interacting with
    print("WELCOME TO RESTAURANT MANAGEMENT CLI")
    print("Please select an option:")
    print("0: Exit the program")
    print("1: List all restaurants")
    print("2: Find restaurant by name")
    print("3: Find restaurant by id")
    print("4: Create restaurant")
    print("5: Update restaurant")
    print("6: Delete restaurant")
    print("7: List dishes,")
    print("8: Find dish by name")
    print("9: Find dish by id")
    print("10: Create dish,")
    print("11: Update dish,")
    print("12: Delete dish,")
    print("13: List all dishes in a restaurant")

#Main function that runs the program and interacts with the user
def main():
    while True:
        print('ENTERING PROGRAM')
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_restaurants()
        elif choice == "2":
            find_restaurant_by_name()
        elif choice == "3":
            find_restaurant_by_id()
        elif choice == "4":
            create_restaurant()
        elif choice == "5":
            update_restaurant()
        elif choice == "6":
            delete_restaurant()
        elif choice == "7":
            list_dishes()
        elif choice == "8":
            find_dish_by_name()
        elif choice == "9":
            find_dish_by_id()
        elif choice == "10":
            create_dish()
        elif choice == "11":
            update_dish()
        elif choice == "12":
            delete_dish()
        elif choice == "13":
            list_dishes_by_restaurant_id()
        else:
            print("Invalid choice")


#Call the main function to run the program
if __name__ == "__main__":
    main()
