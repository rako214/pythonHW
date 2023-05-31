def summ_of_number(num, summ):
    while num != 0:
        summ += num % 10
        num = num // 10
    return summ

input = 131
summ_of_digits = summ_of_number(input, 0)
print(summ_of_digits)
