# Hometask for "Classes and it's using in Python"


** In the above solution, an adjustment was made to the task for multinheritance: a goat can not only be milked, but also breaded. **

Initial data, animals:
 
```python
    #name weigth countfeeds counteggs/countmilk/countbread
    zooz = []
    zooz.append(geese("�����", 8, 4, 1))
    zooz.append(geese("�����", 9, 2, 1))
    zooz.append(cows("������", 134, 2, 3))

    zooz.append(sheeps("�������", 48, 2, 3))
    zooz.append(sheeps("��������", 54, 2, 3))

    zooz.append(chickens("��-��", 5, 3, 4))
    zooz.append(chickens("��������", 4, 2, 1))

    zooz.append(goats("����", 75, 2, 3, 6))
    zooz.append(goats("������", 65, 2, 3, 5))

    zooz.append(ducks("������", 13, 3, 4))
```

logs
```
����� says honk-honk
����� was feed 1 times
����� was feed 2 times
����� was feed 3 times
����� was feed 4 times
����� collects 1 egg
����� says honk-honk
����� was feed 1 times
����� was feed 2 times
����� collects 1 egg
������ says moo... moo
������ was feed 1 times
������ was feed 2 times
������� says blaaah... blaaah
������� was feed 1 times
������� was feed 2 times
������� is bearded 1 times
������� is bearded 2 times
������� is bearded 3 times
�������� says blaaah... blaaah
�������� was feed 1 times
�������� was feed 2 times
�������� is bearded 1 times
�������� is bearded 2 times
�������� is bearded 3 times
��-�� says cluck-cluck
��-�� was feed 1 times
��-�� was feed 2 times
��-�� was feed 3 times
��-�� collects 1 egg
��-�� collects 2 eggs
��-�� collects 3 eggs
��-�� collects 4 eggs
�������� says cluck-cluck
�������� was feed 1 times
�������� was feed 2 times
�������� collects 1 egg
���� says baaah... baaah
���� was feed 1 times
���� was feed 2 times
���� is milked 1 times
���� is milked 2 times
���� is milked 3 times
���� is bearded 1 times
���� is bearded 2 times
���� is bearded 3 times
���� is bearded 4 times
���� is bearded 5 times
���� is bearded 6 times
������ says baaah... baaah
������ was feed 1 times
������ was feed 2 times
������ is milked 1 times
������ is milked 2 times
������ is milked 3 times
������ is bearded 1 times
������ is bearded 2 times
������ is bearded 3 times
������ is bearded 4 times
������ is bearded 5 times
������ says quack-quack
������ was feed 1 times
������ was feed 2 times
������ was feed 3 times
������ collects 1 egg
������ collects 2 eggs
������ collects 3 eggs
������ collects 4 eggs
Total wight is 415
The name of max weight animal is ������. Max weight is 134.

```