import flet as ft
from database_1 import (db1_day_num_one,
                        db1_day_num_two,
                        db1_day_num_three,
                        db1_day_num_four,
                        db1_day_num_five,
                        db1_day_num_six,
                        db1_day_num_seven,
                        db1_day_num_eight,
                        db1_day_num_nine,
                        db1_day_num_ten,
                        db1_day_num_eleven,
                        db1_day_num_twelve)
from database_1 import (db1_day_tomorrow_one,
                        db1_day_tomorrow_two,
                        db1_day_tomorrow_three,
                        db1_day_tomorrow_four,
                        db1_day_tomorrow_five,
                        db1_day_tomorrow_six,
                        db1_day_tomorrow_seven,
                        db1_day_tomorrow_eight,
                        db1_day_tomorrow_nine,
                        db1_day_tomorrow_ten,
                        db1_day_tomorrow_eleven,
                        db1_day_tomorrow_twelve)
from database_1 import (db1_day_after_tomorrow_one,
                        db1_day_after_tomorrow_two,
                        db1_day_after_tomorrow_three,
                        db1_day_after_tomorrow_four,
                        db1_day_after_tomorrow_five,
                        db1_day_after_tomorrow_six,
                        db1_day_after_tomorrow_seven,
                        db1_day_after_tomorrow_eight,
                        db1_day_after_tomorrow_nine,
                        db1_day_after_tomorrow_ten,
                        db1_day_after_tomorrow_eleven,
                        db1_day_after_tomorrow_twelve)
from database_2 import (db2_day_num_one,
                        db2_day_num_two,
                        db2_day_num_three,
                        db2_day_num_four,
                        db2_day_num_five,
                        db2_day_num_six,
                        db2_day_num_seven,
                        db2_day_num_eight,
                        db2_day_num_nine,
                        db2_day_num_ten,
                        db2_day_num_eleven,
                        db2_day_num_twelve)
from database_2 import (db2_day_tomorrow_one,
                        db2_day_tomorrow_two,
                        db2_day_tomorrow_three,
                        db2_day_tomorrow_four,
                        db2_day_tomorrow_five,
                        db2_day_tomorrow_six,
                        db2_day_tomorrow_seven,
                        db2_day_tomorrow_eight,
                        db2_day_tomorrow_nine,
                        db2_day_tomorrow_ten,
                        db2_day_tomorrow_eleven,
                        db2_day_tomorrow_twelve)
from database_2 import (db2_day_after_tomorrow_one,
                        db2_day_after_tomorrow_two,
                        db2_day_after_tomorrow_three,
                        db2_day_after_tomorrow_four,
                        db2_day_after_tomorrow_five,
                        db2_day_after_tomorrow_six,
                        db2_day_after_tomorrow_seven,
                        db2_day_after_tomorrow_eight,
                        db2_day_after_tomorrow_nine,
                        db2_day_after_tomorrow_ten,
                        db2_day_after_tomorrow_eleven,
                        db2_day_after_tomorrow_twelve)
from functions import check_cherg, day_of_week_today, day_of_week_tomorrow, day_of_week_after_tomorrow, seven_days, today
from time_now import (time_now_1,
                      time_now_2,
                      time_now_3,
                      time_now_4,
                      time_now_5,
                      time_now_6,
                      time_now_7,
                      time_now_8,
                      time_now_9,
                      time_now_10,
                      time_now_11,
                      time_now_12)
from time_tomorrow import (time_tomorrow_1,
                           time_tomorrow_2,
                           time_tomorrow_3,
                           time_tomorrow_4,
                           time_tomorrow_5,
                           time_tomorrow_6,
                           time_tomorrow_7,
                           time_tomorrow_8,
                           time_tomorrow_9,
                           time_tomorrow_10,
                           time_tomorrow_11,
                           time_tomorrow_12)
from time_after_tomorrow import (time_after_tomorrow_1,
                                 time_after_tomorrow_2,
                                 time_after_tomorrow_3,
                                 time_after_tomorrow_4,
                                 time_after_tomorrow_5,
                                 time_after_tomorrow_6,
                                 time_after_tomorrow_7,
                                 time_after_tomorrow_8,
                                 time_after_tomorrow_9,
                                 time_after_tomorrow_10,
                                 time_after_tomorrow_11,
                                 time_after_tomorrow_12
                                 )
from datetime import datetime
import time
import urllib.request
import json
from firebase import firebase


def main(page: ft.Page):

    def source_github():
        with urllib.request.urlopen("https://raw.githubusercontent.com/Aporial/Svitlo_Sumy/main/database/database.json") as url:
            main_database = json.load(url)
            source_check = main_database.get("source")
            if source_check == 'github':
                print('Source:', source_check)
                page.client_storage.set("source", source_check)
                database = main_database.get("database")
                print('DATABASE:', database)
                page.client_storage.set("database_storage", database)
                page.client_storage.set("main_database", main_database)
            if source_check == 'firebase':
                source_firebase()

    def source_firebase():
        database_connection = firebase.FirebaseApplication(
            'https://svitlo-sumy-default-rtdb.europe-west1.firebasedatabase.app/', authentication=None)
        main_database = database_connection.get("/", None)
        source_check = main_database.get("source")
        if source_check == 'firebase':
            print('Source:', source_check)
            page.client_storage.set("source", source_check)
            database = main_database.get("database")
            print('DATABASE:', database)
            page.client_storage.set("database_storage", database)
            page.client_storage.set("main_database", main_database)
        if source_check == 'github':
            source_github()

    def check_telegram():
        if page.client_storage.get('telegram_check') == None:
            if page.client_storage.get("number") == None:
                print('Queue has not yet been selected!')
            else:
                time.sleep(2)
                telegram_banner.open = True
                print("Telegram was not opened!")
        if page.client_storage.get('telegram_check') == True:
            print("Telegram was opened!")
        if page.client_storage.get('telegram_check') == False:
            if str(today) == page.client_storage.get('day_close'):
                time.sleep(2)
                telegram_banner.open = True
                print('7 days have passed!')
        page.update()

    def check_cherg_main():
        if storage() == None:
            text_after_img.content = ft.Text(
                "Оберіть чергу",
                size=24,
                weight='w500',
                color='#ffcc66',
                font_family="Golos Text",
                text_align='center'
            )
            text_after_img.update()
        else:
            text_after_img.content = ft.Text(
                f"{storage()} черга",
                size=24,
                weight='w500',
                color='#ffcc66',
                font_family="Golos Text",
                text_align='center'
            )
            text_after_img.update()

    def open_list():
        bs.open = True
        page.navigation_bar.selected_index = 1
        info_tab.visible = False
        bs.update()
        page.update()

    def on_tab(e):
        my_index = e.control.selected_index
        if my_index == 0:
            lamp_img.visible = True
            text_after_img.visible = True
            main_info.visible = True
            info_tab.visible = False
            open_list()
        if my_index == 1:
            lamp_img.visible = True
            text_after_img.visible = True
            main_info.visible = True
            info_tab.visible = False
            page.update()
        if my_index == 2:
            info_tab.visible = True
            lamp_img.visible = False
            text_after_img.visible = False
            main_info.visible = False
            page.update()

    def mono_click(e):
        page.launch_url('https://send.monobank.ua/jar/7rkGHNfQpV',
                        web_window_name='Monobank')

    def telegram_click(e):
        page.launch_url('https://t.me/never_find_myself',
                        web_window_name='Telegram')

    def open_telegram_channel(e):
        page.launch_url('https://t.me/sumy_svitlo',
                        web_window_name='Telegram')

    def cherg_choise(e):
        numb_cherg = e.control.data
        page.client_storage.set("number", numb_cherg)
        bs.open = False
        bs.update()
        check_storage_main()

    def check_storage():
        if page.client_storage.get("number") == None:
            try:
                check_cherg_main()
                if page.client_storage.get("source") == None:
                    try:
                        source_github()
                    except:
                        source_firebase()
                if page.client_storage.get("source") == "github":
                    source_github()
                if page.client_storage.get("source") == "firebase":
                    source_firebase()
                time = datetime.now().strftime("%d.%m.%Y о %H:%M:%S")
                page.client_storage.set('time', time)
                open_list()
                print('Connected!')
            except:
                one_button.disabled = True
                two_button.disabled = True
                three_button.disabled = True
                four_button.disabled = True
                five_button.disabled = True
                six_button.disabled = True
                alert_conn_first()
                print("Fail connection!")
        else:
            try:
                check_cherg_main()
                if page.client_storage.get("source") == None:
                    try:
                        source_github()
                    except:
                        source_firebase()
                if page.client_storage.get("source") == "github":
                    source_github()
                if page.client_storage.get("source") == "firebase":
                    source_firebase()
                time = datetime.now().strftime("%d.%m.%Y о %H:%M:%S")
                page.client_storage.set('time', time)
                print('Connected!')
            except:
                alert_conn_start()
                print("Fail connection!")
            check_storage_main()

    def check_storage_refresh():
        try:
            check_cherg_main()
            if page.client_storage.get("source") == None:
                try:
                    source_github()
                except:
                    source_firebase()
            if page.client_storage.get("source") == "github":
                source_github()
            if page.client_storage.get("source") == "firebase":
                source_firebase()
            data = datetime.now().strftime("%d.%m.%Y о %H:%M:%S")
            page.client_storage.set('time', data)
            time.sleep(1)
            print('Connected!')
        except:
            alert_conn_start()
            print("Fail connection!")
        check_storage_main()

    def check_storage_main():
        check_cherg_main()
        current_time = datetime.now().time()
        storage_info = storage()
        cherg = check_cherg(storage_info)
        main_database = page.client_storage.get("main_database")
        one_check = page.client_storage.get("one")
        two_check = page.client_storage.get("two")
        three_check = page.client_storage.get("three")
        four_check = page.client_storage.get("four")
        five_check = page.client_storage.get("five")
        six_check = page.client_storage.get("six")
        if page.client_storage.get("database_storage") == 1:
            day_num_one = db1_day_num_one
            day_num_two = db1_day_num_two
            day_num_three = db1_day_num_three
            day_num_four = db1_day_num_four
            day_num_five = db1_day_num_five
            day_num_six = db1_day_num_six
            day_num_seven = db1_day_num_seven
            day_num_eight = db1_day_num_eight
            day_num_nine = db1_day_num_nine
            day_num_ten = db1_day_num_ten
            day_num_eleven = db1_day_num_eleven
            day_num_twelve = db1_day_num_twelve
        if page.client_storage.get("database_storage") == 2:
            day_num_one = db2_day_num_one
            day_num_two = db2_day_num_two
            day_num_three = db2_day_num_three
            day_num_four = db2_day_num_four
            day_num_five = db2_day_num_five
            day_num_six = db2_day_num_six
            day_num_seven = db2_day_num_seven
            day_num_eight = db2_day_num_eight
            day_num_nine = db2_day_num_nine
            day_num_ten = db2_day_num_ten
            day_num_eleven = db2_day_num_eleven
            day_num_twelve = db2_day_num_twelve

        result_one = main_database.get(f"{cherg}").get(f"{day_num_one}")
        if result_one == None:
            page.client_storage.remove("one")
            time_now_1.visible = False
            print("One not found!")
        else:
            page.client_storage.set("one", result_one)
            one_check = page.client_storage.get("one")
            try:
                start_time, end_time = one_check.split('-')
                time_start = datetime.strptime(start_time, '%H:%M').time()
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = page.client_storage.get("one")
                time_now_1.visible = True
                if time_end <= current_time:
                    time_now_1.bgcolor = ft.colors.GREY_400
                    time_now_1.content = ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Container(width=25),
                            ft.Text(
                                one,
                                size=21,
                                weight='w500',
                                color=ft.colors.BLACK,
                                font_family="Golos Text"
                            ),
                            ft.Icon(
                                name=ft.icons.DONE_ALL_ROUNDED,
                                color=ft.colors.BLACK
                            )
                        ]
                    )
                elif time_start <= current_time <= time_end:
                    time_now_1.bgcolor = '#ffcc66'
                    time_now_1.content = ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Container(width=25),
                            ft.Text(
                                one,
                                size=21,
                                weight='w500',
                                color=ft.colors.BLACK,
                                font_family="Golos Text"
                            ),
                            ft.Icon(
                                name=ft.icons.BROWSE_GALLERY_OUTLINED,
                                color=ft.colors.BLACK
                            )
                        ]
                    )
                else:
                    time_now_1.bgcolor = '#ffcc66'
                    time_now_1.content = ft.Row(
                        alignment="center",
                        vertical_alignment='center',
                        controls=[
                            ft.Text(
                                one,
                                size=21,
                                weight='w500',
                                color=ft.colors.BLACK,
                                font_family="Golos Text"
                            )
                        ]
                    )
                page.update()
                print("One found!")
            except:
                one = page.client_storage.get("one")
                time_now_1.visible = True
                time_now_1.bgcolor = '#ffcc66'
                time_now_1.content = ft.Row(
                    wrap=True,
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            one,
                            text_align='center',
                            size=18,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("Connection is not forecast!")
        result_two = main_database.get(f"{cherg}").get(f"{day_num_two}")
        if result_two == None:
            page.client_storage.remove("two")
            time_now_2.visible = False
            print("Two not found!")
        else:
            page.client_storage.set("two", result_two)
            two_check = page.client_storage.get("two")
            start_time, end_time = two_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                two = f'{start_time}-24:00'
            else:
                two = page.client_storage.get("two")
            time_now_2.visible = True
            if time_end <= current_time:
                time_now_2.bgcolor = ft.colors.GREY_400
                time_now_2.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            two,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.DONE_ALL_ROUNDED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            elif time_start <= current_time <= time_end:
                time_now_2.bgcolor = '#ffcc66'
                time_now_2.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            two,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.BROWSE_GALLERY_OUTLINED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            else:
                time_now_2.bgcolor = '#ffcc66'
                time_now_2.content = ft.Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            two,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
            page.update()
            print("Two found!")

        result_three = main_database.get(f"{cherg}").get(f"{day_num_three}")
        if result_three == None:
            page.client_storage.remove("three")
            time_now_3.visible = False
            print("Three not found!")
        else:
            page.client_storage.set("three", result_three)
            three_check = page.client_storage.get("three")
            start_time, end_time = three_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                three = f'{start_time}-24:00'
            else:
                three = page.client_storage.get("three")
            time_now_3.visible = True
            if time_end <= current_time:
                time_now_3.bgcolor = ft.colors.GREY_400
                time_now_3.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            three,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.DONE_ALL_ROUNDED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            elif time_start <= current_time <= time_end:
                time_now_3.bgcolor = '#ffcc66'
                time_now_3.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            three,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.BROWSE_GALLERY_OUTLINED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            else:
                time_now_3.bgcolor = '#ffcc66'
                time_now_3.content = ft.Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            three,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
            page.update()
            print("Three found!")

        result_four = main_database.get(f"{cherg}").get(f"{day_num_four}")
        if result_four == None:
            page.client_storage.remove("four")
            time_now_4.visible = False
            print("Four not found!")
        else:
            page.client_storage.set("four", result_four)
            four_check = page.client_storage.get("four")
            start_time, end_time = four_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                four = f'{start_time}-24:00'
            else:
                four = page.client_storage.get("four")
            time_now_4.visible = True
            if time_end <= current_time:
                time_now_4.bgcolor = ft.colors.GREY_400
                time_now_4.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            four,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.DONE_ALL_ROUNDED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            elif time_start <= current_time <= time_end:
                time_now_4.bgcolor = '#ffcc66'
                time_now_4.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            four,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.BROWSE_GALLERY_OUTLINED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            else:
                time_now_4.bgcolor = '#ffcc66'
                time_now_4.content = ft.Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            four,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
            page.update()
            print("Four found!")

        result_five = main_database.get(f"{cherg}").get(f"{day_num_five}")
        if result_five == None:
            page.client_storage.remove("five")
            time_now_5.visible = False
            print("Five not found!")
        else:
            page.client_storage.set("five", result_five)
            five_check = page.client_storage.get("five")
            start_time, end_time = five_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                five = f'{start_time}-24:00'
            else:
                five = page.client_storage.get("five")
            time_now_5.visible = True
            if time_end <= current_time:
                time_now_5.bgcolor = ft.colors.GREY_400
                time_now_5.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            five,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.DONE_ALL_ROUNDED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            elif time_start <= current_time <= time_end:
                time_now_5.bgcolor = '#ffcc66'
                time_now_5.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            five,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.BROWSE_GALLERY_OUTLINED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            else:
                time_now_5.bgcolor = '#ffcc66'
                time_now_5.content = ft.Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            five,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
            page.update()
            print("Five found!")

        result_six = main_database.get(f"{cherg}").get(f"{day_num_six}")
        if result_six == None:
            page.client_storage.remove("six")
            time_now_6.visible = False
            print("Six not found!")
        else:
            page.client_storage.set("six", result_six)
            six_check = page.client_storage.get("six")
            start_time, end_time = six_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                six = f'{start_time}-24:00'
            else:
                six = page.client_storage.get("six")
            time_now_6.visible = True
            if time_end <= current_time:
                time_now_6.bgcolor = ft.colors.GREY_400
                time_now_6.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            six,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.DONE_ALL_ROUNDED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            elif time_start <= current_time <= time_end:
                time_now_6.bgcolor = '#ffcc66'
                time_now_6.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            six,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.BROWSE_GALLERY_OUTLINED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            else:
                time_now_6.bgcolor = '#ffcc66'
                time_now_6.content = ft.Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            six,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
            page.update()
            print("Six found!")

        result_seven = main_database.get(f"{cherg}").get(f"{day_num_seven}")
        if result_seven == None:
            page.client_storage.remove("seven")
            time_now_7.visible = False
            print("Seven not found!")
        else:
            page.client_storage.set("seven", result_seven)
            seven_check = page.client_storage.get("seven")
            start_time, end_time = seven_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                seven = f'{start_time}-24:00'
            else:
                seven = page.client_storage.get("seven")
            time_now_7.visible = True
            if time_end <= current_time:
                time_now_7.bgcolor = ft.colors.GREY_400
                time_now_7.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            seven,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.DONE_ALL_ROUNDED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            elif time_start <= current_time <= time_end:
                time_now_7.bgcolor = '#ffcc66'
                time_now_7.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            seven,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.BROWSE_GALLERY_OUTLINED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            else:
                time_now_7.bgcolor = '#ffcc66'
                time_now_7.content = ft.Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            seven,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
            page.update()
            print("Seven found!")

        result_eight = main_database.get(f"{cherg}").get(f"{day_num_eight}")
        if result_eight == None:
            page.client_storage.remove("eight")
            time_now_8.visible = False
            print("Eight not found!")
        else:
            page.client_storage.set("eight", result_eight)
            eight_check = page.client_storage.get("eight")
            start_time, end_time = eight_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                eight = f'{start_time}-24:00'
            else:
                eight = page.client_storage.get("eight")
            time_now_8.visible = True
            if time_end <= current_time:
                time_now_8.bgcolor = ft.colors.GREY_400
                time_now_8.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            eight,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.DONE_ALL_ROUNDED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            elif time_start <= current_time <= time_end:
                time_now_8.bgcolor = '#ffcc66'
                time_now_8.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            eight,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.BROWSE_GALLERY_OUTLINED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            else:
                time_now_8.bgcolor = '#ffcc66'
                time_now_8.content = ft.Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            eight,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
            page.update()
            print("Eight found!")

        result_nine = main_database.get(f"{cherg}").get(f"{day_num_nine}")
        if result_nine == None:
            page.client_storage.remove("nine")
            time_now_9.visible = False
            print("Nine not found!")
        else:
            page.client_storage.set("nine", result_nine)
            nine_check = page.client_storage.get("nine")
            start_time, end_time = nine_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                nine = f'{start_time}-24:00'
            else:
                nine = page.client_storage.get("three")
            time_now_9.visible = True
            if time_end <= current_time:
                time_now_9.bgcolor = ft.colors.GREY_400
                time_now_9.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            nine,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.DONE_ALL_ROUNDED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            elif time_start <= current_time <= time_end:
                time_now_9.bgcolor = '#ffcc66'
                time_now_9.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            nine,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.BROWSE_GALLERY_OUTLINED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            else:
                time_now_9.bgcolor = '#ffcc66'
                time_now_9.content = ft.Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            nine,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
            page.update()
            print("Nine found!")

        result_ten = main_database.get(f"{cherg}").get(f"{day_num_ten}")
        if result_ten == None:
            page.client_storage.remove("ten")
            time_now_10.visible = False
            print("Ten not found!")
        else:
            page.client_storage.set("ten", result_ten)
            ten_check = page.client_storage.get("ten")
            start_time, end_time = ten_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                ten = f'{start_time}-24:00'
            else:
                ten = page.client_storage.get("four")
            time_now_10.visible = True
            if time_end <= current_time:
                time_now_10.bgcolor = ft.colors.GREY_400
                time_now_10.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            ten,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.DONE_ALL_ROUNDED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            elif time_start <= current_time <= time_end:
                time_now_10.bgcolor = '#ffcc66'
                time_now_10.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            ten,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.BROWSE_GALLERY_OUTLINED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            else:
                time_now_10.bgcolor = '#ffcc66'
                time_now_10.content = ft.Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            ten,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
            page.update()
            print("Ten found!")

        result_eleven = main_database.get(f"{cherg}").get(f"{day_num_eleven}")
        if result_eleven == None:
            page.client_storage.remove("eleven")
            time_now_11.visible = False
            print("Eleven not found!")
        else:
            page.client_storage.set("eleven", result_eleven)
            eleven_check = page.client_storage.get("eleven")
            start_time, end_time = eleven_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                eleven = f'{start_time}-24:00'
            else:
                eleven = page.client_storage.get("five")
            time_now_11.visible = True
            if time_end <= current_time:
                time_now_11.bgcolor = ft.colors.GREY_400
                time_now_11.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            eleven,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.DONE_ALL_ROUNDED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            elif time_start <= current_time <= time_end:
                time_now_11.bgcolor = '#ffcc66'
                time_now_11.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            eleven,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.BROWSE_GALLERY_OUTLINED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            else:
                time_now_11.bgcolor = '#ffcc66'
                time_now_11.content = ft.Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            eleven,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
            page.update()
            print("Eleven found!")

        result_twelve = main_database.get(f"{cherg}").get(f"{day_num_twelve}")
        if result_twelve == None:
            page.client_storage.remove("twelve")
            time_now_12.visible = False
            print("Twelve not found!")
        else:
            page.client_storage.set("twelve", result_twelve)
            twelve_check = page.client_storage.get("twelve")
            start_time, end_time = twelve_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                twelve = f'{start_time}-24:00'
            else:
                twelve = page.client_storage.get("six")
            time_now_12.visible = True
            if time_end <= current_time:
                time_now_12.bgcolor = ft.colors.GREY_400
                time_now_12.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            twelve,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.DONE_ALL_ROUNDED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            elif time_start <= current_time <= time_end:
                time_now_12.bgcolor = '#ffcc66'
                time_now_12.content = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(width=25),
                        ft.Text(
                            twelve,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        ),
                        ft.Icon(
                            name=ft.icons.BROWSE_GALLERY_OUTLINED,
                            color=ft.colors.BLACK
                        )
                    ]
                )
            else:
                time_now_12.bgcolor = '#ffcc66'
                time_now_12.content = ft.Row(
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            twelve,
                            size=21,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
            page.update()
            print("Twelve found!")

        progress_bar.visible = False
        main_info.padding = 0
        main_info.expand = True
        main_tab.visible = True
        time_now.visible = True
        time_tomorrow.visible = True
        time_after_tomorrow.visible = True
        main_tab_anim()
        try:
            if check_time_interval(one_check) == True:
                print("One time check is True!")
            elif check_time_interval(two_check) == True:
                print("Two time check is True!")
            elif check_time_interval(three_check) == True:
                print("Three time check is True!")
            elif check_time_interval(four_check) == True:
                print("Four time check is True!")
            elif check_time_interval(five_check) == True:
                print("Five time check is True!")
            elif check_time_interval(six_check) == True:
                print("Six time check is True!")
        except:
            print("All time check is False!")
        page.update()
        get_time_tomorrow()
        get_time_after_tomorrow()

    def storage():
        storage = page.client_storage.get("number")
        return storage

    def check_time_interval(time_interval):
        current_time = datetime.now().time()
        start_time_str, end_time_str = time_interval.split('-')

        start_time = datetime.strptime(start_time_str, '%H:%M').time()
        end_time = datetime.strptime(end_time_str, '%H:%M').time()

        if start_time <= current_time <= end_time:
            lamp_img.content = ft.Image(
                src=f"/Images/lamp_off.png",
                gapless_playback=True,
                height=280,
                width=280,
            )
            lamp_img.update()
            return True
        else:
            lamp_img.content = ft.Image(
                src=f"/Images/lamp_on.png",
                gapless_playback=True,
                height=280,
                width=280,
            )
            lamp_img.update()
            return False

    def alert_conn_start():
        time = page.client_storage.get('time')
        alert_conn.content = ft.Text(
            f"Немає доступу до Інтернету. Останнє оновлення: {time}",
            size=16,
            color='black',
            text_align='center',
            font_family="Golos Text",
            weight="w500",
        )
        alert_conn.open = True
        page.update()

    def alert_conn_first():
        alert_first_conn.open = True
        page.update()

    def get_time_tomorrow():
        storage_info = storage()
        cherg = check_cherg(storage_info)
        main_database = page.client_storage.get("main_database")
        if page.client_storage.get("database_storage") == 1:
            day_tomorrow_one = db1_day_tomorrow_one
            day_tomorrow_two = db1_day_tomorrow_two
            day_tomorrow_three = db1_day_tomorrow_three
            day_tomorrow_four = db1_day_tomorrow_four
            day_tomorrow_five = db1_day_tomorrow_five
            day_tomorrow_six = db1_day_tomorrow_six
            day_tomorrow_seven = db1_day_tomorrow_seven
            day_tomorrow_eight = db1_day_tomorrow_eight
            day_tomorrow_nine = db1_day_tomorrow_nine
            day_tomorrow_ten = db1_day_tomorrow_ten
            day_tomorrow_eleven = db1_day_tomorrow_eleven
            day_tomorrow_twelve = db1_day_tomorrow_twelve
        if page.client_storage.get("database_storage") == 2:
            day_tomorrow_one = db2_day_tomorrow_one
            day_tomorrow_two = db2_day_tomorrow_two
            day_tomorrow_three = db2_day_tomorrow_three
            day_tomorrow_four = db2_day_tomorrow_four
            day_tomorrow_five = db2_day_tomorrow_five
            day_tomorrow_six = db2_day_tomorrow_six
            day_tomorrow_seven = db2_day_tomorrow_seven
            day_tomorrow_eight = db2_day_tomorrow_eight
            day_tomorrow_nine = db2_day_tomorrow_nine
            day_tomorrow_ten = db2_day_tomorrow_ten
            day_tomorrow_eleven = db2_day_tomorrow_eleven
            day_tomorrow_twelve = db2_day_tomorrow_twelve

        result_one = main_database.get(f"{cherg}").get(f"{day_tomorrow_one}")
        if result_one == None:
            page.client_storage.remove("one_tomorrow")
            time_tomorrow_1.visible = False
            print("One_Tomorrow not found!")
        else:
            page.client_storage.set("one_tomorrow", result_one)
            one_check = page.client_storage.get("one_tomorrow")
            try:
                start_time, end_time = one_check.split('-')
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = page.client_storage.get("one_tomorrow")
                time_tomorrow_1.visible = True
                time_tomorrow_1.content = ft.Text(
                    one,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
                page.update()
                print("One_Tomorrow found!")
            except:
                one = page.client_storage.get("one_tomorrow")
                time_tomorrow_1.visible = True
                time_tomorrow_1.content = ft.Row(
                    wrap=True,
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            one,
                            text_align='center',
                            size=18,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("Connection is not forecast!")

        result_two = main_database.get(f"{cherg}").get(f"{day_tomorrow_two}")
        if result_two == None:
            page.client_storage.remove("two_tomorrow")
            time_tomorrow_2.visible = False
            print("Two_Tomorrow not found!")
        else:
            page.client_storage.set("two_tomorrow", result_two)
            two_check = page.client_storage.get("two_tomorrow")
            start_time, end_time = two_check.split('-')
            if end_time == '23:59':
                two = f'{start_time}-24:00'
            else:
                two = page.client_storage.get("two_tomorrow")
            time_tomorrow_2.visible = True
            time_tomorrow_2.content = ft.Text(
                two,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Two_Tomorrow found!")

        result_three = main_database.get(
            f"{cherg}").get(f"{day_tomorrow_three}")
        if result_three == None:
            page.client_storage.remove("three_tomorrow")
            time_tomorrow_3.visible = False
            print("Three_Tomorrow not found!")
        else:
            page.client_storage.set("three_tomorrow", result_three)
            three_check = page.client_storage.get("three_tomorrow")
            start_time, end_time = three_check.split('-')
            if end_time == '23:59':
                three = f'{start_time}-24:00'
            else:
                three = page.client_storage.get("three_tomorrow")
            time_tomorrow_3.visible = True
            time_tomorrow_3.content = ft.Text(
                three,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Three_Tomorrow found!")

        result_four = main_database.get(f"{cherg}").get(f"{day_tomorrow_four}")
        if result_four == None:
            page.client_storage.remove("four_tomorrow")
            time_tomorrow_4.visible = False
            print("Four_Tomorrow not found!")
        else:
            page.client_storage.set("four_tomorrow", result_four)
            four_check = page.client_storage.get("four_tomorrow")
            start_time, end_time = four_check.split('-')
            if end_time == '23:59':
                four = f'{start_time}-24:00'
            else:
                four = page.client_storage.get("four_tomorrow")
            time_tomorrow_4.visible = True
            time_tomorrow_4.content = ft.Text(
                four,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Four_Tomorrow found!")

        result_five = main_database.get(f"{cherg}").get(f"{day_tomorrow_five}")
        if result_five == None:
            page.client_storage.remove("five_tomorrow")
            time_tomorrow_5.visible = False
            print("Five_Tomorrow not found!")
        else:
            page.client_storage.set("five_tomorrow", result_five)
            five_check = page.client_storage.get("five_tomorrow")
            start_time, end_time = five_check.split('-')
            if end_time == '23:59':
                five = f'{start_time}-24:00'
            else:
                five = page.client_storage.get("five_tomorrow")
            time_tomorrow_5.visible = True
            time_tomorrow_5.content = ft.Text(
                five,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Five_Tomorrow found!")

            result_six = main_database.get(
                f"{cherg}").get(f"{day_tomorrow_six}")
            if result_six == None:
                page.client_storage.remove("six_tomorrow")
                time_tomorrow_6.visible = False
                print("Six_Tomorrow not found!")
            else:
                page.client_storage.set("six_tomorrow", result_six)
                six_check = page.client_storage.get("six_tomorrow")
                start_time, end_time = six_check.split('-')
                if end_time == '23:59':
                    six = f'{start_time}-24:00'
                else:
                    six = page.client_storage.get("six_tomorrow")
                time_tomorrow_6.visible = True
                time_tomorrow_6.content = ft.Text(
                    six,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
                page.update()
                print("Six_Tomorrow found!")

        result_seven = main_database.get(
            f"{cherg}").get(f"{day_tomorrow_seven}")
        if result_seven == None:
            page.client_storage.remove("seven_tomorrow")
            time_tomorrow_7.visible = False
            print("Seven_Tomorrow not found!")
        else:
            page.client_storage.set("seven_tomorrow", result_seven)
            seven_check = page.client_storage.get("seven_tomorrow")
            start_time, end_time = seven_check.split('-')
            if end_time == '23:59':
                seven = f'{start_time}-24:00'
            else:
                seven = page.client_storage.get("seven_tomorrow")
            time_tomorrow_7.visible = True
            time_tomorrow_7.content = ft.Text(
                seven,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Seven_Tomorrow found!")

        result_eight = main_database.get(
            f"{cherg}").get(f"{day_tomorrow_eight}")
        if result_eight == None:
            page.client_storage.remove("eight_tomorrow")
            time_tomorrow_8.visible = False
            print("Eight_Tomorrow not found!")
        else:
            page.client_storage.set("eight_tomorrow", result_eight)
            eight_check = page.client_storage.get("eight_tomorrow")
            start_time, end_time = eight_check.split('-')
            if end_time == '23:59':
                eight = f'{start_time}-24:00'
            else:
                eight = page.client_storage.get("eight_tomorrow")
            time_tomorrow_8.visible = True
            time_tomorrow_8.content = ft.Text(
                eight,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Eight_Tomorrow found!")

        result_nine = main_database.get(f"{cherg}").get(f"{day_tomorrow_nine}")
        if result_nine == None:
            page.client_storage.remove("nine_tomorrow")
            time_tomorrow_9.visible = False
            print("Nine_Tomorrow not found!")
        else:
            page.client_storage.set("nine_tomorrow", result_nine)
            nine_check = page.client_storage.get("nine_tomorrow")
            start_time, end_time = nine_check.split('-')
            if end_time == '23:59':
                nine = f'{start_time}-24:00'
            else:
                nine = page.client_storage.get("nine_tomorrow")
            time_tomorrow_9.visible = True
            time_tomorrow_9.content = ft.Text(
                nine,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Nine_Tomorrow found!")

        result_ten = main_database.get(f"{cherg}").get(f"{day_tomorrow_ten}")
        if result_ten == None:
            page.client_storage.remove("ten_tomorrow")
            time_tomorrow_10.visible = False
            print("Ten_Tomorrow not found!")
        else:
            page.client_storage.set("ten_tomorrow", result_ten)
            ten_check = page.client_storage.get("ten_tomorrow")
            start_time, end_time = ten_check.split('-')
            if end_time == '23:59':
                ten = f'{start_time}-24:00'
            else:
                ten = page.client_storage.get("ten_tomorrow")
            time_tomorrow_10.visible = True
            time_tomorrow_10.content = ft.Text(
                ten,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Ten_Tomorrow found!")

        result_eleven = main_database.get(
            f"{cherg}").get(f"{day_tomorrow_eleven}")
        if result_eleven == None:
            page.client_storage.remove("eleven_tomorrow")
            time_tomorrow_11.visible = False
            print("Eleven_Tomorrow not found!")
        else:
            page.client_storage.set("eleven_tomorrow", result_eleven)
            eleven_check = page.client_storage.get("eleven_tomorrow")
            start_time, end_time = eleven_check.split('-')
            if end_time == '23:59':
                eleven = f'{start_time}-24:00'
            else:
                eleven = page.client_storage.get("eleven_tomorrow")
            time_tomorrow_11.visible = True
            time_tomorrow_11.content = ft.Text(
                eleven,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Eleven_Tomorrow found!")

            result_twelve = main_database.get(
                f"{cherg}").get(f"{day_tomorrow_twelve}")
            if result_twelve == None:
                page.client_storage.remove("twelve_tomorrow")
                time_tomorrow_12.visible = False
                print("Twelve_Tomorrow not found!")
            else:
                page.client_storage.set("twelve_tomorrow", result_twelve)
                twelve_check = page.client_storage.get("twelve_tomorrow")
                start_time, end_time = twelve_check.split('-')
                if end_time == '23:59':
                    twelve = f'{start_time}-24:00'
                else:
                    twelve = page.client_storage.get("twelve_tomorrow")
                time_tomorrow_12.visible = True
                time_tomorrow_12.content = ft.Text(
                    twelve,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
                page.update()
                print("Twelve_Tomorrow found!")

        page.update()

    def get_time_after_tomorrow():
        storage_info = storage()
        cherg = check_cherg(storage_info)
        main_database = page.client_storage.get("main_database")
        if page.client_storage.get("database_storage") == 1:
            day_after_tomorrow_one = db1_day_after_tomorrow_one
            day_after_tomorrow_two = db1_day_after_tomorrow_two
            day_after_tomorrow_three = db1_day_after_tomorrow_three
            day_after_tomorrow_four = db1_day_after_tomorrow_four
            day_after_tomorrow_five = db1_day_after_tomorrow_five
            day_after_tomorrow_six = db1_day_after_tomorrow_six
            day_after_tomorrow_seven = db1_day_after_tomorrow_seven
            day_after_tomorrow_eight = db1_day_after_tomorrow_eight
            day_after_tomorrow_nine = db1_day_after_tomorrow_nine
            day_after_tomorrow_ten = db1_day_after_tomorrow_ten
            day_after_tomorrow_eleven = db1_day_after_tomorrow_eleven
            day_after_tomorrow_twelve = db1_day_after_tomorrow_twelve
        if page.client_storage.get("database_storage") == 2:
            day_after_tomorrow_one = db2_day_after_tomorrow_one
            day_after_tomorrow_two = db2_day_after_tomorrow_two
            day_after_tomorrow_three = db2_day_after_tomorrow_three
            day_after_tomorrow_four = db2_day_after_tomorrow_four
            day_after_tomorrow_five = db2_day_after_tomorrow_five
            day_after_tomorrow_six = db2_day_after_tomorrow_six
            day_after_tomorrow_seven = db2_day_after_tomorrow_seven
            day_after_tomorrow_eight = db2_day_after_tomorrow_eight
            day_after_tomorrow_nine = db2_day_after_tomorrow_nine
            day_after_tomorrow_ten = db2_day_after_tomorrow_ten
            day_after_tomorrow_eleven = db2_day_after_tomorrow_eleven
            day_after_tomorrow_twelve = db2_day_after_tomorrow_twelve

        result_one = main_database.get(f"{cherg}").get(
            f"{day_after_tomorrow_one}")
        if result_one == None:
            page.client_storage.remove("one_after_tomorrow")
            time_after_tomorrow_1.visible = False
            print("One_After_Tomorrow not found!")
        else:
            page.client_storage.set("one_after_tomorrow", result_one)
            one_check = page.client_storage.get("one_after_tomorrow")
            try:
                start_time, end_time = one_check.split('-')
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = page.client_storage.get("one_after_tomorrow")
                time_after_tomorrow_1.visible = True
                time_after_tomorrow_1.content = ft.Text(
                    one,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
                page.update()
                print("One_After_Tomorrow found!")
            except:
                one = page.client_storage.get("one_after_tomorrow")
                time_after_tomorrow_1.visible = True
                time_after_tomorrow_1.content = ft.Row(
                    wrap=True,
                    alignment="center",
                    vertical_alignment='center',
                    controls=[
                        ft.Text(
                            one,
                            text_align='center',
                            size=18,
                            weight='w500',
                            color=ft.colors.BLACK,
                            font_family="Golos Text"
                        )
                    ]
                )
                page.update()
                print("Connection is not forecast!")

        result_two = main_database.get(f"{cherg}").get(
            f"{day_after_tomorrow_two}")
        if result_two == None:
            page.client_storage.remove("two_after_tomorrow")
            time_after_tomorrow_2.visible = False
            print("Two_After_Tomorrow not found!")
        else:
            page.client_storage.set("two_after_tomorrow", result_two)
            two_check = page.client_storage.get("two_after_tomorrow")
            start_time, end_time = two_check.split('-')
            if end_time == '23:59':
                two = f'{start_time}-24:00'
            else:
                two = page.client_storage.get("two_after_tomorrow")
            time_after_tomorrow_2.visible = True
            time_after_tomorrow_2.content = ft.Text(
                two,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Two_After_Tomorrow found!")

        result_three = main_database.get(f"{cherg}").get(
            f"{day_after_tomorrow_three}")
        if result_three == None:
            page.client_storage.remove("three_after_tomorrow")
            time_after_tomorrow_3.visible = False
            print("Three_After_Tomorrow not found!")
        else:
            page.client_storage.set("three_after_tomorrow", result_three)
            three_check = page.client_storage.get("three_after_tomorrow")
            start_time, end_time = three_check.split('-')
            if end_time == '23:59':
                three = f'{start_time}-24:00'
            else:
                three = page.client_storage.get("three_after_tomorrow")
            time_after_tomorrow_3.visible = True
            time_after_tomorrow_3.content = ft.Text(
                three,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Three_After_Tomorrow found!")

        result_four = main_database.get(f"{cherg}").get(
            f"{day_after_tomorrow_four}")
        if result_four == None:
            page.client_storage.remove("four_after_tomorrow")
            time_after_tomorrow_4.visible = False
            print("Four_After_Tomorrow not found!")
        else:
            page.client_storage.set("four_after_tomorrow", result_four)
            four_check = page.client_storage.get("four_after_tomorrow")
            start_time, end_time = four_check.split('-')
            if end_time == '23:59':
                four = f'{start_time}-24:00'
            else:
                four = page.client_storage.get("four_after_tomorrow")
            time_after_tomorrow_4.visible = True
            time_after_tomorrow_4.content = ft.Text(
                four,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Four_After_Tomorrow found!")

        result_five = main_database.get(f"{cherg}").get(
            f"{day_after_tomorrow_five}")
        if result_five == None:
            page.client_storage.remove("five_after_tomorrow")
            time_after_tomorrow_5.visible = False
            print("Five_After_Tomorrow not found!")
        else:
            page.client_storage.set("five_after_tomorrow", result_five)
            five_check = page.client_storage.get("five_after_tomorrow")
            start_time, end_time = five_check.split('-')
            if end_time == '23:59':
                five = f'{start_time}-24:00'
            else:
                five = page.client_storage.get("five_after_tomorrow")
            time_after_tomorrow_5.visible = True
            time_after_tomorrow_5.content = ft.Text(
                five,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Five_After_Tomorrow found!")

        result_six = main_database.get(f"{cherg}").get(
            f"{day_after_tomorrow_six}")
        if result_six == None:
            page.client_storage.remove("six_after_tomorrow")
            time_after_tomorrow_6.visible = False
            print("Six_After_Tomorrow not found!")
        else:
            page.client_storage.set("six_after_tomorrow", result_six)
            six_check = page.client_storage.get("six_after_tomorrow")
            start_time, end_time = six_check.split('-')
            if end_time == '23:59':
                six = f'{start_time}-24:00'
            else:
                six = page.client_storage.get("six_after_tomorrow")
            time_after_tomorrow_6.visible = True
            time_after_tomorrow_6.content = ft.Text(
                six,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Six_After_Tomorrow found!")

        result_seven = main_database.get(f"{cherg}").get(
            f"{day_after_tomorrow_seven}")
        if result_seven == None:
            page.client_storage.remove("seven_after_tomorrow")
            time_after_tomorrow_7.visible = False
            print("Seven_After_Tomorrow not found!")
        else:
            page.client_storage.set("seven_after_tomorrow", result_seven)
            seven_check = page.client_storage.get("seven_after_tomorrow")
            start_time, end_time = seven_check.split('-')
            if end_time == '23:59':
                seven = f'{start_time}-24:00'
            else:
                seven = page.client_storage.get("seven_after_tomorrow")
            time_after_tomorrow_7.visible = True
            time_after_tomorrow_7.content = ft.Text(
                seven,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Seven_After_Tomorrow found!")

        result_eight = main_database.get(f"{cherg}").get(
            f"{day_after_tomorrow_eight}")
        if result_eight == None:
            page.client_storage.remove("eight_after_tomorrow")
            time_after_tomorrow_8.visible = False
            print("Eight_After_Tomorrow not found!")
        else:
            page.client_storage.set("eight_after_tomorrow", result_eight)
            eight_check = page.client_storage.get("eight_after_tomorrow")
            start_time, end_time = eight_check.split('-')
            if end_time == '23:59':
                eight = f'{start_time}-24:00'
            else:
                eight = page.client_storage.get("eight_after_tomorrow")
            time_after_tomorrow_8.visible = True
            time_after_tomorrow_8.content = ft.Text(
                eight,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Eight_After_Tomorrow found!")

        result_nine = main_database.get(f"{cherg}").get(
            f"{day_after_tomorrow_nine}")
        if result_nine == None:
            page.client_storage.remove("nine_after_tomorrow")
            time_after_tomorrow_9.visible = False
            print("Nine_After_Tomorrow not found!")
        else:
            page.client_storage.set("nine_after_tomorrow", result_nine)
            nine_check = page.client_storage.get("nine_after_tomorrow")
            start_time, end_time = nine_check.split('-')
            if end_time == '23:59':
                nine = f'{start_time}-24:00'
            else:
                nine = page.client_storage.get("nine_after_tomorrow")
            time_after_tomorrow_9.visible = True
            time_after_tomorrow_9.content = ft.Text(
                nine,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Nine_After_Tomorrow found!")

        result_ten = main_database.get(f"{cherg}").get(
            f"{day_after_tomorrow_ten}")
        if result_ten == None:
            page.client_storage.remove("ten_after_tomorrow")
            time_after_tomorrow_10.visible = False
            print("Ten_After_Tomorrow not found!")
        else:
            page.client_storage.set("ten_after_tomorrow", result_ten)
            ten_check = page.client_storage.get("ten_after_tomorrow")
            start_time, end_time = ten_check.split('-')
            if end_time == '23:59':
                ten = f'{start_time}-24:00'
            else:
                ten = page.client_storage.get("ten_after_tomorrow")
            time_after_tomorrow_10.visible = True
            time_after_tomorrow_10.content = ft.Text(
                ten,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Ten_After_Tomorrow found!")

        result_eleven = main_database.get(f"{cherg}").get(
            f"{day_after_tomorrow_eleven}")
        if result_eleven == None:
            page.client_storage.remove("eleven_after_tomorrow")
            time_after_tomorrow_11.visible = False
            print("Eleven_After_Tomorrow not found!")
        else:
            page.client_storage.set("eleven_after_tomorrow", result_eleven)
            eleven_check = page.client_storage.get("eleven_after_tomorrow")
            start_time, end_time = eleven_check.split('-')
            if end_time == '23:59':
                eleven = f'{start_time}-24:00'
            else:
                eleven = page.client_storage.get("eleven_after_tomorrow")
            time_after_tomorrow_11.visible = True
            time_after_tomorrow_11.content = ft.Text(
                eleven,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Eleven_After_Tomorrow found!")

        result_twelve = main_database.get(f"{cherg}").get(
            f"{day_after_tomorrow_twelve}")
        if result_twelve == None:
            page.client_storage.remove("twelve_after_tomorrow")
            time_after_tomorrow_12.visible = False
            print("Twelve_After_Tomorrow not found!")
        else:
            page.client_storage.set("twelve_after_tomorrow", result_twelve)
            twelve_check = page.client_storage.get("twelve_after_tomorrow")
            start_time, end_time = twelve_check.split('-')
            if end_time == '23:59':
                twelve = f'{start_time}-24:00'
            else:
                twelve = page.client_storage.get("twelve_after_tomorrow")
            time_after_tomorrow_12.visible = True
            time_after_tomorrow_12.content = ft.Text(
                twelve,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Twelve_After_Tomorrow found!")

        page.update()

    def main_tab_anim():
        main_info.expand = True
        main_info.content = ft.Column(
            controls=[
                main_tab
            ]
        )
        page.update()

    def refresh():
        current_time = datetime.now().strftime("%H:%M")
        refresh_bar.content = ft.Text(
            f"Оновлено о {current_time}",
            size=18,
            color='black',
            text_align='center',
            font_family="Golos Text",
            weight="w500",
        )
        refresh_bar.open = True
        page.update()

    def open_telegram(e):
        page.launch_url('https://t.me/sumy_svitlo',
                        web_window_name='Telegram')
        telegram_banner.open = False
        page.client_storage.set('telegram_check', True)
        page.update()

    def close_bunner(e):
        telegram_banner.open = False
        page.client_storage.set('telegram_check', False)
        day_close = str(seven_days)
        print(day_close)
        page.client_storage.set('day_close', day_close)
        page.update()

    telegram_banner = ft.Banner(
        elevation=5,
        bgcolor='#ffcc66',
        surface_tint_color=ft.colors.BACKGROUND,
        leading=ft.Image(
            src=f"/Images/telegram.svg",
            height=40,
            width=40,),
        content=ft.Text(
            value="Запрошуємо в наш телеграм канал - Світло Суми!",
            size=18,
            weight='w500',
            color=ft.colors.BLACK,
            font_family="Golos Text",
        ),
        actions=[
            ft.TextButton(text="Перейти", style=ft.ButtonStyle(
                color=ft.colors.BLACK), on_click=open_telegram),
            ft.TextButton(text="Закрити", style=ft.ButtonStyle(
                color=ft.colors.BLACK), on_click=close_bunner)
        ]
    )

    alert_conn = ft.SnackBar(
        behavior=ft.SnackBarBehavior.FLOATING,
        elevation=15,
        duration=5000,
        bgcolor='#ffcc66',
        content=ft.Text(
            size=16,
            color='black',
            text_align='center',
            font_family="Golos Text",
            weight="w500",
        )
    )

    alert_first_conn = ft.SnackBar(
        behavior=ft.SnackBarBehavior.FLOATING,
        elevation=15,
        duration=5000,
        bgcolor='#ffcc66',
        content=ft.Text(
            "Немає доступу до Інтернету. Для оновлення інформації потрібне підключення до Інтернету!",
            size=16,
            color='black',
            text_align='center',
            font_family="Golos Text",
            weight="w500",
        )
    )

    refresh_bar = ft.SnackBar(
        behavior=ft.SnackBarBehavior.FLOATING,
        elevation=15,
        duration=3000,
        bgcolor='#ffcc66',
        content=ft.Text(
            # f"Оновлено о ",
            size=18,
            color='black',
            text_align='center',
            font_family="Golos Text",
            weight="w500",
        )
    )

    progress_bar = ft.ProgressBar(
        visible=True,
        bgcolor="white",
        color="#ffcc66",
        bar_height=5,
    )

    time_now = ft.Container(
        alignment=ft.alignment.center,
        padding=10,
        content=ft.Column(
            scroll=ft.ScrollMode.ADAPTIVE,
            alignment='center',
            horizontal_alignment='center',
            spacing=9,
            controls=[
                time_now_1,
                time_now_2,
                time_now_3,
                time_now_4,
                time_now_5,
                time_now_6,
                time_now_7,
                time_now_8,
                time_now_9,
                time_now_10,
                time_now_11,
                time_now_12
            ]
        )
    )

    time_tomorrow = ft.Container(
        alignment=ft.alignment.center,
        padding=10,
        content=ft.Column(
            scroll=ft.ScrollMode.ADAPTIVE,
            alignment='center',
            horizontal_alignment='center',
            spacing=9,
            controls=[
                time_tomorrow_1,
                time_tomorrow_2,
                time_tomorrow_3,
                time_tomorrow_4,
                time_tomorrow_5,
                time_tomorrow_6,
                time_tomorrow_7,
                time_tomorrow_8,
                time_tomorrow_9,
                time_tomorrow_10,
                time_tomorrow_11,
                time_tomorrow_12
            ]
        )
    )

    time_after_tomorrow = ft.Container(
        alignment=ft.alignment.center,
        padding=10,
        content=ft.Column(
            scroll=ft.ScrollMode.ADAPTIVE,
            alignment='center',
            horizontal_alignment='center',
            spacing=9,
            controls=[
                time_after_tomorrow_1,
                time_after_tomorrow_2,
                time_after_tomorrow_3,
                time_after_tomorrow_4,
                time_after_tomorrow_5,
                time_after_tomorrow_6,
                time_after_tomorrow_7,
                time_after_tomorrow_8,
                time_after_tomorrow_9,
                time_after_tomorrow_10,
                time_after_tomorrow_11,
                time_after_tomorrow_12
            ]
        )
    )

    one_button = ft.ElevatedButton(content=ft.Text("Перша", size=22, weight='w500', font_family="Golos Text"),
                                   style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15), overlay_color=ft.colors.AMBER_200), width=250, height=50,
                                   color=ft.colors.BLACK, bgcolor='#ffcc66', on_click=cherg_choise, data=1)

    two_button = ft.ElevatedButton(content=ft.Text("Друга", size=22, weight='w500', font_family="Golos Text"),
                                   style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15), overlay_color=ft.colors.AMBER_200), width=250, height=50,
                                   color=ft.colors.BLACK, bgcolor='#ffcc66', on_click=cherg_choise, data=2)

    three_button = ft.ElevatedButton(content=ft.Text("Третя", size=22, weight='w500', font_family="Golos Text"),
                                     style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15), overlay_color=ft.colors.AMBER_200), width=250, height=50,
                                     color=ft.colors.BLACK, bgcolor='#ffcc66', on_click=cherg_choise, data=3)

    four_button = ft.ElevatedButton(content=ft.Text("Четверта", size=22, weight='w500', font_family="Golos Text"),
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15), overlay_color=ft.colors.AMBER_200), width=250, height=50,
                                    color=ft.colors.BLACK, bgcolor='#ffcc66', on_click=cherg_choise, data=4)

    five_button = ft.ElevatedButton(content=ft.Text("П'ята", size=22, weight='w500', font_family="Golos Text"),
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15), overlay_color=ft.colors.AMBER_200), width=250, height=50,
                                    color=ft.colors.BLACK, bgcolor='#ffcc66', on_click=cherg_choise, data=5)

    six_button = ft.ElevatedButton(content=ft.Text("Шоста", size=22, weight='w500', font_family="Golos Text"),
                                   style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15), overlay_color=ft.colors.AMBER_200), width=250, height=50,
                                   color=ft.colors.BLACK, bgcolor='#ffcc66', on_click=cherg_choise, data=6)

    bs = ft.BottomSheet(
        content=ft.Column(
            horizontal_alignment='center',
            alignment='end',
            height=380,
            width=400,
            spacing=5,
            controls=[
                ft.Text(
                    "Оберіть чергу:",
                    size=20,
                    weight='w500',
                    text_align='center',
                    font_family="Golos Text"
                ),
                one_button,
                two_button,
                three_button,
                four_button,
                five_button,
                six_button,
                ft.Container(height=10),
            ]
        ),
        bgcolor=ft.colors.WHITE,
    )

    lamp_img = ft.SafeArea(
        ft.Container(
            content=ft.Image(
                src=f"/Images/lamp_on.png",
                gapless_playback=True,
                height=280,
                width=280,
            )
        )
    )

    text_after_img = ft.Container(
        blur=10,
        padding=5,
        bgcolor=ft.colors.BLACK26,
        border_radius=15,
        width=250,
        content=ft.Text(
            # f"{storage()} черга",
            size=24,
            weight='w500',
            color='#ffcc66',
            font_family="Golos Text",
            text_align='center'
        )
    )

    main_tab = ft.Tabs(
        visible=False,
        tab_alignment=ft.TabAlignment.CENTER,
        divider_color=ft.colors.BLACK26,
        animation_duration=300,
        scrollable=True,
        indicator_color='#ffcc66',
        label_color='#ffcc66',
        unselected_label_color=ft.colors.BLACK87,
        selected_index=0,
        tabs=[
            ft.Tab(
                tab_content=ft.Text(
                    day_of_week_today,
                    size=18,
                    text_align='center',
                    font_family="Golos Text",
                    weight="w500"
                ),
                content=time_now
            ),
            ft.Tab(
                tab_content=ft.Text(
                    day_of_week_tomorrow,
                    size=18,
                    text_align='center',
                    font_family="Golos Text",
                    weight="w500"
                ),
                content=time_tomorrow
            ),
            ft.Tab(
                tab_content=ft.Text(
                    day_of_week_after_tomorrow,
                    size=18,
                    text_align='center',
                    font_family="Golos Text",
                    weight="w500"
                ),
                content=time_after_tomorrow
            )
        ],
        expand=True
    )

    main_info = ft.Container(
        blur=10,
        padding=15,
        bgcolor=ft.colors.BLACK26,
        border_radius=15,
        content=ft.Column(
            horizontal_alignment='center',
            alignment="center",
            controls=[
                progress_bar,
            ]
        )
    )

    info_tab = ft.SafeArea(
        ft.Container(
            blur=10,
            bgcolor=ft.colors.BLACK12,
            border_radius=15,
            padding=15,
            alignment=ft.alignment.center,
            content=ft.Column(
                scroll=ft.ScrollMode.ADAPTIVE,
                horizontal_alignment='center',
                alignment='start',
                controls=[
                    ft.Text(
                        'Інформація',
                        size=30,
                        color=ft.colors.BLACK87,
                        weight="w400",
                        font_family="Golos Text",
                        text_align="center"
                    ),
                    ft.Divider(height=0.1, color=ft.colors.BLACK26),
                    ft.Text(
                        "Розроблено для безплатного користування.",
                        size=16,
                        color='black',
                        text_align='center',
                        font_family="Golos Text",
                        weight="w500"
                    ),
                    ft.Divider(height=0.1, color=ft.colors.BLACK26),
                    ft.Text(
                        "Застосунок використовує актуальні графіки відключень світла з сайту Сумиобленерго.",
                        size=16,
                        color='black',
                        text_align='center',
                        font_family="Golos Text",
                        weight="w500"
                    ),
                    ft.Divider(height=0.1, color=ft.colors.BLACK26),
                    ft.Text(
                        "В застосунку немає та не буде жодної реклами. Якщо ви хочете підтримати розробника - нижче залишу банку монобанку.",
                        size=16,
                        color='black',
                        text_align='center',
                        font_family="Golos Text",
                        weight="w500"
                    ),
                    ft.Divider(height=0.1, color=ft.colors.BLACK26),
                    ft.ElevatedButton(
                        content=ft.Container(
                            # padding=10,
                            content=ft.Row(
                                alignment='center',
                                vertical_alignment='center',
                                spacing=3,
                                wrap=True,
                                expand=True,
                                controls=[
                                    ft.Image(
                                        src=f"/Images/telegram.svg",
                                        height=40,
                                        width=40,
                                    ),
                                    ft.Text(
                                        "Світло Суми",
                                        size=18,
                                        color='black',
                                        text_align='center',
                                        font_family="Golos Text",
                                        weight="w500"
                                    )
                                ]
                            )
                        ),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=15),
                            overlay_color=ft.colors.AMBER_200),
                        # height=50,
                        color=ft.colors.BLACK,
                        bgcolor='#ffcc66',
                        on_click=open_telegram_channel
                    ),
                    ft.Divider(height=0.1, color=ft.colors.BLACK26),
                    ft.TextButton(
                        style=ft.ButtonStyle(
                            overlay_color=ft.colors.AMBER_200),
                        on_click=mono_click,
                        content=ft.Image(
                            src=f"/Images/monobanka.png",
                            height=100,
                            width=100,
                        )
                    ),
                    ft.Text(
                        "Підтримати розробника",
                        size=20,
                        color='black',
                        text_align='center',
                        font_family="Golos Text",
                        weight="w500"
                    ),
                    ft.Divider(height=0.1, color=ft.colors.BLACK26),
                    ft.ElevatedButton(
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=15),
                            overlay_color=ft.colors.AMBER_200),
                        color=ft.colors.BLACK,
                        bgcolor='#ffcc66',
                        on_click=telegram_click,
                        # width=300,
                        content=ft.Row(
                            alignment='center',
                            vertical_alignment='center',
                            spacing=3,
                            wrap=True,
                            expand=True,
                            controls=[
                                ft.Image(
                                    src=f"/Images/telegram.svg",
                                    height=40,
                                    width=40,
                                ),
                                ft.Text(
                                    "Написати розробнику",
                                    size=17,
                                    color='black',
                                    text_align='center',
                                    font_family="Golos Text",
                                    weight="w500"
                                )
                            ]
                        )
                    )
                ]
            )
        ),
        expand=True,
        visible=False
    )

    main_container = ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_right,
            end=ft.alignment.bottom_left,
            colors=['#ffcc66', '#ff6666']
        ),
        padding=15,
        content=ft.Column(
            horizontal_alignment='center',
            alignment='center',
            controls=[
                lamp_img,
                text_after_img,
                main_info,
                info_tab
            ]
        ),
        expand=True
    )

    page.fonts = {
        "Golos Text": "/fonts/GolosText.ttf"
    }
    page.title = 'Svitlo Sumy'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_height = 700
    page.window_width = 400
    page.padding = 0
    # page.window_center()
    page.window_resizable = True
    page.navigation_bar = ft.NavigationBar(
        surface_tint_color='#ff6666',
        indicator_color='#ffcc66',
        indicator_shape=ft.RoundedRectangleBorder(radius=10),
        height=65,
        on_change=on_tab,
        selected_index=1,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.LIST_ROUNDED, label='Черги',),
            ft.NavigationDestination(
                icon=ft.icons.HOME_ROUNDED, label='Головна'),
            ft.NavigationDestination(
                icon=ft.icons.INFO, selected_icon=ft.icons.INFO_OUTLINE, label='Інформація')
        ]
    )

    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.add(main_container)
    page.overlay.append(bs)
    page.overlay.append(alert_conn)
    page.overlay.append(alert_first_conn)
    page.overlay.append(refresh_bar)
    page.overlay.append(telegram_banner)
    # page.window_title_bar_hidden = True
    # page.window_title_bar_buttons_hidden = True
    page.update()
    check_storage()
    check_telegram()
    while True:
        time.sleep(60)
        try:
            main_info.expand = False
            main_info.padding = 15
            main_info.content = ft.Column(
                horizontal_alignment='center',
                alignment="center",
                controls=[
                    progress_bar
                ]
            )
            progress_bar.visible = True
            page.update()
            check_storage_refresh()
            print("Update Complete!")
        except:
            print("Update Not Complete!")


ft.app(
    target=main,
    name="Svitlo Sumy",
    assets_dir='assets',
)
