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
import urllib.request
import json
from firebase import firebase
import asyncio
import os


async def main(page: ft.Page):

    async def source_github():
        with urllib.request.urlopen("https://raw.githubusercontent.com/Aporial/Svitlo_Sumy/main/database/database.json") as url:
            main_database = json.load(url)
            source_check = main_database.get("source")
            if source_check == 'github':
                print('Source:', source_check)
                await page.client_storage.set_async("source", source_check)
                database = main_database.get("database")
                print('DATABASE:', database)
                update_time = main_database.get("update_time")
                print("Update time:", update_time)
                await page.client_storage.set_async("database_storage", database)
                await page.client_storage.set_async("main_database", main_database)
                await page.client_storage.set_async("update_time", update_time)
            if source_check == 'firebase':
                await source_firebase()

    async def source_firebase():
        database_connection = firebase.FirebaseApplication(
            'https://svitlo-sumy-default-rtdb.europe-west1.firebasedatabase.app/', authentication=None)
        main_database = database_connection.get("/", None)
        source_check = main_database.get("source")
        if source_check == 'firebase':
            print('Source:', source_check)
            await page.client_storage.set_async("source", source_check)
            database = main_database.get("database")
            print('DATABASE:', database)
            update_time = main_database.get("update_time")
            print("Update time:", update_time)
            await page.client_storage.set_async("database_storage", database)
            await page.client_storage.set_async("main_database", main_database)
            await page.client_storage.set_async("update_time", update_time)
        if source_check == 'github':
            await source_github()

    async def check_telegram():
        if await page.client_storage.get_async('telegram_check') == None:
            if await page.client_storage.get_async("number") == None:
                print('Queue has not yet been selected!')
            else:
                await asyncio.sleep(2)
                telegram_banner.open = True
                print("Telegram was not opened!")
        if await page.client_storage.get_async('telegram_check') == True:
            print("Telegram was opened!")
        if await page.client_storage.get_async('telegram_check') == False:
            if str(today) == await page.client_storage.get_async('day_close'):
                await asyncio.sleep(2)
                telegram_banner.open = True
                print('7 days have passed!')
        page.update()

    async def check_cherg_main():
        get_storage = await storage()
        if get_storage == None:
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
                f"{get_storage} черга",
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
            main.visible = True
            info_tab.visible = False
            options_tab.visible = False
            open_list()
        if my_index == 1:
            main.visible = True
            info_tab.visible = False
            options_tab.visible = False
            page.update()
        if my_index == 2:
            info_tab.visible = True
            main.visible = False
            options_tab.visible = False
            page.update()
        if my_index == 3:
            options_tab.visible = True
            info_tab.visible = False
            main.visible = False
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

    async def cherg_choise(e):
        numb_cherg = e.control.data
        await page.client_storage.set_async("number", numb_cherg)
        bs.open = False
        bs.update()
        await check_storage_main()

    async def check_storage():
        if await page.client_storage.get_async("number") == None:
            try:
                if await page.client_storage.get_async("source") == None:
                    try:
                        await source_github()
                    except:
                        await source_firebase()
                if await page.client_storage.get_async("source") == "github":
                    await source_github()
                if await page.client_storage.get_async("source") == "firebase":
                    await source_firebase()
                time = datetime.now().strftime("%d.%m.%Y о %H:%M:%S")
                await page.client_storage.set_async('time', time)
                await info_check()
                await check_cherg_main()
                open_list()
                update_time = await page.client_storage.get_async("update_time")
                grafic_refresh.content = ft.Text(
                    f"Графік оновлено о {update_time}",
                    weight='w400',
                    color=ft.colors.BLACK,
                    font_family="Golos Text",
                    height=18
                )
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
                if await page.client_storage.get_async("source") == None:
                    try:
                        await source_github()
                    except:
                        await source_firebase()
                if await page.client_storage.get_async("source") == "github":
                    await source_github()
                if await page.client_storage.get_async("source") == "firebase":
                    await source_firebase()
                time = datetime.now().strftime("%d.%m.%Y о %H:%M:%S")
                await page.client_storage.set_async('time', time)
                await info_check()
                await check_cherg_main()
                update_time = await page.client_storage.get_async("update_time")
                grafic_refresh.content = ft.Text(
                    f"Графік оновлено о {update_time}",
                    weight='w400',
                    color=ft.colors.BLACK,
                    font_family="Golos Text",
                    height=18
                )
                print('Connected!')
            except:
                await alert_conn_start()
                print("Fail connection!")
            await check_storage_main()

    async def check_storage_refresh():
        try:
            await check_cherg_main()
            if await page.client_storage.get_async("source") == None:
                try:
                    await source_github()
                except:
                    await source_firebase()
            if await page.client_storage.get_async("source") == "github":
                await source_github()
            if await page.client_storage.get_async("source") == "firebase":
                await source_firebase()
            time = datetime.now().strftime("%d.%m.%Y о %H:%M:%S")
            await page.client_storage.set_async('time', time)
            # refresh()
            print('Connected!')
        except:
            await alert_conn_start()
            print("Fail connection!")
        await check_storage_main()

    async def check_storage_main():
        await check_cherg_main()
        current_time = datetime.now().time()
        storage_info = await storage()
        cherg = check_cherg(storage_info)
        main_database = await page.client_storage.get_async("main_database")
        one_check = await page.client_storage.get_async("one")
        two_check = await page.client_storage.get_async("two")
        three_check = await page.client_storage.get_async("three")
        four_check = await page.client_storage.get_async("four")
        five_check = await page.client_storage.get_async("five")
        six_check = await page.client_storage.get_async("six")
        if await page.client_storage.get_async("database_storage") == 1:
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
        if await page.client_storage.get_async("database_storage") == 2:
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
            await page.client_storage.remove_async("one")
            time_now_1.visible = False
            print("One not found!")
        else:
            await page.client_storage.set_async("one", result_one)
            one_check = await page.client_storage.get_async("one")
            try:
                start_time, end_time = one_check.split('-')
                time_start = datetime.strptime(start_time, '%H:%M').time()
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = await page.client_storage.get_async("one")
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
                    time_now_1.bgcolor = '#ffa067'
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
                one = await page.client_storage.get_async("one")
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
            await page.client_storage.remove_async("two")
            time_now_2.visible = False
            print("Two not found!")
        else:
            await page.client_storage.set_async("two", result_two)
            two_check = await page.client_storage.get_async("two")
            start_time, end_time = two_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                two = f'{start_time}-24:00'
            else:
                two = await page.client_storage.get_async("two")
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
                time_now_2.bgcolor = '#ffa067'
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
            await page.client_storage.remove_async("three")
            time_now_3.visible = False
            print("Three not found!")
        else:
            await page.client_storage.set_async("three", result_three)
            three_check = await page.client_storage.get_async("three")
            start_time, end_time = three_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                three = f'{start_time}-24:00'
            else:
                three = await page.client_storage.get_async("three")
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
                time_now_3.bgcolor = '#ffa067'
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
            await page.client_storage.remove_async("four")
            time_now_4.visible = False
            print("Four not found!")
        else:
            await page.client_storage.set_async("four", result_four)
            four_check = await page.client_storage.get_async("four")
            start_time, end_time = four_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                four = f'{start_time}-24:00'
            else:
                four = await page.client_storage.get_async("four")
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
                time_now_4.bgcolor = '#ffa067'
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
            await page.client_storage.remove_async("five")
            time_now_5.visible = False
            print("Five not found!")
        else:
            await page.client_storage.set_async("five", result_five)
            five_check = await page.client_storage.get_async("five")
            start_time, end_time = five_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                five = f'{start_time}-24:00'
            else:
                five = await page.client_storage.get_async("five")
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
                time_now_5.bgcolor = '#ffa067'
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
            await page.client_storage.remove_async("six")
            time_now_6.visible = False
            print("Six not found!")
        else:
            await page.client_storage.set_async("six", result_six)
            six_check = await page.client_storage.get_async("six")
            start_time, end_time = six_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                six = f'{start_time}-24:00'
            else:
                six = await page.client_storage.get_async("six")
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
                time_now_6.bgcolor = '#ffa067'
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
            await page.client_storage.remove_async("seven")
            time_now_7.visible = False
            print("Seven not found!")
        else:
            await page.client_storage.set_async("seven", result_seven)
            seven_check = await page.client_storage.get_async("seven")
            start_time, end_time = seven_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                seven = f'{start_time}-24:00'
            else:
                seven = await page.client_storage.get_async("seven")
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
                time_now_7.bgcolor = '#ffa067'
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
            await page.client_storage.remove_async("eight")
            time_now_8.visible = False
            print("Eight not found!")
        else:
            await page.client_storage.set_async("eight", result_eight)
            eight_check = await page.client_storage.get_async("eight")
            start_time, end_time = eight_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                eight = f'{start_time}-24:00'
            else:
                eight = await page.client_storage.get_async("eight")
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
                time_now_8.bgcolor = '#ffa067'
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
            await page.client_storage.remove_async("nine")
            time_now_9.visible = False
            print("Nine not found!")
        else:
            await page.client_storage.set_async("nine", result_nine)
            nine_check = await page.client_storage.get_async("nine")
            start_time, end_time = nine_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                nine = f'{start_time}-24:00'
            else:
                nine = await page.client_storage.get_async("three")
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
                time_now_9.bgcolor = '#ffa067'
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
            await page.client_storage.remove_async("ten")
            time_now_10.visible = False
            print("Ten not found!")
        else:
            await page.client_storage.set_async("ten", result_ten)
            ten_check = await page.client_storage.get_async("ten")
            start_time, end_time = ten_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                ten = f'{start_time}-24:00'
            else:
                ten = await page.client_storage.get_async("four")
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
                time_now_10.bgcolor = '#ffa067'
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
            await page.client_storage.remove_async("eleven")
            time_now_11.visible = False
            print("Eleven not found!")
        else:
            await page.client_storage.set_async("eleven", result_eleven)
            eleven_check = await page.client_storage.get_async("eleven")
            start_time, end_time = eleven_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                eleven = f'{start_time}-24:00'
            else:
                eleven = await page.client_storage.get_async("five")
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
                time_now_11.bgcolor = '#ffa067'
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
            await page.client_storage.remove_async("twelve")
            time_now_12.visible = False
            print("Twelve not found!")
        else:
            await page.client_storage.set_async("twelve", result_twelve)
            twelve_check = await page.client_storage.get_async("twelve")
            start_time, end_time = twelve_check.split('-')
            time_start = datetime.strptime(start_time, '%H:%M').time()
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if end_time == '23:59':
                twelve = f'{start_time}-24:00'
            else:
                twelve = await page.client_storage.get_async("six")
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
                time_now_12.bgcolor = '#ffa067'
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
        main_tab.visible = True
        time_now.visible = True
        time_tomorrow.visible = True
        time_after_tomorrow.visible = True
        main_tab_anim()
        try:
            if await check_time_interval(one_check) == True:
                print("One time check is True!")
            elif await check_time_interval(two_check) == True:
                print("Two time check is True!")
            elif await check_time_interval(three_check) == True:
                print("Three time check is True!")
            elif await check_time_interval(four_check) == True:
                print("Four time check is True!")
            elif await check_time_interval(five_check) == True:
                print("Five time check is True!")
            elif await check_time_interval(six_check) == True:
                print("Six time check is True!")
        except:
            print("All time check is False!")
        page.update()
        await get_time_tomorrow()
        await get_time_after_tomorrow()

    async def storage():
        storage = await page.client_storage.get_async("number")
        return storage

    async def check_time_interval(time_interval):
        current_time = datetime.now().time()
        start_time_str, end_time_str = time_interval.split('-')

        start_time = datetime.strptime(start_time_str, '%H:%M').time()
        end_time = datetime.strptime(end_time_str, '%H:%M').time()

        if start_time <= current_time <= end_time:
            lamp_img.content = ft.SafeArea(
                content=ft.Image(
                    src=f"/Images/lamp_off.png",
                    # gapless_playback=True,
                )
            )
            lamp_img.update()
            if bg_switch.value == True:
                page.theme_mode = ft.ThemeMode.DARK
                main_container.gradient = ft.LinearGradient(
                    begin=ft.alignment.top_right,
                    end=ft.alignment.bottom_left,
                    colors=['#2b060b', '#ff6666']
                )
                page.navigation_bar.indicator_color = '#4d4d4d'
            if bg_switch.value == False:
                page.navigation_bar.indicator_color = '#ffcc66'
            page.update()
            return True
        else:
            lamp_img.content = ft.SafeArea(
                content=ft.Image(
                    src=f"/Images/lamp_on.png",
                    # gapless_playback=True,
                )
            )
            lamp_img.update()
            if bg_switch.value == True:
                page.theme_mode = ft.ThemeMode.LIGHT
                main_container.gradient = ft.LinearGradient(
                    begin=ft.alignment.top_right,
                    end=ft.alignment.bottom_left,
                    colors=['#ffcc66', '#ff6666']
                )
                page.navigation_bar.indicator_color = '#ffcc66'
            if bg_switch.value == False:
                page.navigation_bar.indicator_color = '#ffcc66'
            page.update()
            return False

    async def alert_conn_start():
        time = await page.client_storage.get_async('time')
        alert_conn.content = ft.Text(
            f"Немає доступу до Інтернету. Останнє оновлення: {time}",
            size=16,
            color='black',
            text_align='center',
            font_family="Golos Text",
            weight="w500",
        )
        update_time = await page.client_storage.get_async("update_time")
        grafic_refresh.content = ft.Text(
            f"Останнє оновлення графіку о {update_time}",
            weight='w400',
            color=ft.colors.BLACK,
            font_family="Golos Text",
            height=18
        )
        alert_conn.open = True
        page.update()

    def alert_conn_first():
        alert_first_conn.open = True
        grafic_refresh.content = ft.Text(
            "Не вдалось завантажити графік",
            weight='w400',
            color=ft.colors.BLACK,
            font_family="Golos Text",
            height=18
        )
        page.update()

    async def get_time_tomorrow():
        storage_info = await storage()
        cherg = check_cherg(storage_info)
        main_database = await page.client_storage.get_async("main_database")
        if await page.client_storage.get_async("database_storage") == 1:
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
        if await page.client_storage.get_async("database_storage") == 2:
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
            await page.client_storage.remove_async("one_tomorrow")
            time_tomorrow_1.visible = False
            print("One_Tomorrow not found!")
        else:
            await page.client_storage.set_async("one_tomorrow", result_one)
            one_check = await page.client_storage.get_async("one_tomorrow")
            try:
                start_time, end_time = one_check.split('-')
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = await page.client_storage.get_async("one_tomorrow")
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
                one = await page.client_storage.get_async("one_tomorrow")
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
            await page.client_storage.remove_async("two_tomorrow")
            time_tomorrow_2.visible = False
            print("Two_Tomorrow not found!")
        else:
            await page.client_storage.set_async("two_tomorrow", result_two)
            two_check = await page.client_storage.get_async("two_tomorrow")
            start_time, end_time = two_check.split('-')
            if end_time == '23:59':
                two = f'{start_time}-24:00'
            else:
                two = await page.client_storage.get_async("two_tomorrow")
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
            await page.client_storage.remove_async("three_tomorrow")
            time_tomorrow_3.visible = False
            print("Three_Tomorrow not found!")
        else:
            await page.client_storage.set_async("three_tomorrow", result_three)
            three_check = await page.client_storage.get_async("three_tomorrow")
            start_time, end_time = three_check.split('-')
            if end_time == '23:59':
                three = f'{start_time}-24:00'
            else:
                three = await page.client_storage.get_async("three_tomorrow")
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
            await page.client_storage.remove_async("four_tomorrow")
            time_tomorrow_4.visible = False
            print("Four_Tomorrow not found!")
        else:
            await page.client_storage.set_async("four_tomorrow", result_four)
            four_check = await page.client_storage.get_async("four_tomorrow")
            start_time, end_time = four_check.split('-')
            if end_time == '23:59':
                four = f'{start_time}-24:00'
            else:
                four = await page.client_storage.get_async("four_tomorrow")
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
            await page.client_storage.remove_async("five_tomorrow")
            time_tomorrow_5.visible = False
            print("Five_Tomorrow not found!")
        else:
            await page.client_storage.set_async("five_tomorrow", result_five)
            five_check = await page.client_storage.get_async("five_tomorrow")
            start_time, end_time = five_check.split('-')
            if end_time == '23:59':
                five = f'{start_time}-24:00'
            else:
                five = await page.client_storage.get_async("five_tomorrow")
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
                await page.client_storage.remove_async("six_tomorrow")
                time_tomorrow_6.visible = False
                print("Six_Tomorrow not found!")
            else:
                await page.client_storage.set_async("six_tomorrow", result_six)
                six_check = await page.client_storage.get_async("six_tomorrow")
                start_time, end_time = six_check.split('-')
                if end_time == '23:59':
                    six = f'{start_time}-24:00'
                else:
                    six = await page.client_storage.get_async("six_tomorrow")
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
            await page.client_storage.remove_async("seven_tomorrow")
            time_tomorrow_7.visible = False
            print("Seven_Tomorrow not found!")
        else:
            await page.client_storage.set_async("seven_tomorrow", result_seven)
            seven_check = await page.client_storage.get_async("seven_tomorrow")
            start_time, end_time = seven_check.split('-')
            if end_time == '23:59':
                seven = f'{start_time}-24:00'
            else:
                seven = await page.client_storage.get_async("seven_tomorrow")
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
            await page.client_storage.remove_async("eight_tomorrow")
            time_tomorrow_8.visible = False
            print("Eight_Tomorrow not found!")
        else:
            await page.client_storage.set_async("eight_tomorrow", result_eight)
            eight_check = await page.client_storage.get_async("eight_tomorrow")
            start_time, end_time = eight_check.split('-')
            if end_time == '23:59':
                eight = f'{start_time}-24:00'
            else:
                eight = await page.client_storage.get_async("eight_tomorrow")
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
            await page.client_storage.remove_async("nine_tomorrow")
            time_tomorrow_9.visible = False
            print("Nine_Tomorrow not found!")
        else:
            await page.client_storage.set_async("nine_tomorrow", result_nine)
            nine_check = await page.client_storage.get_async("nine_tomorrow")
            start_time, end_time = nine_check.split('-')
            if end_time == '23:59':
                nine = f'{start_time}-24:00'
            else:
                nine = await page.client_storage.get_async("nine_tomorrow")
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
            await page.client_storage.remove_async("ten_tomorrow")
            time_tomorrow_10.visible = False
            print("Ten_Tomorrow not found!")
        else:
            await page.client_storage.set_async("ten_tomorrow", result_ten)
            ten_check = await page.client_storage.get_async("ten_tomorrow")
            start_time, end_time = ten_check.split('-')
            if end_time == '23:59':
                ten = f'{start_time}-24:00'
            else:
                ten = await page.client_storage.get_async("ten_tomorrow")
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
            await page.client_storage.remove_async("eleven_tomorrow")
            time_tomorrow_11.visible = False
            print("Eleven_Tomorrow not found!")
        else:
            await page.client_storage.set_async("eleven_tomorrow", result_eleven)
            eleven_check = await page.client_storage.get_async("eleven_tomorrow")
            start_time, end_time = eleven_check.split('-')
            if end_time == '23:59':
                eleven = f'{start_time}-24:00'
            else:
                eleven = await page.client_storage.get_async("eleven_tomorrow")
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
                await page.client_storage.remove_async("twelve_tomorrow")
                time_tomorrow_12.visible = False
                print("Twelve_Tomorrow not found!")
            else:
                await page.client_storage.set_async("twelve_tomorrow", result_twelve)
                twelve_check = await page.client_storage.get_async("twelve_tomorrow")
                start_time, end_time = twelve_check.split('-')
                if end_time == '23:59':
                    twelve = f'{start_time}-24:00'
                else:
                    twelve = await page.client_storage.get_async("twelve_tomorrow")
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

    async def get_time_after_tomorrow():
        storage_info = await storage()
        cherg = check_cherg(storage_info)
        main_database = await page.client_storage.get_async("main_database")
        if await page.client_storage.get_async("database_storage") == 1:
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
        if await page.client_storage.get_async("database_storage") == 2:
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
            await page.client_storage.remove_async("one_after_tomorrow")
            time_after_tomorrow_1.visible = False
            print("One_After_Tomorrow not found!")
        else:
            await page.client_storage.set_async("one_after_tomorrow", result_one)
            one_check = await page.client_storage.get_async("one_after_tomorrow")
            try:
                start_time, end_time = one_check.split('-')
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = await page.client_storage.get_async("one_after_tomorrow")
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
                one = await page.client_storage.get_async("one_after_tomorrow")
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
            await page.client_storage.remove_async("two_after_tomorrow")
            time_after_tomorrow_2.visible = False
            print("Two_After_Tomorrow not found!")
        else:
            await page.client_storage.set_async("two_after_tomorrow", result_two)
            two_check = await page.client_storage.get_async("two_after_tomorrow")
            start_time, end_time = two_check.split('-')
            if end_time == '23:59':
                two = f'{start_time}-24:00'
            else:
                two = await page.client_storage.get_async("two_after_tomorrow")
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
            await page.client_storage.remove_async("three_after_tomorrow")
            time_after_tomorrow_3.visible = False
            print("Three_After_Tomorrow not found!")
        else:
            await page.client_storage.set_async("three_after_tomorrow", result_three)
            three_check = await page.client_storage.get_async("three_after_tomorrow")
            start_time, end_time = three_check.split('-')
            if end_time == '23:59':
                three = f'{start_time}-24:00'
            else:
                three = await page.client_storage.get_async("three_after_tomorrow")
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
            await page.client_storage.remove_async("four_after_tomorrow")
            time_after_tomorrow_4.visible = False
            print("Four_After_Tomorrow not found!")
        else:
            await page.client_storage.set_async("four_after_tomorrow", result_four)
            four_check = await page.client_storage.get_async("four_after_tomorrow")
            start_time, end_time = four_check.split('-')
            if end_time == '23:59':
                four = f'{start_time}-24:00'
            else:
                four = await page.client_storage.get_async("four_after_tomorrow")
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
            await page.client_storage.remove_async("five_after_tomorrow")
            time_after_tomorrow_5.visible = False
            print("Five_After_Tomorrow not found!")
        else:
            await page.client_storage.set_async("five_after_tomorrow", result_five)
            five_check = await page.client_storage.get_async("five_after_tomorrow")
            start_time, end_time = five_check.split('-')
            if end_time == '23:59':
                five = f'{start_time}-24:00'
            else:
                five = await page.client_storage.get_async("five_after_tomorrow")
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
            await page.client_storage.remove_async("six_after_tomorrow")
            time_after_tomorrow_6.visible = False
            print("Six_After_Tomorrow not found!")
        else:
            await page.client_storage.set_async("six_after_tomorrow", result_six)
            six_check = await page.client_storage.get_async("six_after_tomorrow")
            start_time, end_time = six_check.split('-')
            if end_time == '23:59':
                six = f'{start_time}-24:00'
            else:
                six = await page.client_storage.get_async("six_after_tomorrow")
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
            await page.client_storage.remove_async("seven_after_tomorrow")
            time_after_tomorrow_7.visible = False
            print("Seven_After_Tomorrow not found!")
        else:
            await page.client_storage.set_async("seven_after_tomorrow", result_seven)
            seven_check = await page.client_storage.get_async("seven_after_tomorrow")
            start_time, end_time = seven_check.split('-')
            if end_time == '23:59':
                seven = f'{start_time}-24:00'
            else:
                seven = await page.client_storage.get_async("seven_after_tomorrow")
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
            await page.client_storage.remove_async("eight_after_tomorrow")
            time_after_tomorrow_8.visible = False
            print("Eight_After_Tomorrow not found!")
        else:
            await page.client_storage.set_async("eight_after_tomorrow", result_eight)
            eight_check = await page.client_storage.get_async("eight_after_tomorrow")
            start_time, end_time = eight_check.split('-')
            if end_time == '23:59':
                eight = f'{start_time}-24:00'
            else:
                eight = await page.client_storage.get_async("eight_after_tomorrow")
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
            await page.client_storage.remove_async("nine_after_tomorrow")
            time_after_tomorrow_9.visible = False
            print("Nine_After_Tomorrow not found!")
        else:
            await page.client_storage.set_async("nine_after_tomorrow", result_nine)
            nine_check = await page.client_storage.get_async("nine_after_tomorrow")
            start_time, end_time = nine_check.split('-')
            if end_time == '23:59':
                nine = f'{start_time}-24:00'
            else:
                nine = await page.client_storage.get_async("nine_after_tomorrow")
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
            await page.client_storage.remove_async("ten_after_tomorrow")
            time_after_tomorrow_10.visible = False
            print("Ten_After_Tomorrow not found!")
        else:
            await page.client_storage.set_async("ten_after_tomorrow", result_ten)
            ten_check = await page.client_storage.get_async("ten_after_tomorrow")
            start_time, end_time = ten_check.split('-')
            if end_time == '23:59':
                ten = f'{start_time}-24:00'
            else:
                ten = await page.client_storage.get_async("ten_after_tomorrow")
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
            await page.client_storage.remove_async("eleven_after_tomorrow")
            time_after_tomorrow_11.visible = False
            print("Eleven_After_Tomorrow not found!")
        else:
            await page.client_storage.set_async("eleven_after_tomorrow", result_eleven)
            eleven_check = await page.client_storage.get_async("eleven_after_tomorrow")
            start_time, end_time = eleven_check.split('-')
            if end_time == '23:59':
                eleven = f'{start_time}-24:00'
            else:
                eleven = await page.client_storage.get_async("eleven_after_tomorrow")
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
            await page.client_storage.remove_async("twelve_after_tomorrow")
            time_after_tomorrow_12.visible = False
            print("Twelve_After_Tomorrow not found!")
        else:
            await page.client_storage.set_async("twelve_after_tomorrow", result_twelve)
            twelve_check = await page.client_storage.get_async("twelve_after_tomorrow")
            start_time, end_time = twelve_check.split('-')
            if end_time == '23:59':
                twelve = f'{start_time}-24:00'
            else:
                twelve = await page.client_storage.get_async("twelve_after_tomorrow")
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
        main_info.content = ft.Column(
            controls=[
                main_tab,
            ]
        )
        page.update()

    async def open_telegram(e):
        page.launch_url('https://t.me/sumy_svitlo',
                        web_window_name='Telegram')
        telegram_banner.open = False
        await page.client_storage.set_async('telegram_check', True)
        page.update()

    async def close_bunner(e):
        telegram_banner.open = False
        await page.client_storage.set_async('telegram_check', False)
        day_close = str(seven_days)
        print(day_close)
        await page.client_storage.set_async('day_close', day_close)
        page.update()

    async def options_check():
        lamp_check = await page.client_storage.get_async('lamp_options')
        if lamp_check == False:
            lamp_switch.value = False
            lamp_img.visible = False

        bg_check = await page.client_storage.get_async('bg_options')
        if bg_check == True:
            bg_switch.value = True

        page.update()

    async def bg_options(e):
        if bg_switch.value == True:
            await page.client_storage.set_async('bg_options', True)
        if bg_switch.value == False:
            await page.client_storage.set_async('bg_options', False)
            page.theme_mode = ft.ThemeMode.LIGHT
            main_container.gradient = ft.LinearGradient(
                begin=ft.alignment.top_right,
                end=ft.alignment.bottom_left,
                colors=['#ffcc66', '#ff6666']
            )
        await check_storage_main()
        page.update()

    async def lamp_options(e):
        if lamp_switch.value == True:
            await page.client_storage.set_async('lamp_options', True)
            lamp_img.visible = True
            print('Lamp ON')
        if lamp_switch.value == False:
            await page.client_storage.set_async('lamp_options', False)
            # page.navigation_bar.indicator_color = '#ffcc66'
            lamp_img.visible = False
            print('Lamp OFF')
        page.update()

    async def info_check():
        source = await page.client_storage.get_async('source')
        if await page.client_storage.get_async('database_storage') == 1:
            database = "1"
        elif await page.client_storage.get_async('database_storage') == 2:
            database = "2"
        else:
            database = await page.client_storage.get_async('database_storage')
        info_options.content = ft.Row(
            alignment='center',
            controls=[
                ft.Text(
                    f"Джерело: {source}",
                    color=ft.colors.BLACK87,
                    weight="w400",
                    font_family="Golos Text",
                    text_align="center"
                ),
                ft.Text(
                    f"База даних: {database}",
                    color=ft.colors.BLACK87,
                    weight="w400",
                    font_family="Golos Text",
                    text_align="center"
                )
            ]
        )
        info_options.visible = True
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

    bs = ft.AlertDialog(
        modal=False,
        content=ft.Column(
            horizontal_alignment='center',
            alignment='center',
            height=380,
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
            ]
        )
    )

    # bs = ft.BottomSheet(
    #     content=ft.Container(
    #         margin=10,
    #         content=ft.Column(
    #             horizontal_alignment='center',
    #             alignment='center',
    #             # height=380,
    #             # width=400,
    #             # spacing=5,
    #             # wrap=True,
    #             controls=[
    #                 ft.Text(
    #                     "Оберіть чергу:",
    #                     size=20,
    #                     weight='w500',
    #                     text_align='center',
    #                     font_family="Golos Text"
    #                 ),
    #                 one_button,
    #                 two_button,
    #                 three_button,
    #                 four_button,
    #                 five_button,
    #                 six_button,
    #                 # ft.Container(height=10),
    #             ]
    #         )
    #     )
    # )

    lamp_img = ft.SafeArea(
        content=ft.Image(
            src=f"/Images/lamp_on.png",
            # gapless_playback=True,
        ),
        expand=2
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
        expand=3,
        blur=10,
        padding=15,
        bgcolor=ft.colors.BLACK26,
        border_radius=15,
        content=ft.Column(
            horizontal_alignment='center',
            alignment="center",
            controls=[
                progress_bar
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

    lamp_switch = ft.Switch(
        on_change=lamp_options,
        value=True,
        active_color='#ffcc66',
        inactive_thumb_color=ft.colors.GREY,
        active_track_color=ft.colors.WHITE,
        inactive_track_color=ft.colors.WHITE,
        hover_color=ft.colors.WHITE12,
        label_position=ft.LabelPosition.LEFT,
        track_outline_color=ft.colors.WHITE
    )

    bg_switch = ft.Switch(
        on_change=bg_options,
        value=False,
        active_color='#ffcc66',
        inactive_thumb_color=ft.colors.GREY,
        active_track_color=ft.colors.WHITE,
        inactive_track_color=ft.colors.WHITE,
        hover_color=ft.colors.WHITE12,
        label_position=ft.LabelPosition.LEFT,
        track_outline_color=ft.colors.WHITE
    )

    option_switchers = ft.Column(
        controls=[
            ft.Container(
                blur=10,
                bgcolor=ft.colors.BLACK12,
                border_radius=15,
                padding=15,
                alignment=ft.alignment.center,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            spacing=0,
                            controls=[
                                ft.Text(
                                    "Відображення",
                                    size=16,
                                    color=ft.colors.BLACK87,
                                    weight="w400",
                                    font_family="Golos Text",
                                    text_align="start",
                                ),
                                ft.Text(
                                    "Лампочки",
                                    size=16,
                                    color=ft.colors.BLACK87,
                                    weight="w400",
                                    font_family="Golos Text",
                                    text_align="start",
                                )
                            ]
                        ),
                        lamp_switch
                    ]
                )
            ),
            ft.Container(
                blur=10,
                bgcolor=ft.colors.BLACK12,
                border_radius=15,
                padding=15,
                alignment=ft.alignment.center,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            spacing=0,
                            controls=[
                                ft.Text(
                                    "Змінювати фон",
                                    size=16,
                                    color=ft.colors.BLACK87,
                                    weight="w400",
                                    font_family="Golos Text",
                                    text_align="start",
                                ),
                                ft.Text(
                                    "якщо світло вимкнуте",
                                    size=16,
                                    color=ft.colors.BLACK87,
                                    weight="w400",
                                    font_family="Golos Text",
                                    text_align="start",
                                )
                            ]
                        ),
                        bg_switch
                    ]
                )
            ),
        ]
    )

    info_options = ft.Container(
        visible=False,
        content=ft.Column()
    )

    options_tab = ft.SafeArea(
        visible=False,
        content=ft.Container(
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
                    option_switchers,
                    info_options
                ]
            )
        )
    )

    grafic_refresh = ft.Container(
        ft.Text(
            weight='w400',
            color=ft.colors.BLACK,
            font_family="Golos Text",
            height=18
        )
    )

    main = ft.SafeArea(
        ft.Column(
            horizontal_alignment='center',
            alignment='center',
            controls=[
                lamp_img,
                text_after_img,
                main_info,
                grafic_refresh
            ]
        ),
        expand=True
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
                main,
                info_tab,
                options_tab
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
                icon=ft.icons.INFO, selected_icon=ft.icons.INFO_OUTLINE, label='Інформація'),
            ft.NavigationDestination(
                icon=ft.icons.SETTINGS_ROUNDED, selected_icon=ft.icons.SETTINGS_OUTLINED, label='Параметри'),
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
    await check_cherg_main()
    await check_telegram()
    await options_check()
    page.run_task(check_storage)
    page.update()

    def event_detach(e):
        if e.data == "detach" and page.platform == ft.PagePlatform.ANDROID:
            os._exit(1)

    def event_hide(e):
        if e.data == "hide" and page.platform == ft.PagePlatform.ANDROID:
            os._exit(1)

    def event_pause(e):
        if e.data == "pause" and page.platform == ft.PagePlatform.ANDROID:
            os._exit(1)

    page.on_app_lifecycle_state_change = event_detach
    # page.on_app_lifecycle_state_change = event_hide
    # page.on_app_lifecycle_state_change = event_pause

    while True:
        await asyncio.sleep(60)
        try:
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
            await asyncio.sleep(1)
            await check_storage_refresh()
            print("Update Complete!")
        except:
            print("Update Not Complete!")


ft.app(
    target=main,
    name="Svitlo Sumy",
    assets_dir='assets',
)
