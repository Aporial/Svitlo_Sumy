from functions import today, tomorrow, after_tomorrow

one = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
two = (2, 5, 8, 11, 14, 17, 20, 23, 26, 29)
three = (3, 6, 9, 12, 15, 18, 21, 24, 27, 30)

if today.day in one:
    db2_day_num_one = 'one_1'
    db2_day_num_two = 'one_2'
    db2_day_num_three = 'one_3'
    db2_day_num_four = 'one_4'
    db2_day_num_five = 'one_5'
    db2_day_num_six = 'one_6'
if today.day in two:
    db2_day_num_one = 'two_1'
    db2_day_num_two = 'two_2'
    db2_day_num_three = 'two_3'
    db2_day_num_four = 'two_4'
    db2_day_num_five = 'two_5'
    db2_day_num_six = 'two_6'
if today.day in three:
    db2_day_num_one = 'three_1'
    db2_day_num_two = 'three_2'
    db2_day_num_three = 'three_3'
    db2_day_num_four = 'three_4'
    db2_day_num_five = 'three_5'
    db2_day_num_six = 'three_6'

if tomorrow.day in one:
    db2_day_tomorrow_one = 'one_1'
    db2_day_tomorrow_two = 'one_2'
    db2_day_tomorrow_three = 'one_3'
    db2_day_tomorrow_four = 'one_4'
    db2_day_tomorrow_five = 'one_5'
    db2_day_tomorrow_six = 'one_6'
if tomorrow.day in two:
    db2_day_tomorrow_one = 'two_1'
    db2_day_tomorrow_two = 'two_2'
    db2_day_tomorrow_three = 'two_3'
    db2_day_tomorrow_four = 'two_4'
    db2_day_tomorrow_five = 'two_5'
    db2_day_tomorrow_six = 'two_6'
if tomorrow.day in three:
    db2_day_tomorrow_one = 'three_1'
    db2_day_tomorrow_two = 'three_2'
    db2_day_tomorrow_three = 'three_3'
    db2_day_tomorrow_four = 'three_4'
    db2_day_tomorrow_five = 'three_5'
    db2_day_tomorrow_six = 'three_6'

if after_tomorrow.day in one:
    db2_day_after_tomorrow_one = 'one_1'
    db2_day_after_tomorrow_two = 'one_2'
    db2_day_after_tomorrow_three = 'one_3'
    db2_day_after_tomorrow_four = 'one_4'
    db2_day_after_tomorrow_five = 'one_5'
    db2_day_after_tomorrow_six = 'one_6'
if after_tomorrow.day in two:
    db2_day_after_tomorrow_one = 'two_1'
    db2_day_after_tomorrow_two = 'two_2'
    db2_day_after_tomorrow_three = 'two_3'
    db2_day_after_tomorrow_four = 'two_4'
    db2_day_after_tomorrow_five = 'two_5'
    db2_day_after_tomorrow_six = 'two_6'
if after_tomorrow.day in three:
    db2_day_after_tomorrow_one = 'three_1'
    db2_day_after_tomorrow_two = 'three_2'
    db2_day_after_tomorrow_three = 'three_3'
    db2_day_after_tomorrow_four = 'three_4'
    db2_day_after_tomorrow_five = 'three_5'
    db2_day_after_tomorrow_six = 'three_6'
