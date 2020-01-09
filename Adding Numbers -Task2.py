def adding_up(c):
    value = 0
    for num in range(c + 1):
        value += num
    return value


print(adding_up(4))
print(adding_up(13))
print(adding_up(600))

# using range, print every third letter from the letters list, starting with the second letter in the list.
my_list = ['a', 'h', 'b', 'c', 'e', 'd', 'e', 'l', 'f', 'g', 'l', 'm', 'n', 'o', 'p']


def letters(letter_list):
    for index in range(1, len(letter_list), 3):
        print(letter_list[index])


letters(my_list)
