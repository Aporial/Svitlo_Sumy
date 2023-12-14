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

if today.day in one:
    day_num_one = 'one_1'
    day_num_two = 'one_2'
    day_num_three = 'one_3'
    day_num_four = 'one_4'
    day_num_five = 'one_5'
    day_num_six = 'one_6'
if today.day in two:
    day_num_one = 'two_1'
    day_num_two = 'two_2'
    day_num_three = 'two_3'
    day_num_four = 'two_4'
    day_num_five = 'two_5'
    day_num_six = 'two_6'
if today.day in three:
    day_num_one = 'three_1'
    day_num_two = 'three_2'
    day_num_three = 'three_3'
    day_num_four = 'three_4'
    day_num_five = 'three_5'
    day_num_six = 'three_6'
if today.day in four:
    day_num_one = 'four_1'
    day_num_two = 'four_2'
    day_num_three = 'four_3'
    day_num_four = 'four_4'
    day_num_five = 'four_5'
    day_num_six = 'four_6'
if today.day in five:
    day_num_one = 'five_1'
    day_num_two = 'five_2'
    day_num_three = 'five_3'
    day_num_four = 'five_4'
    day_num_five = 'five_5'
    day_num_six = 'five_6'
if today.day in six:
    day_num_one = 'six'
    day_num_two = 'six_2'
    day_num_three = 'six_3'
    day_num_four = 'six_4'
    day_num_five = 'six_5'
    day_num_six = 'six_6'


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
