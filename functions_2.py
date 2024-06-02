import datetime

one = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
two = (2, 5, 8, 11, 14, 17, 20, 23, 26, 29)
three = (3, 6, 9, 12, 15, 18, 21, 24, 27, 30)

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
after_tomorrow = today + datetime.timedelta(days=2)

if today.strftime('%w') == '1':
    day_of_week_today = f"Пн, {today.strftime('%d.%m')}"
elif today.strftime('%w') == '2':
    day_of_week_today = f"Вт, {today.strftime('%d.%m')}"
elif today.strftime('%w') == '3':
    day_of_week_today = f"Ср, {today.strftime('%d.%m')}"
elif today.strftime('%w') == '4':
    day_of_week_today = f"Чт, {today.strftime('%d.%m')}"
elif today.strftime('%w') == '5':
    day_of_week_today = f"Пт, {today.strftime('%d.%m')}"
elif today.strftime('%w') == '6':
    day_of_week_today = f"Сб, {today.strftime('%d.%m')}"
elif today.strftime('%w') == '0':
    day_of_week_today = f"Нд, {today.strftime('%d.%m')}"

if tomorrow.strftime('%w') == '1':
    day_of_week_tomorrow = f"Пн, {tomorrow.strftime('%d.%m')}"
elif tomorrow.strftime('%w') == '2':
    day_of_week_tomorrow = f"Вт, {tomorrow.strftime('%d.%m')}"
elif tomorrow.strftime('%w') == '3':
    day_of_week_tomorrow = f"Ср, {tomorrow.strftime('%d.%m')}"
elif tomorrow.strftime('%w') == '4':
    day_of_week_tomorrow = f"Чт, {tomorrow.strftime('%d.%m')}"
elif tomorrow.strftime('%w') == '5':
    day_of_week_tomorrow = f"Пт, {tomorrow.strftime('%d.%m')}"
elif tomorrow.strftime('%w') == '6':
    day_of_week_tomorrow = f"Сб, {tomorrow.strftime('%d.%m')}"
elif tomorrow.strftime('%w') == '0':
    day_of_week_tomorrow = f"Нд, {tomorrow.strftime('%d.%m')}"

if after_tomorrow.strftime('%w') == '1':
    day_of_week_after_tomorrow = f"Пн, {after_tomorrow.strftime('%d.%m')}"
elif after_tomorrow.strftime('%w') == '2':
    day_of_week_after_tomorrow = f"Вт, {after_tomorrow.strftime('%d.%m')}"
elif after_tomorrow.strftime('%w') == '3':
    day_of_week_after_tomorrow = f"Ср, {after_tomorrow.strftime('%d.%m')}"
elif after_tomorrow.strftime('%w') == '4':
    day_of_week_after_tomorrow = f"Чт, {after_tomorrow.strftime('%d.%m')}"
elif after_tomorrow.strftime('%w') == '5':
    day_of_week_after_tomorrow = f"Пт, {after_tomorrow.strftime('%d.%m')}"
elif after_tomorrow.strftime('%w') == '6':
    day_of_week_after_tomorrow = f"Сб, {after_tomorrow.strftime('%d.%m')}"
elif after_tomorrow.strftime('%w') == '0':
    day_of_week_after_tomorrow = f"Нд, {after_tomorrow.strftime('%d.%m')}"

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

if tomorrow.day in one:
    day_tomorrow_one = 'one_1'
    day_tomorrow_two = 'one_2'
    day_tomorrow_three = 'one_3'
    day_tomorrow_four = 'one_4'
    day_tomorrow_five = 'one_5'
    day_tomorrow_six = 'one_6'
if tomorrow.day in two:
    day_tomorrow_one = 'two_1'
    day_tomorrow_two = 'two_2'
    day_tomorrow_three = 'two_3'
    day_tomorrow_four = 'two_4'
    day_tomorrow_five = 'two_5'
    day_tomorrow_six = 'two_6'
if tomorrow.day in three:
    day_tomorrow_one = 'three_1'
    day_tomorrow_two = 'three_2'
    day_tomorrow_three = 'three_3'
    day_tomorrow_four = 'three_4'
    day_tomorrow_five = 'three_5'
    day_tomorrow_six = 'three_6'

if after_tomorrow.day in one:
    day_after_tomorrow_one = 'one_1'
    day_after_tomorrow_two = 'one_2'
    day_after_tomorrow_three = 'one_3'
    day_after_tomorrow_four = 'one_4'
    day_after_tomorrow_five = 'one_5'
    day_after_tomorrow_six = 'one_6'
if after_tomorrow.day in two:
    day_after_tomorrow_one = 'two_1'
    day_after_tomorrow_two = 'two_2'
    day_after_tomorrow_three = 'two_3'
    day_after_tomorrow_four = 'two_4'
    day_after_tomorrow_five = 'two_5'
    day_after_tomorrow_six = 'two_6'
if after_tomorrow.day in three:
    day_after_tomorrow_one = 'three_1'
    day_after_tomorrow_two = 'three_2'
    day_after_tomorrow_three = 'three_3'
    day_after_tomorrow_four = 'three_4'
    day_after_tomorrow_five = 'three_5'
    day_after_tomorrow_six = 'three_6'

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
