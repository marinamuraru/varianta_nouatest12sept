# Write a function for each subtask
# Task 1.
# Write a Python program to create a list containing the following
# numbers: 10, 20, 30, 40, 50.
#               sub-task1: Print the list.
# from os import remove
# from tkinter.font import names
# from unittest.mock import numerics


def sub_task1():
    list1 = "10", "20", "30", "40", "50"
    print(list1)

# Task 2.
# Given the list
#       numbers = [10, 20, 30, 40, 50],
#
#       write a Python program to:
#       sub-task2: Print the first element of the list.
def sub_task2():
    numbers = [10, 20, 30, 40, 50]
    print(numbers[0])
#       sub-task3: empty function
def sub_task3():
    pass

#       sub-task4: Print the third element of the list.
def sub_task4():
    numbers = [10, 20, 30, 40, 50]
    print(numbers[2:3])
#       sub-task5: Change the second element of the list to 25 and print the updated list.
def sub_task5():
    numbers = [10, 20, 30, 40, 50]
    numbers[1] = 25
    print(numbers)

#       sub-task6: Insert the number 15 at the second position in the list
def sub_task6():
    numbers = [10, 20, 30, 40, 50]
    numbers.insert(1, 15)
    print(numbers)
# Task 3.

# Given the list
#       matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],
#
#       write a Python program to:
#       sub-task7: Print the second element of the second list.
def sub_task7():
    matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    matrix2 = matrix[1][1]
    print(matrix2)


#       sub-task8: Print all the elements from the first, third and last list.
def sub_task8():
    matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    matrix2 = matrix[0][0:], matrix[2][0:], matrix[4][0:]
    print(matrix2)

# Task 4.
# Write a Python program to create a dictionary with the following key-value pairs
#       sub-task9: Print the dictionary
def sub_task9():
    any_dictionary = {
        "hair" : "dark_brown",
        "eyes" : "brown",
        "height" : "183"
    }
    print(any_dictionary)
# Given the following dictionary
#       person = {"name": "Alice", "age": 25, "city": "New York"},




#       write a Python program to:
#       sub-task9: Print the value associated with the key "name".
def sub_task99():
    person = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }
    print(person["name"])
#       sub-task10: Print the value associated with the key "age".
#       sub-task11: Print the value of the "city" key using the get() method.

# Task 5.
# Write a Python program that takes a list of fruits:
#       fruits = ["apple", "banana", "cherry", "apple", "banana", "apple"]

#       sub-task12: Create a dictionary that counts the number of occurrences of each fruit, resulting in:
#           {"apple": 3, "banana": 2, "cherry": 1}
# new

if __name__ == "__main__":
    # print("Welcome to the first test of the course!")
    sub_task1()
    sub_task2()
    sub_task3()
    sub_task4()
    sub_task5()
    sub_task6()
    sub_task7()
    sub_task8()
    sub_task9()
    sub_task99()