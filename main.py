import flet as ft
from functions import check_cherg, today, tomorrow, after_tomorrow
from functions import day_num_one, day_num_two, day_num_three, day_num_four, day_num_five, day_num_six
from functions import day_tomorrow_one, day_tomorrow_two, day_tomorrow_three, day_tomorrow_four, day_tomorrow_five, day_tomorrow_six
from functions import day_after_tomorrow_one, day_after_tomorrow_two, day_after_tomorrow_three, day_after_tomorrow_four, day_after_tomorrow_five, day_after_tomorrow_six
from time_now import time_now_1, time_now_2, time_now_3, time_now_4, time_now_5, time_now_6
from time_tomorrow import time_tomorrow_1, time_tomorrow_2, time_tomorrow_3, time_tomorrow_4, time_tomorrow_5, time_tomorrow_6
from time_after_tomorrow import time_after_tomorrow_1, time_after_tomorrow_2, time_after_tomorrow_3, time_after_tomorrow_4, time_after_tomorrow_5, time_after_tomorrow_6
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests


def main(page: ft.Page):

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

    def open_pdf(e):
        page.launch_url('https://www.soe.com.ua/images/gr23-24-adr.pdf')

    def cherg_choise(e):
        numb_cherg = e.control.data
        page.client_storage.set("number", numb_cherg)
        bs.open = False
        bs.update()
        current_time = datetime.now().time()
        storage_info = storage()
        cherg = check_cherg(storage_info)
        one_check = page.client_storage.get("one")
        two_check = page.client_storage.get("two")
        three_check = page.client_storage.get("three")
        four_check = page.client_storage.get("four")
        five_check = page.client_storage.get("five")
        six_check = page.client_storage.get("six")
        try:
            try_one = db.reference(f"/{cherg}/{day_num_one}")
            result_one = try_one.get()
            page.client_storage.set("one", result_one)
            one_check = page.client_storage.get("one")
            start_time, end_time = one_check.split('-')
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if time_end <= current_time:
                time_now_1.bgcolor = ft.colors.GREY_400
            else:
                time_now_1.bgcolor = '#ffcc66'
            if end_time == '23:59':
                one = f'{start_time}-24:00'
            else:
                one = page.client_storage.get("one")
            time_now_1.visible = True
            time_now_1.content = ft.Text(
                one,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("One found!")
        except:
            if page.client_storage.get("one") != None:
                one_check = page.client_storage.get("one")
                start_time, end_time = one_check.split('-')
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if time_end <= current_time:
                    time_now_1.bgcolor = ft.colors.GREY_400
                else:
                    time_now_1.bgcolor = '#ffcc66'
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = page.client_storage.get("one")
                time_now_1.visible = True
                time_now_1.content = ft.Text(
                    one,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
            page.update()
            print("One not found!")

        try:
            try_two = db.reference(f"/{cherg}/{day_num_two}")
            result_two = try_two.get()
            page.client_storage.set("two", result_two)
            two_check = page.client_storage.get("two")
            two_check = page.client_storage.get("two")
            start_time, end_time = two_check.split('-')
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if time_end <= current_time:
                time_now_2.bgcolor = ft.colors.GREY_400
            else:
                time_now_2.bgcolor = '#ffcc66'
            if end_time == '23:59':
                two = f'{start_time}-24:00'
            else:
                two = page.client_storage.get("two")
            time_now_2.visible = True
            time_now_2.content = ft.Text(
                two,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Two found!")
        except:
            if page.client_storage.get("two") != None:
                two_check = page.client_storage.get("two")
                start_time, end_time = two_check.split('-')
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if time_end <= current_time:
                    time_now_2.bgcolor = ft.colors.GREY_400
                else:
                    time_now_2.bgcolor = '#ffcc66'
                if end_time == '23:59':
                    two = f'{start_time}-24:00'
                else:
                    two = page.client_storage.get("two")
                time_now_2.visible = True
                time_now_2.content = ft.Text(
                    two,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
            page.update()
            print("Two not found!")

        try:
            try_three = db.reference(f"/{cherg}/{day_num_three}")
            result_three = try_three.get()
            page.client_storage.set("three", result_three)
            three_check = page.client_storage.get("three")
            start_time, end_time = three_check.split('-')
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if time_end <= current_time:
                time_now_3.bgcolor = ft.colors.GREY_400
            else:
                time_now_3.bgcolor = '#ffcc66'
            if end_time == '23:59':
                three = f'{start_time}-24:00'
            else:
                three = page.client_storage.get("three")
            time_now_3.visible = True
            time_now_3.content = ft.Text(
                three,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Three found!")
        except:
            if page.client_storage.get("three") != None:
                three_check = page.client_storage.get("three")
                start_time, end_time = three_check.split('-')
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if time_end <= current_time:
                    time_now_3.bgcolor = ft.colors.GREY_400
                else:
                    time_now_3.bgcolor = '#ffcc66'
                if end_time == '23:59':
                    three = f'{start_time}-24:00'
                else:
                    three = page.client_storage.get("three")
                time_now_3.visible = True
                time_now_3.content = ft.Text(
                    three,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
            page.update()
            print("Three not found!")

        try:
            try_four = db.reference(f"/{cherg}/{day_num_four}")
            result_four = try_four.get()
            page.client_storage.set("four", result_four)
            four_check = page.client_storage.get("four")
            start_time, end_time = four_check.split('-')
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if time_end <= current_time:
                time_now_4.bgcolor = ft.colors.GREY_400
            else:
                time_now_4.bgcolor = '#ffcc66'
            if end_time == '23:59':
                four = f'{start_time}-24:00'
            else:
                four = page.client_storage.get("four")
            time_now_4.visible = True
            time_now_4.content = ft.Text(
                four,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Four found!")
        except:
            if page.client_storage.get("four") != None:
                four_check = page.client_storage.get("four")
                start_time, end_time = four_check.split('-')
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if time_end <= current_time:
                    time_now_4.bgcolor = ft.colors.GREY_400
                else:
                    time_now_4.bgcolor = '#ffcc66'
                if end_time == '23:59':
                    four = f'{start_time}-24:00'
                else:
                    four = page.client_storage.get("four")
                time_now_4.visible = True
                time_now_4.content = ft.Text(
                    four,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
            page.update()
            print("Four not found!")

        try:
            try_five = db.reference(f"/{cherg}/{day_num_five}")
            result_five = try_five.get()
            page.client_storage.set("five", result_five)
            five_check = page.client_storage.get("five")
            start_time, end_time = five_check.split('-')
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if time_end <= current_time:
                time_now_5.bgcolor = ft.colors.GREY_400
            else:
                time_now_5.bgcolor = '#ffcc66'
            if end_time == '23:59':
                five = f'{start_time}-24:00'
            else:
                five = page.client_storage.get("five")
            time_now_5.visible = True
            time_now_5.content = ft.Text(
                five,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Five found!")
        except:
            if page.client_storage.get("five") != None:
                five_check = page.client_storage.get("five")
                start_time, end_time = five_check.split('-')
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if time_end <= current_time:
                    time_now_5.bgcolor = ft.colors.GREY_400
                else:
                    time_now_5.bgcolor = '#ffcc66'
                if end_time == '23:59':
                    five = f'{start_time}-24:00'
                else:
                    five = page.client_storage.get("five")
                time_now_5.visible = True
                time_now_5.content = ft.Text(
                    five,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
            page.update()
            print("Five not found!")

        try:
            try_six = db.reference(f"/{cherg}/{day_num_six}")
            result_six = try_six.get()
            page.client_storage.set("six", result_six)
            six_check = page.client_storage.get("six")
            start_time, end_time = six_check.split('-')
            time_end = datetime.strptime(end_time, '%H:%M').time()
            if time_end <= current_time:
                time_now_6.bgcolor = ft.colors.GREY_400
            else:
                time_now_6.bgcolor = '#ffcc66'
            if end_time == '23:59':
                six = f'{start_time}-24:00'
            else:
                six = page.client_storage.get("six")
            time_now_6.visible = True
            time_now_6.content = ft.Text(
                six,
                size=21,
                weight='w500',
                color=ft.colors.BLACK,
                font_family="Golos Text"
            )
            page.update()
            print("Six found!")
        except:
            if page.client_storage.get("six") != None:
                six_check = page.client_storage.get("six")
                start_time, end_time = six_check.split('-')
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if time_end <= current_time:
                    time_now_6.bgcolor = ft.colors.GREY_400
                else:
                    time_now_6.bgcolor = '#ffcc66'
                if end_time == '23:59':
                    six = f'{start_time}-24:00'
                else:
                    six = page.client_storage.get("six")
                time_now_6.visible = True
                time_now_6.content = ft.Text(
                    six,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
                page.update()
            page.update()
            print("Six not found!")
        progress_bar.visible = False
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

    def check_storage():
        if page.client_storage.get("number") == None:
            try:
                requests.get("http://google.com").ok
                connect_firebase = credentials.Certificate(
                    "./assets/firebase_init.json")
                firebase_admin.initialize_app(
                    connect_firebase, {"databaseURL": "https://svitlo-sumy-default-rtdb.europe-west1.firebasedatabase.app"})
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
                connect_firebase = credentials.Certificate(
                    "./assets/firebase_init.json")
                firebase_admin.initialize_app(
                    connect_firebase, {"databaseURL": "https://svitlo-sumy-default-rtdb.europe-west1.firebasedatabase.app"})
                test_connect = db.reference()
                test_connect.get()
                print('Connected!')
            except:
                one_button.disabled = True
                two_button.disabled = True
                three_button.disabled = True
                four_button.disabled = True
                five_button.disabled = True
                six_button.disabled = True
                alert_conn_start()
                print("Fail connection!")
            current_time = datetime.now().time()
            storage_info = storage()
            cherg = check_cherg(storage_info)
            one_check = page.client_storage.get("one")
            two_check = page.client_storage.get("two")
            three_check = page.client_storage.get("three")
            four_check = page.client_storage.get("four")
            five_check = page.client_storage.get("five")
            six_check = page.client_storage.get("six")
            try:
                try_one = db.reference(f"/{cherg}/{day_num_one}")
                result_one = try_one.get()
                page.client_storage.set("one", result_one)
                one_check = page.client_storage.get("one")
                start_time, end_time = one_check.split('-')
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if time_end <= current_time:
                    time_now_1.bgcolor = ft.colors.GREY_400
                else:
                    time_now_1.bgcolor = '#ffcc66'
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = page.client_storage.get("one")
                time_now_1.visible = True
                time_now_1.content = ft.Text(
                    one,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
                page.update()
                print("One found!")
            except:
                if page.client_storage.get("one") != None:
                    one_check = page.client_storage.get("one")
                    start_time, end_time = one_check.split('-')
                    time_end = datetime.strptime(end_time, '%H:%M').time()
                    if time_end <= current_time:
                        time_now_1.bgcolor = ft.colors.GREY_400
                    else:
                        time_now_1.bgcolor = '#ffcc66'
                    if end_time == '23:59':
                        one = f'{start_time}-24:00'
                    else:
                        one = page.client_storage.get("one")
                    time_now_1.visible = True
                    time_now_1.content = ft.Text(
                        one,
                        size=21,
                        weight='w500',
                        color=ft.colors.BLACK,
                        font_family="Golos Text"
                    )
                page.update()
                print("One not found!")

            try:
                try_two = db.reference(f"/{cherg}/{day_num_two}")
                result_two = try_two.get()
                page.client_storage.set("two", result_two)
                two_check = page.client_storage.get("two")
                start_time, end_time = two_check.split('-')
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if time_end <= current_time:
                    time_now_2.bgcolor = ft.colors.GREY_400
                else:
                    time_now_2.bgcolor = '#ffcc66'
                if end_time == '23:59':
                    two = f'{start_time}-24:00'
                else:
                    two = page.client_storage.get("two")
                time_now_2.visible = True
                time_now_2.content = ft.Text(
                    two,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
                page.update()
                print("Two found!")
            except:
                if page.client_storage.get("two") != None:
                    two_check = page.client_storage.get("two")
                    start_time, end_time = two_check.split('-')
                    time_end = datetime.strptime(end_time, '%H:%M').time()
                    if time_end <= current_time:
                        time_now_2.bgcolor = ft.colors.GREY_400
                    else:
                        time_now_2.bgcolor = '#ffcc66'
                    if end_time == '23:59':
                        two = f'{start_time}-24:00'
                    else:
                        two = page.client_storage.get("two")
                    time_now_2.visible = True
                    time_now_2.content = ft.Text(
                        two,
                        size=21,
                        weight='w500',
                        color=ft.colors.BLACK,
                        font_family="Golos Text"
                    )
                page.update()
                print("Two not found!")

            try:
                try_three = db.reference(f"/{cherg}/{day_num_three}")
                result_three = try_three.get()
                page.client_storage.set("three", result_three)
                three_check = page.client_storage.get("three")
                start_time, end_time = three_check.split('-')
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if time_end <= current_time:
                    time_now_3.bgcolor = ft.colors.GREY_400
                else:
                    time_now_3.bgcolor = '#ffcc66'
                if end_time == '23:59':
                    three = f'{start_time}-24:00'
                else:
                    three = page.client_storage.get("three")
                time_now_3.visible = True
                time_now_3.content = ft.Text(
                    three,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
                page.update()
                print("Three found!")
            except:
                if page.client_storage.get("three") != None:
                    three_check = page.client_storage.get("three")
                    start_time, end_time = three_check.split('-')
                    time_end = datetime.strptime(end_time, '%H:%M').time()
                    if time_end <= current_time:
                        time_now_3.bgcolor = ft.colors.GREY_400
                    else:
                        time_now_3.bgcolor = '#ffcc66'
                    if end_time == '23:59':
                        three = f'{start_time}-24:00'
                    else:
                        three = page.client_storage.get("three")
                    time_now_3.visible = True
                    time_now_3.content = ft.Text(
                        three,
                        size=21,
                        weight='w500',
                        color=ft.colors.BLACK,
                        font_family="Golos Text"
                    )
                page.update()
                print("Three not found!")

            try:
                try_four = db.reference(f"/{cherg}/{day_num_four}")
                result_four = try_four.get()
                page.client_storage.set("four", result_four)
                four_check = page.client_storage.get("four")
                start_time, end_time = four_check.split('-')
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if time_end <= current_time:
                    time_now_4.bgcolor = ft.colors.GREY_400
                else:
                    time_now_4.bgcolor = '#ffcc66'
                if end_time == '23:59':
                    four = f'{start_time}-24:00'
                else:
                    four = page.client_storage.get("four")
                time_now_4.visible = True
                time_now_4.content = ft.Text(
                    four,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
                page.update()
                print("Four found!")
            except:
                if page.client_storage.get("four") != None:
                    four_check = page.client_storage.get("four")
                    start_time, end_time = four_check.split('-')
                    time_end = datetime.strptime(end_time, '%H:%M').time()
                    if time_end <= current_time:
                        time_now_4.bgcolor = ft.colors.GREY_400
                    else:
                        time_now_4.bgcolor = '#ffcc66'
                    if end_time == '23:59':
                        four = f'{start_time}-24:00'
                    else:
                        four = page.client_storage.get("four")
                    time_now_4.visible = True
                    time_now_4.content = ft.Text(
                        four,
                        size=21,
                        weight='w500',
                        color=ft.colors.BLACK,
                        font_family="Golos Text"
                    )
                page.update()
                print("Four not found!")

            try:
                try_five = db.reference(f"/{cherg}/{day_num_five}")
                result_five = try_five.get()
                page.client_storage.set("five", result_five)
                five_check = page.client_storage.get("five")
                start_time, end_time = five_check.split('-')
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if time_end <= current_time:
                    time_now_5.bgcolor = ft.colors.GREY_400
                else:
                    time_now_5.bgcolor = '#ffcc66'
                if end_time == '23:59':
                    five = f'{start_time}-24:00'
                else:
                    five = page.client_storage.get("five")
                time_now_5.visible = True
                time_now_5.content = ft.Text(
                    five,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
                page.update()
                print("Five found!")
            except:
                if page.client_storage.get("five") != None:
                    five_check = page.client_storage.get("five")
                    start_time, end_time = five_check.split('-')
                    time_end = datetime.strptime(end_time, '%H:%M').time()
                    if time_end <= current_time:
                        time_now_5.bgcolor = ft.colors.GREY_400
                    else:
                        time_now_5.bgcolor = '#ffcc66'
                    if end_time == '23:59':
                        five = f'{start_time}-24:00'
                    else:
                        five = page.client_storage.get("five")
                    time_now_5.visible = True
                    time_now_5.content = ft.Text(
                        five,
                        size=21,
                        weight='w500',
                        color=ft.colors.BLACK,
                        font_family="Golos Text"
                    )
                page.update()
                print("Five not found!")

            try:
                try_six = db.reference(f"/{cherg}/{day_num_six}")
                result_six = try_six.get()
                page.client_storage.set("six", result_six)
                six_check = page.client_storage.get("six")
                start_time, end_time = six_check.split('-')
                time_end = datetime.strptime(end_time, '%H:%M').time()
                if time_end <= current_time:
                    time_now_6.bgcolor = ft.colors.GREY_400
                else:
                    time_now_6.bgcolor = '#ffcc66'
                if end_time == '23:59':
                    six = f'{start_time}-24:00'
                else:
                    six = page.client_storage.get("six")
                time_now_6.visible = True
                time_now_6.content = ft.Text(
                    six,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
                page.update()
                print("Six found!")
            except:
                if page.client_storage.get("six") != None:
                    six_check = page.client_storage.get("six")
                    start_time, end_time = six_check.split('-')
                    time_end = datetime.strptime(end_time, '%H:%M').time()
                    if time_end <= current_time:
                        time_now_6.bgcolor = ft.colors.GREY_400
                    else:
                        time_now_6.bgcolor = '#ffcc66'
                    if end_time == '23:59':
                        six = f'{start_time}-24:00'
                    else:
                        six = page.client_storage.get("six")
                    time_now_6.visible = True
                    time_now_6.content = ft.Text(
                        six,
                        size=21,
                        weight='w500',
                        color=ft.colors.BLACK,
                        font_family="Golos Text"
                    )
                    page.update()
                page.update()
                print("Six not found!")
            progress_bar.visible = False
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
                height=280,
                width=280,
            )
            return True
        else:
            lamp_img.content = ft.Image(
                src=f"/Images/lamp_on.png",
                height=280,
                width=280,
            )
            return False

    def alert_conn_start():
        alert_conn.open = True
        page.update()

    def alert_conn_first():
        alert_first_conn.open = True
        page.update()

    def get_time_tomorrow():
        storage_info = storage()
        cherg = check_cherg(storage_info)
        try:
            try_one = db.reference(f"/{cherg}/{day_tomorrow_one}")
            result_one = try_one.get()
            page.client_storage.set("one_tomorrow", result_one)
            one_check = page.client_storage.get("one_tomorrow")
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
            if page.client_storage.get("one_tomorrow") != None:
                one_check = page.client_storage.get("one_tomorrow")
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
            print("One_Tomorrow not found!")

        try:
            try_two = db.reference(f"/{cherg}/{day_tomorrow_two}")
            result_two = try_two.get()
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
        except:
            if page.client_storage.get("two_tomorrow") != None:
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
            print("Two_Tomorrow not found!")

        try:
            try_three = db.reference(f"/{cherg}/{day_tomorrow_three}")
            result_three = try_three.get()
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
        except:
            if page.client_storage.get("three_tomorrow") != None:
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
            print("Three_Tomorrow not found!")

        try:
            try_four = db.reference(f"/{cherg}/{day_tomorrow_four}")
            result_four = try_four.get()
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
        except:
            if page.client_storage.get("four_tomorrow") != None:
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
            print("Four_Tomorrow not found!")

        try:
            try_five = db.reference(f"/{cherg}/{day_tomorrow_five}")
            result_five = try_five.get()
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
        except:
            if page.client_storage.get("five_tomorrow") != None:
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
            print("Five_Tomorrow not found!")

        try:
            try_six = db.reference(f"/{cherg}/{day_tomorrow_six}")
            result_six = try_six.get()
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
        except:
            if page.client_storage.get("six_tomorrow") != None:
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
            page.update()
            print("Six_Tomorrow not found!")
        page.update()

    def get_time_after_tomorrow():
        storage_info = storage()
        cherg = check_cherg(storage_info)
        try:
            try_one = db.reference(f"/{cherg}/{day_after_tomorrow_one}")
            result_one = try_one.get()
            page.client_storage.set("one_after_tomorrow", result_one)
            one_check = page.client_storage.get("one_after_tomorrow")
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
            if page.client_storage.get("one_after_tomorrow") != None:
                one_check = page.client_storage.get("one_after_tomorrow")
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
            print("One_After_Tomorrow not found!")

        try:
            try_two = db.reference(f"/{cherg}/{day_after_tomorrow_two}")
            result_two = try_two.get()
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
        except:
            if page.client_storage.get("two_after_tomorrow") != None:
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
            print("Two_After_Tomorrow not found!")

        try:
            try_three = db.reference(f"/{cherg}/{day_after_tomorrow_three}")
            result_three = try_three.get()
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
        except:
            if page.client_storage.get("three_after_tomorrow") != None:
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
            print("Three_After_Tomorrow not found!")

        try:
            try_four = db.reference(f"/{cherg}/{day_after_tomorrow_four}")
            result_four = try_four.get()
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
        except:
            if page.client_storage.get("four_after_tomorrow") != None:
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
            print("Four_After_Tomorrow not found!")

        try:
            try_five = db.reference(f"/{cherg}/{day_after_tomorrow_five}")
            result_five = try_five.get()
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
        except:
            if page.client_storage.get("five_after_tomorrow") != None:
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
            print("Five_After_Tomorrow not found!")

        try:
            try_six = db.reference(f"/{cherg}/{day_after_tomorrow_six}")
            result_six = try_six.get()
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
        except:
            if page.client_storage.get("six_after_tomorrow") != None:
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
            page.update()
            print("Six_After_Tomorrow not found!")
        page.update()

    def main_tab_anim():
        main_info.expand = True
        main_info.content = ft.Column(
            controls=[
                main_tab
            ]
        )
        page.update()

    alert_conn = ft.SnackBar(
        behavior=ft.SnackBarBehavior.FLOATING,
        elevation=15,
        duration=5000,
        bgcolor='#ffcc66',
        content=ft.Text(
            "Немає доступу до інтернету або слабке з'єднання. Використовується інформація, яка була завантажена в минуле відкриття застосунку!",
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
            "Немає доступу до інтернету або слабке з'єднання. Для оновлення інформації потрібне підключення до інтернету!",
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
                height=280,
                width=280,
            )
        )
    )

    text_after_img = ft.Text(
        "Графік відключень",
        size=24,
        weight='w500',
        color=ft.colors.BLACK87,
        font_family="Golos Text",
        text_align='center'
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
                tab_content=ft.Column(
                    spacing=0,
                    horizontal_alignment='center',
                    alignment='start',
                    controls=[
                        ft.Text(
                            "Сьогодні",
                            size=18,
                            text_align='center',
                            font_family="Golos Text",
                            weight="w500"
                        ),
                        ft.Text(
                            today.strftime("(%d.%m)"),
                            size=16,
                            text_align='center',
                            font_family="Golos Text",
                            weight="w500"
                        )
                    ]
                ),
                content=time_now
            ),
            ft.Tab(
                tab_content=ft.Column(
                    spacing=0,
                    horizontal_alignment='center',
                    alignment='start',
                    controls=[
                        ft.Text(
                            "Завтра",
                            size=18,
                            text_align='center',
                            font_family="Golos Text",
                            weight="w500"
                        ),
                        ft.Text(
                            tomorrow.strftime("(%d.%m)"),
                            size=16,
                            text_align='center',
                            font_family="Golos Text",
                            weight="w500"
                        )
                    ]
                ),
                content=time_tomorrow
            ),
            ft.Tab(
                tab_content=ft.Column(
                    spacing=0,
                    horizontal_alignment='center',
                    alignment='start',
                    controls=[
                        ft.Text(
                            "Післязавтра",
                            size=18,
                            text_align='center',
                            font_family="Golos Text",
                            weight="w500"
                        ),
                        ft.Text(
                            after_tomorrow.strftime("(%d.%m)"),
                            size=16,
                            text_align='center',
                            font_family="Golos Text",
                            weight="w500"
                        )
                    ]
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
                        content=ft.Text(
                            "Дізнатися свою чергу",
                            size=18,
                            color='black',
                            text_align='center',
                            font_family="Golos Text",
                            weight="w500"
                        ),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=15),
                            overlay_color=ft.colors.AMBER_200),
                        height=50,
                        color=ft.colors.BLACK,
                        bgcolor='#ffcc66',
                        on_click=open_pdf
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
    page.update()
    check_storage()


ft.app(
    target=main,
    name="Svitlo Sumy",
    assets_dir='assets',
)
