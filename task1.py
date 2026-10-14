def third_largest(numbers):
    if len(numbers) < 3:
        return -1

    first = -1000
    second = -1000
    third = -1000

    for number in numbers:
        if number > first:
            third = second
            second = first
            first = number
        elif number > second:
            third = second
            second = number
        elif number > third:
            third = number

    return third


text = input("Введіть числа через пробіл: ")
numbers = []
for part in text.split():
    numbers.append(int(part))

print(third_largest(numbers))

