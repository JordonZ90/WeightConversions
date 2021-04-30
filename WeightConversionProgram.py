import weight


def display_menu():
    print("MENU")
    print("1. Pounds to Stone")
    print("2. Stone to Pounds")
    print("3. Pounds to Kilograms")
    print("4. Kilograms to Pounds")
    print("5. Kilograms to Stone")
    print("6. Stone to Kilograms")
    print("7. Ounces to Grams")
    print("8. Grams to Ounces")
    print()


def convert_weight():
    option = int(input("Enter a menu option"))
    if option == 1:
        pounds = float(input("Enter weight in Pounds "))
        stone = weight.pounds_to_stone(pounds)
        stone = round(stone, 2)
        print(f"Weight in {stone} stone")
    elif option == 2:
        stone = float(input("Enter weight in Stone "))
        pounds = weight.stone_to_pounds(stone)
        pounds = round(pounds, 2)
        print(f"Weight in {pounds} pounds")
    elif option == 3:
        pounds = float(input("Enter weight in Pounds "))
        kilograms = weight.pounds_to_kilograms(pounds)
        kilograms = round(kilograms, 2)
        print(f"Weight in {kilograms} Kilograms")
    elif option == 4:
        kilograms = float(input("Enter weight in Kilograms "))
        pounds = weight.kilograms_to_pounds(kilograms)
        pounds = round(pounds, 2)
        print(f"Weight in {pounds} Pounds")
    elif option == 5:
        kilograms = float(input("Enter weight in kilograms "))
        stone = weight.kilograms_to_stone(kilograms)
        stone = round(stone, 2)
        print(f"Weight in {stone} stone")
    elif option == 6:
        stone = float(input("Enter weight in Stone "))
        kilograms = weight.stone_to_kilograms(stone)
        kilograms = round(kilograms, 2)
        print(f"Weight in {kilograms} Kilograms")
    elif option == 7:
        ounces = float(input("Enter weight in Ounces "))
        grams = weight.ounces_to_grams(ounces)
        grams = round(grams, 2)
        print(f"Weight in {grams} Grams")
    elif option == 8:
        grams = float(input("Enter weight in Grams "))
        ounces = weight.grams_to_ounces(grams)
        ounces = round(ounces, 2)
        print(f"Weight in {ounces} Ounces")
    else:
        print("You must enter a valid menu number ")


def main():
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert_weight()
        print()
        again = input("Convert another measurement? (y|n) ")
        if again == "y".lower():
            display_menu()
        else:
            print()
    print("Goodbye!")


if __name__ == "__main__":
    main()