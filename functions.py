import datetime


one = [1, 7, 13, 19, 25, 31]
two = (2, 8, 14, 20, 26)
three = (3, 9, 15, 21, 27)
four = (4, 10, 16, 22, 28)
five = (5, 11, 17, 23, 29)
six = (6, 12, 18, 24, 30)

today = datetime.date.today()

if today.day in one:
    day_num = 'one'
if today.day in two:
    day_num = 'two'
if today.day in three:
    day_num = 'three'
if today.day in four:
    day_num = 'four'
if today.day in five:
    day_num = 'five'
if today.day in six:
    day_num = 'six'


def check_cherg(e):
    if e == 1:
        cherg = '1_cherg'
    if e == 2:
        cherg = '2_cherg'
    if e == 3:
        cherg = '3_cherg'
    if e == 4:
        cherg = '4_cherg'
    if e == 5:
        cherg = '5_cherg'
    if e == 6:
        cherg = '6_cherg'
    return cherg
