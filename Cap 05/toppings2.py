availabel_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in availabel_toppings:
            print("Adding " + requested_topping + ".")
        else:
            print("Sorry, we don't have " + requested_topping + ".")

    print("\nFinished making your pizza!")
else:
    print("Are you sure want a plain pizza?")

