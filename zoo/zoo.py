def show_animals():
    with open("data/animals.txt", "r", encoding="utf-8") as notes:
        for line in notes:
            print(line.strip())

def add_animal():
    animal = input("New animal: ")
    with open("data/animals.txt", "a", encoding="utf-8") as file:
        file.write(f"{animal}\n")
