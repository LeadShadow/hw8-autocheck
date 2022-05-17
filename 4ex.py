from random import randrange


def get_numbers_ticket(min, max, quantity):
    list1 = []
    i = 0
    if min < 1 or max > 1000 or quantity not in range(min, max):
        return []
    while i < quantity:
        get_number = randrange(min, max)
        if get_number in list1:
            continue
        list1.append(get_number)
        i += 1
    list1.sort()
    print(len(list1))
    return list1


print(get_numbers_ticket(5, 30, 6))

        