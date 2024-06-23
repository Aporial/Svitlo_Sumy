from flet import *
from for_telegram.chergs import *
from for_telegram.day import today
from for_telegram.database_1 import db1_day_num_one, db1_day_num_two, db1_day_num_three, db1_day_num_four, db1_day_num_five, db1_day_num_six
from for_telegram.database_2 import db2_day_num_one, db2_day_num_two, db2_day_num_three, db2_day_num_four, db2_day_num_five, db2_day_num_six
from firebase import firebase
from datetime import datetime


def main(page: Page):

    database_connection = firebase.FirebaseApplication(
        'https://svitlo-sumy-default-rtdb.europe-west1.firebasedatabase.app/', authentication=None)
    main_database = database_connection.get("/", None)
    database = main_database.get("database")
    print('DATABASE:', database)
    page.client_storage.set("database_storage", database)
    page.client_storage.set("main_database", main_database)

    day = datetime.now().strftime(f"{today}.%m.%Y")

    def one_cherg():
        if page.client_storage.get("database_storage") == 1:
            day_num_one = db1_day_num_one
            day_num_two = db1_day_num_two
            day_num_three = db1_day_num_three
            day_num_four = db1_day_num_four
            day_num_five = db1_day_num_five
            day_num_six = db1_day_num_six
        if page.client_storage.get("database_storage") == 2:
            day_num_one = db2_day_num_one
            day_num_two = db2_day_num_two
            day_num_three = db2_day_num_three
            day_num_four = db2_day_num_four
            day_num_five = db2_day_num_five
            day_num_six = db2_day_num_six

        result_one = main_database.get("1_cherg").get(f"{day_num_one}")
        try:
            if result_one == None:
                one_cherg_1.visible = False
                print("one_cherg_1 not found!")
            else:
                start_time, end_time = result_one.split('-')
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = result_one
                one_cherg_1.visible = True
                one_cherg_1.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            one,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("one_cherg_1 found!")
        except:
            one_cherg_1.visible = True
            one_cherg_1.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_one,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_two = main_database.get("1_cherg").get(f"{day_num_two}")
        try:
            if result_two == None:
                one_cherg_2.visible = False
                print("one_cherg_2 not found!")
            else:
                start_time, end_time = result_two.split('-')
                if end_time == '23:59':
                    two = f'{start_time}-24:00'
                else:
                    two = result_two
                one_cherg_2.visible = True
                one_cherg_2.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            two,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("one_cherg_2 found!")
        except:
            one_cherg_2.visible = True
            one_cherg_2.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_two,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_three = main_database.get("1_cherg").get(f"{day_num_three}")
        try:
            if result_three == None:
                one_cherg_3.visible = False
                print("one_cherg_3 not found!")
            else:
                start_time, end_time = result_three.split('-')
                if end_time == '23:59':
                    three = f'{start_time}-24:00'
                else:
                    three = result_three
                one_cherg_3.visible = True
                one_cherg_3.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            three,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("one_cherg_3 found!")
        except:
            one_cherg_3.visible = True
            one_cherg_3.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_three,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_four = main_database.get("1_cherg").get(f"{day_num_four}")
        try:
            if result_four == None:
                one_cherg_4.visible = False
                print("one_cherg_4 not found!")
            else:
                start_time, end_time = result_four.split('-')
                if end_time == '23:59':
                    four = f'{start_time}-24:00'
                else:
                    four = result_four
                one_cherg_4.visible = True
                one_cherg_4.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            four,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("one_cherg_4 found!")
        except:
            one_cherg_4.visible = True
            one_cherg_4.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_four,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_five = main_database.get("1_cherg").get(f"{day_num_five}")
        try:
            if result_five == None:
                one_cherg_5.visible = False
                print("one_cherg_5 not found!")
            else:
                start_time, end_time = result_five.split('-')
                if end_time == '23:59':
                    five = f'{start_time}-24:00'
                else:
                    five = result_five
                one_cherg_5.visible = True
                one_cherg_5.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            five,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("one_cherg_5 found!")
        except:
            one_cherg_5.visible = True
            one_cherg_5.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_five,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_six = main_database.get("1_cherg").get(f"{day_num_six}")
        try:
            if result_six == None:
                one_cherg_6.visible = False
                print("one_cherg_6 not found!")
            else:
                start_time, end_time = result_six.split('-')
                if end_time == '23:59':
                    six = f'{start_time}-24:00'
                else:
                    six = result_six
                one_cherg_6.visible = True
                one_cherg_6.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            six,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("one_cherg_6 found!")
        except:
            one_cherg_6.visible = True
            one_cherg_6.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_six,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

    def two_cherg():
        if page.client_storage.get("database_storage") == 1:
            day_num_one = db1_day_num_one
            day_num_two = db1_day_num_two
            day_num_three = db1_day_num_three
            day_num_four = db1_day_num_four
            day_num_five = db1_day_num_five
            day_num_six = db1_day_num_six
        if page.client_storage.get("database_storage") == 2:
            day_num_one = db2_day_num_one
            day_num_two = db2_day_num_two
            day_num_three = db2_day_num_three
            day_num_four = db2_day_num_four
            day_num_five = db2_day_num_five
            day_num_six = db2_day_num_six

        result_one = main_database.get("2_cherg").get(f"{day_num_one}")
        try:
            if result_one == None:
                two_cherg_1.visible = False
                print("two_cherg_1 not found!")
            else:
                start_time, end_time = result_one.split('-')
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = result_one
                two_cherg_1.visible = True
                two_cherg_1.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            one,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("two_cherg_1 found!")
        except:
            two_cherg_1.visible = True
            two_cherg_1.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_one,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_two = main_database.get("2_cherg").get(f"{day_num_two}")
        try:
            if result_two == None:
                two_cherg_2.visible = False
                print("two_cherg_2 not found!")
            else:
                start_time, end_time = result_two.split('-')
                if end_time == '23:59':
                    two = f'{start_time}-24:00'
                else:
                    two = result_two
                two_cherg_2.visible = True
                two_cherg_2.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            two,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("two_cherg_2 found!")
        except:
            two_cherg_2.visible = True
            two_cherg_2.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_two,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_three = main_database.get("2_cherg").get(f"{day_num_three}")
        try:
            if result_three == None:
                two_cherg_3.visible = False
                print("two_cherg_3 not found!")
            else:
                start_time, end_time = result_three.split('-')
                if end_time == '23:59':
                    three = f'{start_time}-24:00'
                else:
                    three = result_three
                two_cherg_3.visible = True
                two_cherg_3.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            three,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("two_cherg_3 found!")
        except:
            two_cherg_3.visible = True
            two_cherg_3.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_three,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_four = main_database.get("2_cherg").get(f"{day_num_four}")
        try:
            if result_four == None:
                two_cherg_4.visible = False
                print("two_cherg_4 not found!")
            else:
                start_time, end_time = result_four.split('-')
                if end_time == '23:59':
                    four = f'{start_time}-24:00'
                else:
                    four = result_four
                two_cherg_4.visible = True
                two_cherg_4.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            four,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("two_cherg_4 found!")
        except:
            two_cherg_4.visible = True
            two_cherg_4.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_four,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_five = main_database.get("2_cherg").get(f"{day_num_five}")
        try:
            if result_five == None:
                two_cherg_5.visible = False
                print("two_cherg_5 not found!")
            else:
                start_time, end_time = result_five.split('-')
                if end_time == '23:59':
                    five = f'{start_time}-24:00'
                else:
                    five = result_five
                two_cherg_5.visible = True
                two_cherg_5.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            five,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("two_cherg_5 found!")
        except:
            two_cherg_5.visible = True
            two_cherg_5.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_five,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_six = main_database.get("2_cherg").get(f"{day_num_six}")
        try:
            if result_six == None:
                two_cherg_6.visible = False
                print("two_cherg_6 not found!")
            else:
                start_time, end_time = result_six.split('-')
                if end_time == '23:59':
                    six = f'{start_time}-24:00'
                else:
                    six = result_six
                two_cherg_6.visible = True
                two_cherg_6.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            six,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("two_cherg_6 found!")
        except:
            two_cherg_6.visible = True
            two_cherg_6.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_six,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

    def three_cherg():
        if page.client_storage.get("database_storage") == 1:
            day_num_one = db1_day_num_one
            day_num_two = db1_day_num_two
            day_num_three = db1_day_num_three
            day_num_four = db1_day_num_four
            day_num_five = db1_day_num_five
            day_num_six = db1_day_num_six
        if page.client_storage.get("database_storage") == 2:
            day_num_one = db2_day_num_one
            day_num_two = db2_day_num_two
            day_num_three = db2_day_num_three
            day_num_four = db2_day_num_four
            day_num_five = db2_day_num_five
            day_num_six = db2_day_num_six

        result_one = main_database.get("3_cherg").get(f"{day_num_one}")
        try:
            if result_one == None:
                three_cherg_1.visible = False
                print("three_cherg_1 not found!")
            else:
                start_time, end_time = result_one.split('-')
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = result_one
                three_cherg_1.visible = True
                three_cherg_1.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            one,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("three_cherg_1 found!")
        except:
            three_cherg_1.visible = True
            three_cherg_1.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_one,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_two = main_database.get("3_cherg").get(f"{day_num_two}")
        try:
            if result_two == None:
                three_cherg_2.visible = False
                print("three_cherg_2 not found!")
            else:
                start_time, end_time = result_two.split('-')
                if end_time == '23:59':
                    two = f'{start_time}-24:00'
                else:
                    two = result_two
                three_cherg_2.visible = True
                three_cherg_2.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            two,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("three_cherg_2 found!")
        except:
            three_cherg_2.visible = True
            three_cherg_2.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_two,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_three = main_database.get("3_cherg").get(f"{day_num_three}")
        try:
            if result_three == None:
                three_cherg_3.visible = False
                print("three_cherg_3 not found!")
            else:
                start_time, end_time = result_three.split('-')
                if end_time == '23:59':
                    three = f'{start_time}-24:00'
                else:
                    three = result_three
                three_cherg_3.visible = True
                three_cherg_3.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            three,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("three_cherg_3 found!")
        except:
            three_cherg_3.visible = True
            three_cherg_3.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_three,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_four = main_database.get("3_cherg").get(f"{day_num_four}")
        try:
            if result_four == None:
                three_cherg_4.visible = False
                print("three_cherg_4 not found!")
            else:
                start_time, end_time = result_four.split('-')
                if end_time == '23:59':
                    four = f'{start_time}-24:00'
                else:
                    four = result_four
                three_cherg_4.visible = True
                three_cherg_4.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            four,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("three_cherg_4 found!")
        except:
            three_cherg_4.visible = True
            three_cherg_4.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_four,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_five = main_database.get("3_cherg").get(f"{day_num_five}")
        try:
            if result_five == None:
                three_cherg_5.visible = False
                print("three_cherg_5 not found!")
            else:
                start_time, end_time = result_five.split('-')
                if end_time == '23:59':
                    five = f'{start_time}-24:00'
                else:
                    five = result_five
                three_cherg_5.visible = True
                three_cherg_5.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            five,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("three_cherg_5 found!")
        except:
            three_cherg_5.visible = True
            three_cherg_5.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_five,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_six = main_database.get("3_cherg").get(f"{day_num_six}")
        try:
            if result_six == None:
                three_cherg_6.visible = False
                print("three_cherg_6 not found!")
            else:
                start_time, end_time = result_six.split('-')
                if end_time == '23:59':
                    six = f'{start_time}-24:00'
                else:
                    six = result_six
                three_cherg_6.visible = True
                three_cherg_6.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            six,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("three_cherg_6 found!")
        except:
            three_cherg_6.visible = True
            three_cherg_6.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_six,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

    def four_cherg():
        if page.client_storage.get("database_storage") == 1:
            day_num_one = db1_day_num_one
            day_num_two = db1_day_num_two
            day_num_three = db1_day_num_three
            day_num_four = db1_day_num_four
            day_num_five = db1_day_num_five
            day_num_six = db1_day_num_six
        if page.client_storage.get("database_storage") == 2:
            day_num_one = db2_day_num_one
            day_num_two = db2_day_num_two
            day_num_three = db2_day_num_three
            day_num_four = db2_day_num_four
            day_num_five = db2_day_num_five
            day_num_six = db2_day_num_six

        result_one = main_database.get("4_cherg").get(f"{day_num_one}")
        try:
            if result_one == None:
                four_cherg_1.visible = False
                print("four_cherg_1 not found!")
            else:
                start_time, end_time = result_one.split('-')
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = result_one
                four_cherg_1.visible = True
                four_cherg_1.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            one,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("four_cherg_1 found!")
        except:
            four_cherg_1.visible = True
            four_cherg_1.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_one,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_two = main_database.get("4_cherg").get(f"{day_num_two}")
        try:
            if result_two == None:
                four_cherg_2.visible = False
                print("four_cherg_2 not found!")
            else:
                start_time, end_time = result_two.split('-')
                if end_time == '23:59':
                    two = f'{start_time}-24:00'
                else:
                    two = result_two
                four_cherg_2.visible = True
                four_cherg_2.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            two,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("four_cherg_2 found!")
        except:
            four_cherg_2.visible = True
            four_cherg_2.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_two,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_three = main_database.get("4_cherg").get(f"{day_num_three}")
        try:
            if result_three == None:
                four_cherg_3.visible = False
                print("four_cherg_3 not found!")
            else:
                start_time, end_time = result_three.split('-')
                if end_time == '23:59':
                    three = f'{start_time}-24:00'
                else:
                    three = result_three
                four_cherg_3.visible = True
                four_cherg_3.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            three,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("four_cherg_3 found!")
        except:
            four_cherg_3.visible = True
            four_cherg_3.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_three,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_four = main_database.get("4_cherg").get(f"{day_num_four}")
        try:
            if result_four == None:
                four_cherg_4.visible = False
                print("four_cherg_4 not found!")
            else:
                start_time, end_time = result_four.split('-')
                if end_time == '23:59':
                    four = f'{start_time}-24:00'
                else:
                    four = result_four
                four_cherg_4.visible = True
                four_cherg_4.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            four,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("four_cherg_4 found!")
        except:
            four_cherg_4.visible = True
            four_cherg_4.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_four,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_five = main_database.get("4_cherg").get(f"{day_num_five}")
        try:
            if result_five == None:
                four_cherg_5.visible = False
                print("four_cherg_5 not found!")
            else:
                start_time, end_time = result_five.split('-')
                if end_time == '23:59':
                    five = f'{start_time}-24:00'
                else:
                    five = result_five
                four_cherg_5.visible = True
                four_cherg_5.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            five,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("four_cherg_5 found!")
        except:
            four_cherg_5.visible = True
            four_cherg_5.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_five,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_six = main_database.get("4_cherg").get(f"{day_num_six}")
        try:
            if result_six == None:
                four_cherg_6.visible = False
                print("four_cherg_6 not found!")
            else:
                start_time, end_time = result_six.split('-')
                if end_time == '23:59':
                    six = f'{start_time}-24:00'
                else:
                    six = result_six
                four_cherg_6.visible = True
                four_cherg_6.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            six,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("four_cherg_6 found!")
        except:
            four_cherg_6.visible = True
            four_cherg_6.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_six,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

    def five_cherg():
        if page.client_storage.get("database_storage") == 1:
            day_num_one = db1_day_num_one
            day_num_two = db1_day_num_two
            day_num_three = db1_day_num_three
            day_num_four = db1_day_num_four
            day_num_five = db1_day_num_five
            day_num_six = db1_day_num_six
        if page.client_storage.get("database_storage") == 2:
            day_num_one = db2_day_num_one
            day_num_two = db2_day_num_two
            day_num_three = db2_day_num_three
            day_num_four = db2_day_num_four
            day_num_five = db2_day_num_five
            day_num_six = db2_day_num_six

        result_one = main_database.get("5_cherg").get(f"{day_num_one}")
        try:
            if result_one == None:
                five_cherg_1.visible = False
                print("five_cherg_1 not found!")
            else:
                start_time, end_time = result_one.split('-')
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = result_one
                five_cherg_1.visible = True
                five_cherg_1.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            one,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("five_cherg_1 found!")
        except:
            five_cherg_1.visible = True
            five_cherg_1.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_one,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_two = main_database.get("5_cherg").get(f"{day_num_two}")
        try:
            if result_two == None:
                five_cherg_2.visible = False
                print("five_cherg_2 not found!")
            else:
                start_time, end_time = result_two.split('-')
                if end_time == '23:59':
                    two = f'{start_time}-24:00'
                else:
                    two = result_two
                five_cherg_2.visible = True
                five_cherg_2.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            two,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("five_cherg_2 found!")
        except:
            five_cherg_2.visible = True
            five_cherg_2.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_two,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_three = main_database.get("5_cherg").get(f"{day_num_three}")
        try:
            if result_three == None:
                five_cherg_3.visible = False
                print("five_cherg_3 not found!")
            else:
                start_time, end_time = result_three.split('-')
                if end_time == '23:59':
                    three = f'{start_time}-24:00'
                else:
                    three = result_three
                five_cherg_3.visible = True
                five_cherg_3.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            three,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("five_cherg_3 found!")
        except:
            five_cherg_3.visible = True
            five_cherg_3.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_three,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_four = main_database.get("5_cherg").get(f"{day_num_four}")
        try:
            if result_four == None:
                five_cherg_4.visible = False
                print("five_cherg_4 not found!")
            else:
                start_time, end_time = result_four.split('-')
                if end_time == '23:59':
                    four = f'{start_time}-24:00'
                else:
                    four = result_four
                five_cherg_4.visible = True
                five_cherg_4.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            four,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("five_cherg_4 found!")
        except:
            five_cherg_4.visible = True
            five_cherg_4.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_four,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_five = main_database.get("5_cherg").get(f"{day_num_five}")
        try:
            if result_five == None:
                five_cherg_5.visible = False
                print("five_cherg_5 not found!")
            else:
                start_time, end_time = result_five.split('-')
                if end_time == '23:59':
                    five = f'{start_time}-24:00'
                else:
                    five = result_five
                five_cherg_5.visible = True
                five_cherg_5.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            five,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("five_cherg_5 found!")
        except:
            five_cherg_5.visible = True
            five_cherg_5.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_five,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_six = main_database.get("5_cherg").get(f"{day_num_six}")
        try:
            if result_six == None:
                five_cherg_6.visible = False
                print("five_cherg_6 not found!")
            else:
                start_time, end_time = result_six.split('-')
                if end_time == '23:59':
                    six = f'{start_time}-24:00'
                else:
                    six = result_six
                five_cherg_6.visible = True
                five_cherg_6.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            six,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("five_cherg_6 found!")
        except:
            five_cherg_6.visible = True
            five_cherg_6.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_six,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

    def six_cherg():
        if page.client_storage.get("database_storage") == 1:
            day_num_one = db1_day_num_one
            day_num_two = db1_day_num_two
            day_num_three = db1_day_num_three
            day_num_four = db1_day_num_four
            day_num_five = db1_day_num_five
            day_num_six = db1_day_num_six
        if page.client_storage.get("database_storage") == 2:
            day_num_one = db2_day_num_one
            day_num_two = db2_day_num_two
            day_num_three = db2_day_num_three
            day_num_four = db2_day_num_four
            day_num_five = db2_day_num_five
            day_num_six = db2_day_num_six

        result_one = main_database.get("6_cherg").get(f"{day_num_one}")
        try:
            if result_one == None:
                six_cherg_1.visible = False
                print("six_cherg_1 not found!")
            else:
                start_time, end_time = result_one.split('-')
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = result_one
                six_cherg_1.visible = True
                six_cherg_1.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            one,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("six_cherg_1 found!")
        except:
            six_cherg_1.visible = True
            six_cherg_1.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_one,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_two = main_database.get("6_cherg").get(f"{day_num_two}")
        try:
            if result_two == None:
                six_cherg_2.visible = False
                print("six_cherg_2 not found!")
            else:
                start_time, end_time = result_two.split('-')
                if end_time == '23:59':
                    two = f'{start_time}-24:00'
                else:
                    two = result_two
                six_cherg_2.visible = True
                six_cherg_2.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            two,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("six_cherg_2 found!")
        except:
            six_cherg_2.visible = True
            six_cherg_2.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_two,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_three = main_database.get("6_cherg").get(f"{day_num_three}")
        try:
            if result_three == None:
                six_cherg_3.visible = False
                print("six_cherg_3 not found!")
            else:
                start_time, end_time = result_three.split('-')
                if end_time == '23:59':
                    three = f'{start_time}-24:00'
                else:
                    three = result_three
                six_cherg_3.visible = True
                six_cherg_3.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            three,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("six_cherg_3 found!")
        except:
            six_cherg_3.visible = True
            six_cherg_3.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_three,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_four = main_database.get("6_cherg").get(f"{day_num_four}")
        try:
            if result_four == None:
                six_cherg_4.visible = False
                print("six_cherg_4 not found!")
            else:
                start_time, end_time = result_four.split('-')
                if end_time == '23:59':
                    four = f'{start_time}-24:00'
                else:
                    four = result_four
                six_cherg_4.visible = True
                six_cherg_4.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            four,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("six_cherg_4 found!")
        except:
            six_cherg_4.visible = True
            six_cherg_4.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_four,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_five = main_database.get("6_cherg").get(f"{day_num_five}")
        try:
            if result_five == None:
                six_cherg_5.visible = False
                print("six_cherg_5 not found!")
            else:
                start_time, end_time = result_five.split('-')
                if end_time == '23:59':
                    five = f'{start_time}-24:00'
                else:
                    five = result_five
                six_cherg_5.visible = True
                six_cherg_5.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            five,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("six_cherg_5 found!")
        except:
            six_cherg_5.visible = True
            six_cherg_5.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_five,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

        result_six = main_database.get("6_cherg").get(f"{day_num_six}")
        try:
            if result_six == None:
                six_cherg_6.visible = False
                print("six_cherg_6 not found!")
            else:
                start_time, end_time = result_six.split('-')
                if end_time == '23:59':
                    six = f'{start_time}-24:00'
                else:
                    six = result_six
                six_cherg_6.visible = True
                six_cherg_6.content = Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        Text(
                            six,
                            size=21,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("six_cherg_6 found!")
        except:
            six_cherg_6.visible = True
            six_cherg_6.content = Row(
                wrap=True,
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_six,
                        text_align='center',
                        size=15,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print('Connection is not forecast!')

    logo = Container(
        content=Image(
            src=f"/icon.png",
            gapless_playback=True,
            height=150,
            width=150,
        )
    )

    title = Text(
        f'Світло Суми - Графік відключень на {day}',
        size=35,
        weight='w500',
        color=colors.BLACK,
        font_family="Golos Text"
    )

    head = Row(
        alignment='center',
        controls=[
            logo,
            title
        ]
    )

    chergs_table = DataTable(
        columns=[
            DataColumn(
                Text(
                    '1 черга',
                    size=24,
                    weight='w500',
                    color=colors.BLACK,
                    font_family="Golos Text"
                )
            ),
            DataColumn(
                Text(
                    '2 черга',
                    size=24,
                    weight='w500',
                    color=colors.BLACK,
                    font_family="Golos Text"
                )
            ),
            DataColumn(
                Text(
                    '3 черга',
                    size=24,
                    weight='w500',
                    color=colors.BLACK,
                    font_family="Golos Text"
                )
            ),
            DataColumn(
                Text(
                    '4 черга',
                    size=24,
                    weight='w500',
                    color=colors.BLACK,
                    font_family="Golos Text"
                )
            ),
            DataColumn(
                Text(
                    '5 черга',
                    size=24,
                    weight='w500',
                    color=colors.BLACK,
                    font_family="Golos Text"
                )
            ),
            DataColumn(
                Text(
                    '6 черга',
                    size=24,
                    weight='w500',
                    color=colors.BLACK,
                    font_family="Golos Text"
                )
            )
        ],
        rows=[
            DataRow(
                cells=[
                    DataCell(one_cherg_1),
                    DataCell(two_cherg_1),
                    DataCell(three_cherg_1),
                    DataCell(four_cherg_1),
                    DataCell(five_cherg_1),
                    DataCell(six_cherg_1)
                ]
            ),
            DataRow(
                cells=[
                    DataCell(one_cherg_2),
                    DataCell(two_cherg_2),
                    DataCell(three_cherg_2),
                    DataCell(four_cherg_2),
                    DataCell(five_cherg_2),
                    DataCell(six_cherg_2)
                ]
            ),
            DataRow(
                cells=[
                    DataCell(one_cherg_3),
                    DataCell(two_cherg_3),
                    DataCell(three_cherg_3),
                    DataCell(four_cherg_3),
                    DataCell(five_cherg_3),
                    DataCell(six_cherg_3)
                ]
            ),
            DataRow(
                cells=[
                    DataCell(one_cherg_4),
                    DataCell(two_cherg_4),
                    DataCell(three_cherg_4),
                    DataCell(four_cherg_4),
                    DataCell(five_cherg_4),
                    DataCell(six_cherg_4)
                ]
            ),
            DataRow(
                cells=[
                    DataCell(one_cherg_5),
                    DataCell(two_cherg_5),
                    DataCell(three_cherg_5),
                    DataCell(four_cherg_5),
                    DataCell(five_cherg_5),
                    DataCell(six_cherg_5)
                ]
            ),
            DataRow(
                cells=[
                    DataCell(one_cherg_6),
                    DataCell(two_cherg_6),
                    DataCell(three_cherg_6),
                    DataCell(four_cherg_6),
                    DataCell(five_cherg_6),
                    DataCell(six_cherg_6)
                ]
            )
        ]
    )

    chergs = Container(
        blur=10,
        padding=5,
        bgcolor=colors.BLACK26,
        border_radius=15,
        content=Row(
            spacing=1,
            vertical_alignment='center',
            alignment='center',
            controls=[
                Column(
                    spacing=1,
                    horizontal_alignment='center',
                    # alignment='center',
                    controls=[
                        Text(
                            '1 черга',
                            size=24,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        ),
                        Container(
                            alignment=alignment.center,
                            padding=10,
                            content=Column(
                                scroll=ScrollMode.ADAPTIVE,
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=9,
                                controls=[
                                    one_cherg_1,
                                    one_cherg_2,
                                    one_cherg_3,
                                    one_cherg_4,
                                    one_cherg_5,
                                    one_cherg_6,
                                ]
                            )
                        )
                    ]
                ),
                VerticalDivider(
                    color=colors.BLACK,
                    width=10,
                ),
                Column(
                    spacing=1,
                    horizontal_alignment='center',
                    # alignment='center',
                    controls=[
                        Text(
                            '2 черга',
                            size=24,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        ),
                        Container(
                            alignment=alignment.center,
                            padding=10,
                            content=Column(
                                scroll=ScrollMode.ADAPTIVE,
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=9,
                                controls=[
                                    two_cherg_1,
                                    two_cherg_2,
                                    two_cherg_3,
                                    two_cherg_4,
                                    two_cherg_5,
                                    two_cherg_6,
                                ]
                            )
                        )
                    ]
                ),
                VerticalDivider(
                    color=colors.BLACK,
                    width=10,
                ),
                Column(
                    spacing=1,
                    horizontal_alignment='center',
                    # alignment='center',
                    controls=[
                        Text(
                            '3 черга',
                            size=24,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        ),
                        Container(
                            alignment=alignment.center,
                            padding=10,
                            content=Column(
                                scroll=ScrollMode.ADAPTIVE,
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=9,
                                controls=[
                                    three_cherg_1,
                                    three_cherg_2,
                                    three_cherg_3,
                                    three_cherg_4,
                                    three_cherg_5,
                                    three_cherg_6,
                                ]
                            )
                        )
                    ]
                ),
                VerticalDivider(
                    color=colors.BLACK,
                    width=10,
                ),
                Column(
                    spacing=1,
                    horizontal_alignment='center',
                    # alignment='center',
                    controls=[
                        Text(
                            '4 черга',
                            size=24,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        ),
                        Container(
                            alignment=alignment.center,
                            padding=10,
                            content=Column(
                                scroll=ScrollMode.ADAPTIVE,
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=9,
                                controls=[
                                    four_cherg_1,
                                    four_cherg_2,
                                    four_cherg_3,
                                    four_cherg_4,
                                    four_cherg_5,
                                    four_cherg_6,
                                ]
                            )
                        )
                    ]
                ),
                VerticalDivider(
                    color=colors.BLACK,
                    width=10,
                ),
                Column(
                    spacing=1,
                    horizontal_alignment='center',
                    # alignment='center',
                    controls=[
                        Text(
                            '5 черга',
                            size=24,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        ),
                        Container(
                            alignment=alignment.center,
                            padding=10,
                            content=Column(
                                scroll=ScrollMode.ADAPTIVE,
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=9,
                                controls=[
                                    five_cherg_1,
                                    five_cherg_2,
                                    five_cherg_3,
                                    five_cherg_4,
                                    five_cherg_5,
                                    five_cherg_6,
                                ]
                            )
                        )
                    ]
                ),
                VerticalDivider(
                    color=colors.BLACK,
                    width=10,
                ),
                Column(
                    spacing=1,
                    horizontal_alignment='center',
                    # alignment='center',
                    controls=[
                        Text(
                            '6 черга',
                            size=24,
                            weight='w500',
                            color=colors.BLACK,
                            font_family="Golos Text"
                        ),
                        Container(
                            alignment=alignment.center,
                            padding=10,
                            content=Column(
                                scroll=ScrollMode.ADAPTIVE,
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=9,
                                controls=[
                                    six_cherg_1,
                                    six_cherg_2,
                                    six_cherg_3,
                                    six_cherg_4,
                                    six_cherg_5,
                                    six_cherg_6,
                                ]
                            )
                        )
                    ]
                ),

            ]
        )
    )

    main_container = Container(
        expand=True,
        gradient=LinearGradient(
            begin=alignment.top_right,
            end=alignment.bottom_left,
            colors=['#ffc366', '#ff6666']
        ),
        padding=15,
        content=Column(
            alignment='center',
            controls=[
                head,
                chergs_table
            ]
        )
    )

    page.fonts = {
        "Golos Text": "/fonts/GolosText.ttf"
    }
    page.title = 'Svitlo Sumy'
    page.theme_mode = ThemeMode.LIGHT
    page.window_height = 500
    page.window_width = 1110
    page.padding = 0
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    # page.window_center()
    # page.window_resizable = False
    page.window_title_bar_hidden = True
    page.add(main_container)
    page.update()
    one_cherg()
    two_cherg()
    three_cherg()
    four_cherg()
    five_cherg()
    six_cherg()


app(
    target=main,
    name="Svitlo Sumy",
    assets_dir='assets',
)
