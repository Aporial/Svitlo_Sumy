import datetime

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
after_tomorrow = today + datetime.timedelta(days=2)

seven_days = today + datetime.timedelta(days=7)

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
