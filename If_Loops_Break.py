"""IF STATEMENT"""
x = 10

if x > 5:
    print('X is greater than 5')

"""IF ELIF ELSE STATEMENT"""

grade = 85

if grade >= 90:
    print("A")

elif grade >= 80:
    print("B")

else:
    print("C")

"""FOR LOOP"""

fruits = ['apples', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

"""WHILE LOOP"""

count = 0

while count < 5:
    print(count)
    count += 1

"""BREAK AND CONTINUE STATEMENTS"""

"""break statement example"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_total = 0

for num in numbers:

    num_total += num

    if num == 5:
        break
    print(num, num_total)

"""continue statement example"""

fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

for fruit in fruits:
    if fruit == "cherry":

        """Selectively bypasses an item"""
        continue
    print(fruit)

 






