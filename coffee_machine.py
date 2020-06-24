# THIS PROJECT IS STILL UNDER DEVELOPMENT
# THE COMMENTED CODE WITHIN '...' CAN BE IGNORED

# ..................................................
# # takes user input on available amount of ingredients
# # (of course ideally a sensor that gives an input would
# # be better)
# print('How many ml of water are already present in me?')
# available_water = int(input('ml of water: '))
# print('How many ml of milk are already present in me?')
# available_milk = int(input('ml of milk :'))
# print('How many grams of coffee beans are already present in me?')
# available_coffee_beans = int(input('grams of coffee beans: '))
#
# # takes input on number of cups of coffee user wants
# print('How many coffee cups should I make?')
# number_of_cups = int(input('cups: '))
#
# # calculates and prints amount of ingredients needed for
# # number_of_cups entered by user
# water = 200 * number_of_cups
# milk = 50 * number_of_cups
# coffee_beans = 15 * number_of_cups
# print('\nFor', number_of_cups, 'cups of coffee please add to me the following:\n',
#       milk, 'ml of milk\n',
#       water, 'ml of water\n',
#       coffee_beans, 'g of coffee beans\n')
#
# # prints this while calculating next code blocks
# print('Processing...\n')
#
# # compares required ingredients with available ingredients
# # and prints ability to make or not make requested cups
# # of coffee (along with extra/maximum cups if possible)
# if water <= available_water and \
#         milk <= available_milk and \
#         coffee_beans <= available_coffee_beans:
#     # calculates number of extra coffee cups
#     # machine can make
#     extra_possible_cups = min((available_water // 200) - number_of_cups,
#                               (available_milk // 50) - number_of_cups,
#                               (available_coffee_beans // 15) - number_of_cups)
#     if extra_possible_cups > 0:
#         print('Yes, I can make this amount of coffee (and ',
#               extra_possible_cups,
#               ' cup(s) more too!\n')
#     else:
#         print('Yes, I can make this amount of coffee,'
#               ' this is the maximum amount of coffee I can make right now.\n')
# else:
#     # calculates maximum number of coffee cups
#     # machine can make
#     maximum_possible_cups = min((available_water // 200),
#                                 (available_milk // 50),
#                                 (available_coffee_beans // 15))
#     print('Sorry, but I can only make ',
#           maximum_possible_cups,
#           ' cup(s) right now :(\n')
#
# print('Initiating coffee engines')
# print('Disintegrating coffee beans')
# print('Boiling water')
# print('Formulating coffee solution')
# print('Pouring coffee in the cup')
# print('Finalising emulsion by adding milk')
# print('Enjoy! :)')
# ..................................................

# these variables are re-assigned solely for
# successful completion of a project and shall be
# set to default values later
available_money = 550
available_water = 400
available_milk = 540
available_coffee_beans = 120
available_disposable_cups = 9


# when called, shows remaining ingredients, cups, and
# money in the coffee machine
def show_status():
    print('Current Status:\n',
          available_water, 'ml of water\n',
          available_milk, 'ml of milk\n',
          available_coffee_beans, 'grams of coffee beans\n',
          available_disposable_cups, 'disposable cups\n',
          available_money, 'money\n')


# when called, shows list of possible options
# for the user to choose to make the coffee
# machine do something
def show_options():
    print('What would you like to do?\n',
          '1. buy\n',
          '2. fill\n',
          '3. take\n',
          '4. remaining\n',
          '5. exit\n')


# changes remaining items in coffee machine
# according to sign of arguments given e.g.
# -10 will reduce 10 from variable while 10
# would increase 10 in the variable
def change_status(req_water, req_milk, req_coffee_beans,
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


# compares remaining items in coffee machine with
# those required by the requested user and prints
# any ingredient deficit if present along with returning
# True which is used in other parts of the program
# THIS FUNCTION IS UNDER DEVELOPMENT
def compare_status(req_water, req_milk, req_coffee_beans,
                   req_cups):
    global available_disposable_cups
    global available_water
    global available_coffee_beans
    global available_milk
    if available_disposable_cups < req_cups:
        print('Sorry, not enough disposable cups!')
        return True
    elif available_water < req_water:
        print('Sorry, not enough water!')
        return True
    elif available_coffee_beans < req_coffee_beans:
        print('Sorry, not enough coffee beans!')
        return True
    elif available_milk < req_milk:
        print('Sorry, not enough milk!')
        return True
    else:
        return False


# this is the while loop which contains code for
# taking input and performing actions of the coffee
# machine
while True:
    show_options()
    action_selected = input('Enter number corresponding to action: ')
    if action_selected == '1':
        print('Choose type of coffee: \n',
              '1. Espresso\n',
              '2. Latte \n',
              '3. Cappuccino\n',
              '4. Back\n')
        coffee_selected = input('Enter number corresponding to coffee: ')
        if coffee_selected == '1':
            if compare_status(250, 0, 16, 1):
                continue
            print('I have enough resources, making you a coffee!')
            change_status(-250, 0, -16, 4, -1)
        elif coffee_selected == '2':
            if compare_status(350, 75, 20, 1):
                continue
            print('I have enough resources, making you a coffee!')
            change_status(-350, -75, -20, 7, -1)
        elif coffee_selected == '3':
            if compare_status(200, 100, 12, 1):
                continue
            print('I have enough resources, making you a coffee!')
            change_status(-200, -100, -12, 6, -1)
        elif coffee_selected == '4':
            continue
    elif action_selected == '2':
        water_added = int(input('Enter amount of water you want to add in ml: '))
        milk_added = int(input('Enter amount of milk you want to add in ml: '))
        coffee_beans_added = int(input('Enter amount of coffee beans you want to add in grams: '))
        disposable_cups_added = int(input('Enter amount of disposable cups you want to add: '))
        change_status(water_added,
                      milk_added,
                      coffee_beans_added,
                      0,
                      disposable_cups_added)
    elif action_selected == '3':
        print('I will now give you ', available_money, '$')
        change_status(0, 0, 0, -available_money, 0)
    elif action_selected == '4':
        show_status()
    elif action_selected == '5':
        break
