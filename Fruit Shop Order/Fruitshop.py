def greet(name):
    print(f'Welcome {name}!')

name=input('Enter your name: ').upper()
greet(name)

try:
    n=int(input('\nNumber of types of fruits you wish to buy: '))
except ValueError or NameError:
    print('Invalid Value!!')

fruits=[]
numbers=[]
for i in range(n):
    fruit=input(f'Enter fruit {i+1}: ')
    fruits.append(fruit)
    number = input(f'Enter quantity {i + 1}: ')
    numbers.append(number)

for numbers,fruits in zip(numbers,fruits):
    print(f" Fruit: {fruits} / Quantity: {numbers}")

confirmation = input('\nConfirm order List? (y/n): ')

if confirmation.upper() == 'Y':
    print('Order Confirmed!\n')
else:
    print('Edit List')
print('Visit Again!!')