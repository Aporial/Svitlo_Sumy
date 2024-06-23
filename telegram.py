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

    day = datetime.now().strftime(f"{today}.%m.%Y")

    def one_line():
        result_one = main_database.get("1_cherg").get(f"{day_num_one}")
        try:
            if result_one == None:
                one_cherg_1.visible = False
                line_1.cells.append(DataCell(Text()))
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
                line_1.cells.append(DataCell(one_cherg_1))
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
            line_1.cells.append(DataCell(one_cherg_1))
            page.update()
            print('Connection is not forecast!')

        result_one = main_database.get("2_cherg").get(f"{day_num_one}")
        try:
            if result_one == None:
                two_cherg_1.visible = False
                line_1.cells.append(DataCell(Text()))
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
                line_1.cells.append(DataCell(two_cherg_1))
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
            line_1.cells.append(DataCell(two_cherg_1))
            page.update()
            print('Connection is not forecast!')
        result_one = main_database.get("3_cherg").get(f"{day_num_one}")
        try:
            if result_one == None:
                three_cherg_1.visible = False
                line_1.cells.append(DataCell(Text()))
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
                line_1.cells.append(DataCell(three_cherg_1))
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
            line_1.cells.append(DataCell(three_cherg_1))
            page.update()
            print('Connection is not forecast!')

        result_one = main_database.get("4_cherg").get(f"{day_num_one}")
        try:
            if result_one == None:
                four_cherg_1.visible = False
                line_1.cells.append(DataCell(Text()))
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
                line_1.cells.append(DataCell(four_cherg_1))
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
            line_1.cells.append(DataCell(four_cherg_1))
            page.update()
            print('Connection is not forecast!')

        result_one = main_database.get("5_cherg").get(f"{day_num_one}")
        try:
            if result_one == None:
                five_cherg_1.visible = False
                line_1.cells.append(DataCell(Text()))
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
                line_1.cells.append(DataCell(five_cherg_1))
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
            line_1.cells.append(DataCell(five_cherg_1))
            page.update()
            print('Connection is not forecast!')

        result_one = main_database.get("6_cherg").get(f"{day_num_one}")
        try:
            if result_one == None:
                six_cherg_1.visible = False
                line_1.cells.append(DataCell(Text()))
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
                line_1.cells.append(DataCell(six_cherg_1))
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
            line_1.cells.append(DataCell(six_cherg_1))
            page.update()
            print('Connection is not forecast!')

    def two_line():
        result_two = main_database.get("1_cherg").get(f"{day_num_two}")
        try:
            if result_two == None:
                one_cherg_2.visible = False
                line_2.cells.append(DataCell(Text()))
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
                line_2.cells.append(DataCell(one_cherg_2))
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
            line_2.cells.append(DataCell(one_cherg_2))
            page.update()
            print('Connection is not forecast!')

        result_two = main_database.get("2_cherg").get(f"{day_num_two}")
        try:
            if result_two == None:
                two_cherg_2.visible = False
                line_2.cells.append(DataCell(Text()))
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
                line_2.cells.append(DataCell(two_cherg_2))
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
            line_2.cells.append(DataCell(two_cherg_2))
            page.update()
            print('Connection is not forecast!')

        result_two = main_database.get("3_cherg").get(f"{day_num_two}")
        try:
            if result_two == None:
                three_cherg_2.visible = False
                line_2.cells.append(DataCell(Text()))
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
                line_2.cells.append(DataCell(three_cherg_2))
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
            line_2.cells.append(DataCell(three_cherg_2))
            page.update()
            print('Connection is not forecast!')

        result_two = main_database.get("4_cherg").get(f"{day_num_two}")
        try:
            if result_two == None:
                four_cherg_2.visible = False
                line_2.cells.append(DataCell(Text()))
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
                line_2.cells.append(DataCell(four_cherg_2))
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
            line_2.cells.append(DataCell(four_cherg_2))
            page.update()
            print('Connection is not forecast!')

        result_two = main_database.get("5_cherg").get(f"{day_num_two}")
        try:
            if result_two == None:
                five_cherg_2.visible = False
                line_2.cells.append(DataCell(Text()))
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
                line_2.cells.append(DataCell(five_cherg_2))
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
            line_2.cells.append(DataCell(five_cherg_2))
            page.update()
            print('Connection is not forecast!')

        result_two = main_database.get("6_cherg").get(f"{day_num_two}")
        try:
            if result_two == None:
                six_cherg_2.visible = False
                line_2.cells.append(DataCell(Text()))
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
                line_2.cells.append(DataCell(six_cherg_2))
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
            line_2.cells.append(DataCell(six_cherg_2))
            page.update()
            print('Connection is not forecast!')

    def three_line():
        result_three = main_database.get("1_cherg").get(f"{day_num_three}")
        try:
            if result_three == None:
                one_cherg_3.visible = False
                line_3.cells.append(DataCell(Text()))
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
                line_3.cells.append(DataCell(one_cherg_3))
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
            line_3.cells.append(DataCell(one_cherg_3))
            print('Connection is not forecast!')

        result_three = main_database.get("2_cherg").get(f"{day_num_three}")
        try:
            if result_three == None:
                two_cherg_3.visible = False
                line_3.cells.append(DataCell(Text()))
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
                line_3.cells.append(DataCell(two_cherg_3))
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
            line_3.cells.append(DataCell(two_cherg_3))
            page.update()
            print('Connection is not forecast!')

        result_three = main_database.get("3_cherg").get(f"{day_num_three}")
        try:
            if result_three == None:
                three_cherg_3.visible = False
                line_3.cells.append(DataCell(Text()))
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
                line_3.cells.append(DataCell(three_cherg_3))
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
            line_3.cells.append(DataCell(three_cherg_3))
            page.update()
            print('Connection is not forecast!')

        result_three = main_database.get("4_cherg").get(f"{day_num_three}")
        try:
            if result_three == None:
                four_cherg_3.visible = False
                line_3.cells.append(DataCell(Text()))
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
                line_3.cells.append(DataCell(four_cherg_3))
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
            line_3.cells.append(DataCell(four_cherg_3))
            page.update()
            print('Connection is not forecast!')

        result_three = main_database.get("5_cherg").get(f"{day_num_three}")
        try:
            if result_three == None:
                five_cherg_3.visible = False
                line_3.cells.append(DataCell(Text()))
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
                line_3.cells.append(DataCell(five_cherg_3))
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
            line_3.cells.append(DataCell(five_cherg_3))
            page.update()
            print('Connection is not forecast!')

        result_three = main_database.get("6_cherg").get(f"{day_num_three}")
        try:
            if result_three == None:
                six_cherg_3.visible = False
                line_3.cells.append(DataCell(Text()))
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
                line_3.cells.append(DataCell(six_cherg_3))
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
            line_3.cells.append(DataCell(six_cherg_3))
            page.update()
            print('Connection is not forecast!')

    def four_line():
        result_four = main_database.get("1_cherg").get(f"{day_num_four}")
        try:
            if result_four == None:
                one_cherg_4.visible = False
                line_4.cells.append(DataCell(Text()))
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
                line_4.cells.append(DataCell(one_cherg_4))
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
            line_4.cells.append(DataCell(one_cherg_4))
            page.update()
            print('Connection is not forecast!')

        result_four = main_database.get("2_cherg").get(f"{day_num_four}")
        try:
            if result_four == None:
                two_cherg_4.visible = False
                line_4.cells.append(DataCell(Text()))
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
                line_4.cells.append(DataCell(two_cherg_4))
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
            line_4.cells.append(DataCell(two_cherg_4))
            page.update()
            print('Connection is not forecast!')

        result_four = main_database.get("3_cherg").get(f"{day_num_four}")
        try:
            if result_four == None:
                three_cherg_4.visible = False
                line_4.cells.append(DataCell(Text()))
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
                line_4.cells.append(DataCell(three_cherg_4))
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
            line_4.cells.append(DataCell(three_cherg_4))
            page.update()
            print('Connection is not forecast!')

        result_four = main_database.get("4_cherg").get(f"{day_num_four}")
        try:
            if result_four == None:
                four_cherg_4.visible = False
                line_4.cells.append(DataCell(Text()))
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
                line_4.cells.append(DataCell(four_cherg_4))
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
            line_4.cells.append(DataCell(four_cherg_4))
            page.update()
            print('Connection is not forecast!')

        result_four = main_database.get("5_cherg").get(f"{day_num_four}")
        try:
            if result_four == None:
                five_cherg_4.visible = False
                line_4.cells.append(DataCell(Text()))
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
                line_4.cells.append(DataCell(five_cherg_4))
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
            line_4.cells.append(DataCell(five_cherg_4))
            page.update()
            print('Connection is not forecast!')

        result_four = main_database.get("6_cherg").get(f"{day_num_four}")
        try:
            if result_four == None:
                six_cherg_4.visible = False
                line_4.cells.append(DataCell(Text()))
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
                line_4.cells.append(DataCell(six_cherg_4))
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
            line_4.cells.append(DataCell(six_cherg_4))
            page.update()
            print('Connection is not forecast!')

    def five_line():
        result_five = main_database.get("1_cherg").get(f"{day_num_five}")
        try:
            if result_five == None:
                one_cherg_5.visible = False
                line_5.cells.append(DataCell(Text()))
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
                line_5.cells.append(DataCell(one_cherg_5))
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
            line_5.cells.append(DataCell(one_cherg_5))
            page.update()
            print('Connection is not forecast!')

        result_five = main_database.get("2_cherg").get(f"{day_num_five}")
        try:
            if result_five == None:
                two_cherg_5.visible = False
                line_5.cells.append(DataCell(Text()))
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
                line_5.cells.append(DataCell(two_cherg_5))
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
            line_5.cells.append(DataCell(two_cherg_5))
            page.update()
            print('Connection is not forecast!')

        result_five = main_database.get("3_cherg").get(f"{day_num_five}")
        try:
            if result_five == None:
                three_cherg_5.visible = False
                line_5.cells.append(DataCell(Text()))
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
                line_5.cells.append(DataCell(three_cherg_5))
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
            line_5.cells.append(DataCell(three_cherg_5))
            page.update()
            print('Connection is not forecast!')

        result_five = main_database.get("4_cherg").get(f"{day_num_five}")
        try:
            if result_five == None:
                four_cherg_5.visible = False
                line_5.cells.append(DataCell(Text()))
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
                line_5.cells.append(DataCell(four_cherg_5))
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
            line_5.cells.append(DataCell(four_cherg_5))
            page.update()
            print('Connection is not forecast!')

        result_five = main_database.get("5_cherg").get(f"{day_num_five}")
        try:
            if result_five == None:
                five_cherg_5.visible = False
                line_5.cells.append(DataCell(Text()))
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
                line_5.cells.append(DataCell(five_cherg_5))
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
            line_5.cells.append(DataCell(five_cherg_5))
            page.update()
            print('Connection is not forecast!')

        result_five = main_database.get("6_cherg").get(f"{day_num_five}")
        try:
            if result_five == None:
                six_cherg_5.visible = False
                line_5.cells.append(DataCell(Text()))
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
                line_5.cells.append(DataCell(six_cherg_5))
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
            line_5.cells.append(DataCell(six_cherg_5))
            page.update()
            print('Connection is not forecast!')

    def six_line():
        result_six = main_database.get("1_cherg").get(f"{day_num_six}")
        try:
            if result_six == None:
                one_cherg_6.visible = False
                line_6.cells.append(DataCell(Text()))
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
                line_6.cells.append(DataCell(one_cherg_6))
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
            line_6.cells.append(DataCell(one_cherg_6))
            page.update()
            print('Connection is not forecast!')

        result_six = main_database.get("2_cherg").get(f"{day_num_six}")
        try:
            if result_six == None:
                two_cherg_6.visible = False
                line_6.cells.append(DataCell(Text()))
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
                line_6.cells.append(DataCell(two_cherg_6))
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
            line_6.cells.append(DataCell(two_cherg_6))
            page.update()
            print('Connection is not forecast!')

        result_six = main_database.get("3_cherg").get(f"{day_num_six}")
        try:
            if result_six == None:
                three_cherg_6.visible = False
                line_6.cells.append(DataCell(Text()))
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
                line_6.cells.append(DataCell(three_cherg_6))
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
            line_6.cells.append(DataCell(three_cherg_6))
            page.update()
            print('Connection is not forecast!')

        result_six = main_database.get("4_cherg").get(f"{day_num_six}")
        try:
            if result_six == None:
                four_cherg_6.visible = False
                line_6.cells.append(DataCell(Text()))
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
                line_6.cells.append(DataCell(four_cherg_6))
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
            line_6.cells.append(DataCell(four_cherg_6))
            page.update()
            print('Connection is not forecast!')

        result_six = main_database.get("5_cherg").get(f"{day_num_six}")
        try:
            if result_six == None:
                five_cherg_6.visible = False
                line_6.cells.append(DataCell(Text()))
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
                line_6.cells.append(DataCell(five_cherg_6))
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
            line_6.cells.append(DataCell(five_cherg_6))
            page.update()
            print('Connection is not forecast!')

        result_six = main_database.get("6_cherg").get(f"{day_num_six}")
        try:
            if result_six == None:
                six_cherg_6.visible = False
                line_6.cells.append(DataCell(Text()))
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
                line_6.cells.append(DataCell(six_cherg_6))
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
            line_6.cells.append(DataCell(six_cherg_6))
            page.update()
            print('Connection is not forecast!')

    day_container = Container(
        blur=10,
        padding=1,
        bgcolor=colors.BLACK26,
        border_radius=15,
        content=Text(
            f" {day} ",
            size=35,
            weight='w500',
            color='#ffcc66',
            font_family="Golos Text"
        )
    )

    logo = Container(
        content=Image(
            src=f"/icon.png",
            gapless_playback=True,
            height=150,
            width=150,
        )
    )

    title = Text(
        'Світло Суми - Графік відключень на',
        size=35,
        weight='w500',
        color=colors.BLACK,
        font_family="Golos Text"
    )

    head = Row(
        alignment='center',
        controls=[
            logo,
            title,
            day_container
        ]
    )

    line_1 = DataRow(
        cells=[]
    )

    line_2 = DataRow(
        cells=[]
    )

    line_3 = DataRow(
        cells=[]
    )

    line_4 = DataRow(
        cells=[]
    )

    line_5 = DataRow(
        cells=[]
    )

    line_6 = DataRow(
        cells=[]
    )

    chergs_names = Row(
        alignment=MainAxisAlignment.CENTER,
        spacing=43,
        controls=[
            Container(
                blur=10,
                padding=5,
                bgcolor=colors.BLACK26,
                border_radius=15,
                width=125,
                content=Text(
                    "1 черга",
                    size=24,
                    weight='w500',
                    color='#ffcc66',
                    font_family="Golos Text",
                    text_align='center'
                )
            ),
            Container(
                blur=10,
                padding=5,
                bgcolor=colors.BLACK26,
                border_radius=15,
                width=125,
                content=Text(
                    "2 черга",
                    size=24,
                    weight='w500',
                    color='#ffcc66',
                    font_family="Golos Text",
                    text_align='center'
                )
            ),
            Container(
                blur=10,
                padding=5,
                bgcolor=colors.BLACK26,
                border_radius=15,
                width=125,
                content=Text(
                    "3 черга",
                    size=24,
                    weight='w500',
                    color='#ffcc66',
                    font_family="Golos Text",
                    text_align='center'
                )
            ),
            Container(
                blur=10,
                padding=5,
                bgcolor=colors.BLACK26,
                border_radius=15,
                width=125,
                content=Text(
                    "4 черга",
                    size=24,
                    weight='w500',
                    color='#ffcc66',
                    font_family="Golos Text",
                    text_align='center'
                )
            ),
            Container(
                blur=10,
                padding=5,
                bgcolor=colors.BLACK26,
                border_radius=15,
                width=125,
                content=Text(
                    "5 черга",
                    size=24,
                    weight='w500',
                    color='#ffcc66',
                    font_family="Golos Text",
                    text_align='center'
                )
            ),
            Container(
                blur=10,
                padding=5,
                bgcolor=colors.BLACK26,
                border_radius=15,
                width=125,
                content=Text(
                    "6 черга",
                    size=24,
                    weight='w500',
                    color='#ffcc66',
                    font_family="Golos Text",
                    text_align='center'
                )
            ),

        ]
    )

    chergs_table = Container(
        alignment=alignment.center,
        blur=10,
        padding=5,
        bgcolor=colors.BLACK26,
        border_radius=15,
        content=DataTable(
            heading_row_height=0,
            horizontal_margin=12,
            data_row_max_height=70,
            vertical_lines=BorderSide(1, colors.BLACK),
            # horizontal_lines=BorderSide(1, colors.BLACK),
            divider_thickness=0.01,
            column_spacing=25,
            columns=[
                DataColumn(
                    Text(
                        '     1 черга',
                        size=24,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ),
                DataColumn(
                    Text(
                        '     2 черга',
                        size=24,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ),
                DataColumn(
                    Text(
                        '     3 черга',
                        size=24,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ),
                DataColumn(
                    Text(
                        '     4 черга',
                        size=24,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ),
                DataColumn(
                    Text(
                        '     5 черга',
                        size=24,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ),
                DataColumn(
                    Text(
                        '     6 черга',
                        size=24,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                )
            ],
            rows=[
                line_1,
                line_2,
                line_3,
                line_4,
                # line_5,
                # line_6
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
                chergs_names,
                chergs_table
            ]
        )
    )

    page.fonts = {
        "Golos Text": "/fonts/GolosText.ttf"
    }
    page.title = 'Svitlo Sumy'
    page.theme_mode = ThemeMode.LIGHT
    page.window_height = 402
    page.window_width = 1074
    page.padding = 0
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_center()
    # page.window_resizable = False
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.add(main_container)
    one_line()
    two_line()
    three_line()
    four_line()
    five_line()
    six_line()
    page.update()


app(
    target=main,
    name="Svitlo Sumy",
    assets_dir='assets',
)
