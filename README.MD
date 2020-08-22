# Hometask for "Classes and it's using in Python"


** In the above solution, an adjustment was made to the task for multinheritance: a goat can not only be milked, but also breaded. **

Initial data, animals:
 
```python
    #name weigth countfeeds counteggs/countmilk/countbread
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
```

logs
```
Белый says honk-honk
Белый was feed 1 times
Белый was feed 2 times
Белый was feed 3 times
Белый was feed 4 times
Белый collects 1 egg
Серый says honk-honk
Серый was feed 1 times
Серый was feed 2 times
Серый collects 1 egg
Манька says moo... moo
Манька was feed 1 times
Манька was feed 2 times
Барашек says blaaah... blaaah
Барашек was feed 1 times
Барашек was feed 2 times
Барашек is bearded 1 times
Барашек is bearded 2 times
Барашек is bearded 3 times
Кудрявый says blaaah... blaaah
Кудрявый was feed 1 times
Кудрявый was feed 2 times
Кудрявый is bearded 1 times
Кудрявый is bearded 2 times
Кудрявый is bearded 3 times
Ко-Ко says cluck-cluck
Ко-Ко was feed 1 times
Ко-Ко was feed 2 times
Ко-Ко was feed 3 times
Ко-Ко collects 1 egg
Ко-Ко collects 2 eggs
Ко-Ко collects 3 eggs
Ко-Ко collects 4 eggs
Кукареку says cluck-cluck
Кукареку was feed 1 times
Кукареку was feed 2 times
Кукареку collects 1 egg
Рога says baaah... baaah
Рога was feed 1 times
Рога was feed 2 times
Рога is milked 1 times
Рога is milked 2 times
Рога is milked 3 times
Рога is bearded 1 times
Рога is bearded 2 times
Рога is bearded 3 times
Рога is bearded 4 times
Рога is bearded 5 times
Рога is bearded 6 times
Копыта says baaah... baaah
Копыта was feed 1 times
Копыта was feed 2 times
Копыта is milked 1 times
Копыта is milked 2 times
Копыта is milked 3 times
Копыта is bearded 1 times
Копыта is bearded 2 times
Копыта is bearded 3 times
Копыта is bearded 4 times
Копыта is bearded 5 times
Кряква says quack-quack
Кряква was feed 1 times
Кряква was feed 2 times
Кряква was feed 3 times
Кряква collects 1 egg
Кряква collects 2 eggs
Кряква collects 3 eggs
Кряква collects 4 eggs
Total wight is 415
The name of max weight animal is Манька. Max weight is 134.

```