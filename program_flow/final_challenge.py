options = [1, 2, 3, 4, 5, 6, 0]
answers = "\n 1. tacos \n 2. hamburger \n 3. hot-dog \n 4. salad \n 5. " \
          "protein-shake \n 6. spaghetti \n 0. exit"

print("What would you like to eat today? ")
print(answers)

print("")
answer = 7

while answer not in range(len(options)):
    answer = int(input("Please pick one of the options: "))

    if answer == 0:
        exit()

    if answer in options:
        break

    else:
        continue

while answer in range(len(options)):
    print("You picked #{}".format(answer))
    yes_or_no = input("Would you like the ingredients? (y/n): ")

    if yes_or_no == "y":

        if answer == 1:
            print("Here are your ingredients: "
                  "\n1. hard-shell taco"
                  "\n2. lettuce"
                  "\n3. grounded beef"
                  "\n4. tomatoes"
                  "\n5. string cheese"
                  "\n6. sour-cream")
            break

        if answer == 2:
            print("Here are your ingredients: "
                  "\n1. 2 burger buns"
                  "\n2. a beef patty"
                  "\n3. lettuce"
                  "\n4. cheese"
                  "\n5. pickles"
                  "\n6. ketchup")
            break

        if answer == 3:
            print("Here are your ingredients: "
                  "\n1. hot-dog bun"
                  "\n2. beef sausage"
                  "\n3. ketchup"
                  "\n4. mayonnaise")
            break

        if answer == 4:
            print("Here are your ingredients: "
                  "\n1. tomatoes"
                  "\n2. cucumbers"
                  "\n3. avocado"
                  "\n4. lettuce"
                  "\n5. ranch dressing")
            break

        if answer == 5:
            print("Here are your ingredients: "
                  "\n1. ice"
                  "\n2. milk"
                  "\n3. protein powder"
                  "\n5. oats"
                  "\n6. peanut butter"
                  "\n7. honey"
                  "\n8. banana"
                  "\n9. blueberries")
            break

        if answer == 6:
            print("Here are your ingredients: "
                  "\n1. spaghetti noodles"
                  "\n2. tomato sauce")
            break

        else:
            continue

    if yes_or_no == "n":
        print("Enjoy your meal")
        break

    else:
        continue
