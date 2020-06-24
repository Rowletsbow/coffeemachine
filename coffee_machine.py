from datetime import datetime, time

available_money = 0
available_water = 0
available_milk = 0
available_coffee_beans = 0
available_disposable_cups = 0


def processing():
    print('Initiating coffee engines')
    print('Disintegrating coffee beans')
    print('Boiling water')
    print('Formulating coffee solution')
    print('Pouring coffee in the cup')
    print('Finalising emulsion by adding milk')
    print('Enjoy! :)')
    

# def cup_calculator(coffee_ingredients):
#     cups_possible1 = 0
#     cups_possible2 = 0
#     cups_possible3 = 0
#     cups_possible_list = []
#     cups_possible_list2 = []
#     if ingredient_checker(coffee_ingredients):
#         for key, value in coffee_ingredients.items():
#             if key == 'water':
#                 if value != 0:
#                     cups_possible1 = (available_water // coffee_ingredients['water'])
#                     cups_possible_list.append(cups_possible1 - number_of_cups)
#             elif key == 'milk':
#                 if value != 0:
#                     cups_possible2 = (available_milk // coffee_ingredients['milk'])
#                     cups_possible_list.append(cups_possible2 - number_of_cups)
#             elif key == 'coffee_beans':
#                 if value != 0:
#                     cups_possible3 = (available_coffee_beans // coffee_ingredients['coffee_beans'])
#                     cups_possible_list.append(cups_possible3 - number_of_cups)
#         extra_possible_cups = max(cups_possible_list)
#         if extra_possible_cups > 0:
#             print('Yes, I can make this amount of coffee (and ',
#                   extra_possible_cups,
#                   ' cup(s) more too!)\n')
#         else:
#             print('Yes, I can make this amount of coffee,'
#                   ' this is the maximum amount of coffee I can make right now.\n')
#     else:
#         for key, value in coffee_ingredients.items():
#             if key == 'water':
#                 if value != 0:
#                     cups_possible1 = (available_water // coffee_ingredients['water'])
#                     cups_possible_list2.append(cups_possible1)
#             elif key == 'milk':
#                 if value != 0:
#                     cups_possible2 = (available_milk // coffee_ingredients['milk'])
#                     cups_possible_list2.append(cups_possible2)
#             elif key == 'coffee_beans':
#                 if value != 0:
#                     cups_possible3 = (available_coffee_beans // coffee_ingredients['coffee_beans'])
#                     cups_possible_list2.append(cups_possible3)
#         maximum_possible_cups = min(cups_possible_list2)
#         print('Sorry, but I can only make ',
#               maximum_possible_cups,
#               ' cup(s) right now :(\n')


# when called, shows remaining ingredients, cups, and
# money in the coffee machine
def show_machine_status():
    print('Current Machine Status:\n',
          available_water, 'ml of water\n',
          available_milk, 'ml of milk\n',
          available_coffee_beans, 'grams of coffee beans\n',
          available_disposable_cups, 'disposable cups\n',
          available_money, 'money\n')


# when called, shows list of possible options
# for the user to choose to make the coffee
# machine do something
def show_main_menu():
    now = datetime.now()
    now_time = now.time()
    greeting = ''
    if time(6, 0) <= now_time <= time(12, 0):
        greeting = 'Good morning!'
    elif time(12, 0) < now_time < time(18, 0):
        greeting = 'Good afternoon!'
    elif time(18, 0) <= now_time <= time(23, 59):
        greeting = 'Good evening!'
    else:
        greeting = 'All the best!'

    print('{} What would you like to do? :)\n'.format(greeting),
          '1. Buy\n',
          '2. Fill\n',
          '3. Take\n',
          '4. Remaining\n',
          '5. Exit\n')


# changes remaining items in coffee machine
# according to sign of arguments given e.g.
# -10 will reduce 10 from variable while 10
# would increase 10 in the variable
def change_machine_status(req_water, req_milk, req_coffee_beans,
                          money, req_cups):
    global available_money
    available_money = available_money + money
    global available_disposable_cups
    available_disposable_cups = available_disposable_cups + req_cups
    global available_water
    available_water = available_water + req_water
    global available_coffee_beans
    available_coffee_beans = available_coffee_beans + req_coffee_beans
    global available_milk
    available_milk = available_milk + req_milk


class Coffee:
    def __init__(self,
                 req_water,
                 req_milk,
                 req_coffee_beans,
                 req_disposable_cups,
                 cost):
        self.ingredients = {'water': req_water,
                            'milk': req_milk,
                            'coffee_beans': req_coffee_beans,
                            'disposable_cups': req_disposable_cups}
        self.cost = cost


# compares remaining items in coffee machine with
# those required by the requested user and prints
# any ingredient deficit if present
def ingredient_checker(coffee_ingredients):
    global available_disposable_cups
    global available_water
    global available_coffee_beans
    global available_milk
    no_ingredient_counter = 0
    for key, value in coffee_ingredients.items():
        if key == 'water':
            if value > available_water:
                print('Sorry, not enough water!')
                no_ingredient_counter += 1
        elif key == 'milk':
            if value > available_milk:
                print('Sorry, not enough milk!')
                no_ingredient_counter += 1
        elif key == 'coffee_beans':
            if value > available_coffee_beans:
                print('Sorry, not enough coffee beans!')
                no_ingredient_counter += 1
        elif key == 'disposable_cups':
            if value > available_disposable_cups:
                print('Sorry, not enough disposable cups!')
                no_ingredient_counter += 1
    if no_ingredient_counter > 0:
        return False
    return True


# this is the while loop which contains code for
# taking input and performing actions of the coffee
# machine
while True:
    show_main_menu()
    action_selected = input('Enter number corresponding to action: ')
    if action_selected == '1':
        print('Choose type of coffee: \n',
              '1. Espresso\n',
              '2. Latte \n',
              '3. Cappuccino\n',
              '4. Back\n')
        coffee_menu_selected = input('Enter number corresponding to action: ')
        if coffee_menu_selected == '1':
            print('How many coffee cups should I make?')
            number_of_cups = int(input('cups: '))
            espresso = Coffee(250, 0, 16, number_of_cups, 4)
            # cup_calculator(espresso.ingredients)
            if not ingredient_checker(espresso.ingredients):
                continue
            processing()
            change_machine_status(-espresso.ingredients['water'],
                                  espresso.ingredients['milk'],
                                  -espresso.ingredients['coffee_beans'], 
                                  espresso.cost, 
                                  -number_of_cups)
        elif coffee_menu_selected == '2':
            print('How many coffee cups should I make?')
            number_of_cups = int(input('cups: '))
            latte = Coffee(350, 75, 20, number_of_cups, 7)
            # cup_calculator(latte.ingredients)
            if not ingredient_checker(latte.ingredients):
                continue
            processing()
            change_machine_status(-latte.ingredients['water'],
                                  -latte.ingredients['milk'],
                                  -latte.ingredients['coffee_beans'], 
                                  latte.cost, 
                                  -number_of_cups)
        elif coffee_menu_selected == '3':
            print('How many coffee cups should I make?')
            number_of_cups = int(input('cups: '))
            cappuccino = Coffee(200, 100, 12, number_of_cups, 6)
            # cup_calculator(cappuccino.ingredients)
            if not ingredient_checker(cappuccino.ingredients):
                continue
            processing()
            change_machine_status(-cappuccino.ingredients['water'],
                                  -cappuccino.ingredients['milk'],
                                  -cappuccino.ingredients['coffee_beans'],
                                  cappuccino.cost, 
                                  -number_of_cups)
        elif coffee_menu_selected == '4':
            continue
    elif action_selected == '2':
        water_added = int(input('Enter amount of water you want to add in ml: '))
        milk_added = int(input('Enter amount of milk you want to add in ml: '))
        coffee_beans_added = int(input('Enter amount of coffee beans you want to add in grams: '))
        disposable_cups_added = int(input('Enter amount of disposable cups you want to add: '))
        change_machine_status(water_added,
                              milk_added,
                              coffee_beans_added,
                              0,
                              disposable_cups_added)
    elif action_selected == '3':
        print('I will now give you ', available_money, '$')
        change_machine_status(0, 0, 0, -available_money, 0)
    elif action_selected == '4':
        show_machine_status()
    elif action_selected == '5':
        break
