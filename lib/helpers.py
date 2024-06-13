from models.restaurant import Restaurant
from models.dishes import Dish



def exit_program():
    print('EXITING PROGAM')
    print("Goodbye!")
    exit()


def list_restaurants():
    restaurants = Restaurant.get_all()
    for restaurant in restaurants:
        print(restaurant)


    
def find_restaurant_by_name():
    name = input("Enter the Restaurant's name: ")
    restaurant = Restaurant.find_by_name(name)
    if restaurant:
        print(restaurant)
    else:
        print(f'{name} not found')


    
def find_restaurant_by_id():
        id_ = input("Enter the Restaurant's id: ")
        restaurant = Restaurant.find_by_id(id_)
        if restaurant:
            print(restaurant)
        else:
            print(f'{id_} not found')


     
def create_restaurant():
        name = input("Enter the Restaurant's name: ")
        location = input("Enter the Restaurant's location: ")
        try:
            restaurant = Restaurant.create(name, location)
            print(f'Creating {restaurant}')
            print('Restaurant created')
        except Exception as exc:
            print("Error creating Restaurant: ", exc)


     
def update_restaurant():
        id_ = input("Enter the Restaurant's id: ")
        if restaurant := Restaurant.find_by_id(id_):
            try:
                name = input("Enter the Restaurant's new name: ")
                restaurant.name = name
                location = input("Enter the Restaurant's new location: ")
                restaurant.location = location

                restaurant.update()
                print(f'Updating {restaurant}')
                print('Restaurant updated')
            except Exception as exc:
                print("Error updating Restaurant: ", exc)
        else:
            print(f'Restaurant {id_} not found')


       
def delete_restaurant():
        id_ = input("Enter the Restaurant's id: ")
        if restaurant := Restaurant.find_by_id(id_):
            restaurant.delete()
            print(f'{id_} deleted')
        else:
            print(f'{id_} not found')


    
def list_dishes():
        dish = Dish.get_all()
        for dish in dish:
            print(dish)


    
def find_dish_by_name():
        name = input("Enter the name of the Dish: ")
        dish = Dish.find_by_name(name)
        if dish:
            print(dish)
        else:
            print(f'{name} not found')


               
def find_dish_by_id():
        id_ = input("Enter the id of the Dish: ")
        dish = dish.find_by_id(id_)
        if dish:
            print(dish)
        else:
            print(f'{id_} not found')


    
def create_dish():
        name = input("Enter the name of the Dish: ")
        price = input("Enter the price of the Dish: ")
        restaurant_id = input("Enter the Restaurant id of the Dish: ")
        try:
            dish = Dish.create(name, price, restaurant_id)
            print(f'Creating {dish}')
            print('Dish created')
        except Exception as exc:
            print("Error creating Dish: ", exc)

   
def update_dish():
        id_ = input("Enter the dish's id: ")
        if dish := dish.find_by_id(id_):
            try:
                name = input("Enter the new name of the Dish: ")
                dish.name = name
                price = input("Enter the new price of the Dish: ")
                dish.price = price
                restaurant_id = input("Enter the new Restaurant id of the Dish: ")
                dish.restaurant_id = restaurant_id

                dish.update()
                print(f'Updating {dish}')
                print('Dish updated')
            except Exception as exc:
                print("Error updating Dish: ", exc)
        else:
            print(f'{id_} not found')


   
def delete_dish():
        id_ = input('Enter the id of the Dish: ')
        if dish := Dish.find_by_id(id_):
            dish.delete()
            print(f'{id_} deleted')
        else:
            print(f'{id_} not found')


    
def list_dishes_by_restaurant_id():
        id_ = input('Enter the id of the Restaurant: ')
        if dish := Restaurant.find_by_id(id_):
            dishes = Restaurant.get_dishes()
            for dish in dishes:
                print(dish)
        else:
            print(f'{id_} not found')