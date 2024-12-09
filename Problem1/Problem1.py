import math

def natural_numbers_100():
    numbers = range(1000)
    for numbers in numbers:
        print(numbers)

natural_numbers_100()

numbers_0_999 = range(0,1000)

divisable_by_3_and_5 = [numbers for numbers in numbers_0_999 if numbers % 3 ==0 or numbers % 5 == 0]
print(divisable_by_3_and_5)
print(sum(divisable_by_3_and_5))