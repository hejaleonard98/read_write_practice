from zoo.zoo import show_animals,add_animal

def main():
    while True:
        print("")
        print("ZOO")
        print("")
        print("1. Show animals")
        print("2. Add animal")
        print("3. Exit")
        print("")
        choice = input("Choose: ").strip()

        if not choice.isdigit():
            print("Please enter a number!")
            continue

        match choice:
            case "1": show_animals()
            case "2": add_animal()
            case "3": break


if __name__ == "__main__":
    main()
