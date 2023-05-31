# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

def is_ticket_happy(number_of_ticket):
    first_summ = 0
    second_summ = 0
    while(number_of_ticket / 1000 > 1):
        first_summ += number_of_ticket % 10
        number_of_ticket = number_of_ticket // 10
    while(number_of_ticket != 0):
        second_summ += number_of_ticket % 10
        number_of_ticket = number_of_ticket // 10
    if(first_summ == second_summ):
        print('Yes')
    else:
        print('No')


is_ticket_happy(456451)