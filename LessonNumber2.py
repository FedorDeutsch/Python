# https://metanit.com/python/tutorial/2.14.php
# Урок 2 - Консольный ввод и вывод

print("Hello, Fedor !") # Стандартный вывод строки
print("Hello, World ! ", end =" ") # Теперь след строка будет выводиться через пробел
print("Hallo, Welt !\n") # По факту end - это тоже самое, что и \n

age = int(input("Enter your age: ")) # После выполнения кода выше, пользователь сможет ввести данные в age
name = input("Enter your name: ")
print("Name: ", name,", " "Age:", age) # Номер 1
print(f"Имя: {name}, Лет: {age}") # Номер 2
