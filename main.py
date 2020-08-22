class Zoo:
    eat = 0
    name = ""
    weight = 0

    def __init__(self, a_name="", a_weight=0):
        if a_name == "":
            print(f"{self} without name!")
        if a_weight == 0:
            print(f"{self} without weight!")
        self.name = a_name
        self.weight = a_weight

    def get_weight(self):
        return self.weight

    def feed(self):
        self.eat = self.eat + 1
        print(f"{self.name} was feed {str(self.eat)} times")

    def voice(self):
        pass


class Bird(Zoo):
    eggs = 0

    def voice(self):
        super().voice()

    def collect_eggs(self):
        self.eggs += 1
        if self.eggs == 1:
            print(f"{self.name} collects 1 egg")
        else:
            print(f"{self.name} collects {str(self.eggs)} eggs")


class Chicken(Bird):
    def voice(self):
        super().voice()
        print(f"{self.name} says cluck-cluck")


class Duck(Bird):
    def voice(self):
        super().voice()
        print(f"{self.name} says quack-quack")


class Goose(Bird):
    def voice(self):
        super().voice()
        print(f"{self.name} says honk-honk")


class Animal(Zoo):
    def voice(self):
        super().voice()


class Milk_Animal(Animal):
    milk_can = 0

    def milk(self):
        self.milk_can += 1
        print(f"{self.name} is milked {str(self.milk_can)} times")


class Wool_Animal(Animal):
    wool = 0

    def beard(self):
        self.wool += 1
        print(f"{self.name} is bearded {str(self.wool)} times")


class Sheep(Wool_Animal):
    def voice(self):
        super().voice()
        print(f"{self.name} says blaaah... blaaah")


class Cow(Milk_Animal):
    def voice(self):
        super().voice()
        print(f"{self.name} says moo... moo")


class Goat(Milk_Animal, Wool_Animal):
    def voice(self):
        super().voice()
        print(f"{self.name} says baaah... baaah")


def main():

    def chickens(name, weigth, countfeed, counteggs):
        v_chicken = Chicken(name, weigth)
        v_chicken.voice()
        for _ in range(countfeed):
            v_chicken.feed()
        for _ in range(counteggs):
            v_chicken.collect_eggs()
        return v_chicken

    def geese(name, weight, countfeed, counteggs):
        v_goose = Goose(name, weight)
        v_goose.voice()
        for _ in range(countfeed):
            v_goose.feed()
        for _ in range(counteggs):
            v_goose.collect_eggs()
        return v_goose

    def ducks(name, weight, countfeed, counteggs):
        v_duck = Duck(name, weight)
        v_duck.voice()
        for _ in range(countfeed):
            v_duck.feed()
        for _ in range(counteggs):
            v_duck.collect_eggs()
        return v_duck

    def sheeps(name, weight, countfeed, countbeards):
        v_sheep = Sheep(name, weight)
        v_sheep.voice()
        for _ in range(countfeed):
            v_sheep.feed()
        for _ in range(countbeards):
            v_sheep.beard()
        return v_sheep

    def cows(name, weight, countfeed, countmilk):
        v_cow = Cow(name, weight)
        v_cow.voice()
        for _ in range(countfeed):
            v_cow.feed()
        for _ in range(countmilk):
            v_cow.milk
        return v_cow

    def goats(name, weight, countfeed, countmilk, countbeards):
        v_goat = Goat(name, weight)
        v_goat.voice()
        for _ in range(countfeed):
            v_goat.feed()
        for _ in range(countmilk):
            v_goat.milk()
        for _ in range(countbeards):
            v_goat.beard()
        return v_goat

    # Task 2
    zooz = []
    zooz.append(geese("Белый", 8, 4, 1))
    zooz.append(geese("Серый", 9, 2, 1))
    zooz.append(cows("Манька", 134, 2, 3))

    zooz.append(sheeps("Барашек", 48, 2, 3))
    zooz.append(sheeps("Кудрявый", 54, 2, 3))

    zooz.append(chickens("Ко-Ко", 5, 3, 4))
    zooz.append(chickens("Кукареку", 4, 2, 1))

    zooz.append(goats("Рога", 75, 2, 3, 6))
    zooz.append(goats("Копыта", 65, 2, 3, 5))

    zooz.append(ducks("Кряква", 13, 3, 4))

    # Task 3
    print(f"Total wight is {sum(int(z.get_weight()) for z in zooz)}")

    max_weight_animal = zooz[1]
    for z in zooz:
        if z.weight > max_weight_animal.weight:
           max_weight_animal = z
    print(f"The name of max weight animal is {max_weight_animal.name}. Max weight is {str(max_weight_animal.weight)}.")      



    # #print(sum([cl.weight for cl in Animal]))

    # print(type(chicken1).mro())
main()
