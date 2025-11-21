spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    #Return a list of names of the foods
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    #Return a list of foods with heat_level greater than 5
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    #Print all foods formatted with heat_level as an emojis
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    #Return the food dictionary that matches the given cuisine
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None  # if their is no match

def print_spiciest_foods(spicy_foods):
    #Print foods with heat_level > 5 formatted with the emojis
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


def get_average_heat_level(spicy_foods):
    #Return the average heat_level of all foods
    total = sum(food['heat_level'] for food in spicy_foods)
    return total // len(spicy_foods)  #  division for average

def create_spicy_food(spicy_foods, new_food): #changed it to new food 
    #Return a new list with new_food added
    return spicy_foods + [new_food]
