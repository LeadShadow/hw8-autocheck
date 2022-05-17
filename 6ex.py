from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    sum1 = 0
    for i in number_list:
        sum1 += Decimal(i)
    average = sum1 / len(number_list)
    return average


print(decimal_average([4.5788689699797, 34.7576578697964, 86.8877666656633, 12], 6))