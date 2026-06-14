class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")


class ZooGarden:
    def __init__(self):
        self.animals = []

    def add_animal(self):
        name = input("Enter animal name: ")
        species = input("Enter species: ")
        age = int(input("Enter age: "))

        animal = Animal(name, species, age)
        self.animals.append(animal)

        print("Animal added successfully!")

    def view_animals(self):
        if len(self.animals) == 0:
            print("No animals in the zoo.")
            return

        for i, animal in enumerate(self.animals, start=1):
            print(f"\nAnimal #{i}")
            animal.display()

    def update_animal(self):
        if len(self.animals) == 0:
            print("No animals available.")
            return

        self.view_animals()

        index = int(input("Enter animal number to update: ")) - 1

        if 0 <= index < len(self.animals):
            self.animals[index].name = input("New name: ")
            self.animals[index].species = input("New species: ")
            self.animals[index].age = int(input("New age: "))

            print("Animal updated successfully!")
        else:
            print("Invalid number.")

    def remove_animal(self):
        if len(self.animals) == 0:
            print("No animals available.")
            return

        self.view_animals()

        index = int(input("Enter animal number to remove: ")) - 1

        if 0 <= index < len(self.animals):
            removed = self.animals.pop(index)
            print(f"{removed.name} removed successfully!")
        else:
            print("Invalid number.")

    def zoo_statistics(self):
        print("\n===== ZOO STATISTICS =====")
        print(f"Total Animals: {len(self.animals)}")


zoo = ZooGarden()

while True:
    print("\n========================")
    print("      ZOO GARDEN")
    print("========================")
    print("1. Add Animal")
    print("2. View Animals")
    print("3. Update Animal")
    print("4. Remove Animal")
    print("5. View Zoo Statistics")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        zoo.add_animal()

    elif choice == "2":
        zoo.view_animals()

    elif choice == "3":
        zoo.update_animal()

    elif choice == "4":
        zoo.remove_animal()

    elif choice == "5":
        zoo.zoo_statistics()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")