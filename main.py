import flet as ft
from functions import check_cherg, day_num_one, day_num_two, day_num_three, day_num_four, day_num_five, day_num_six
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
            expand_container.visible = True
            info_tab.visible = False
            open_list()
        if my_index == 1:
            expand_container.visible = True
            info_tab.visible = False
            page.update()
        if my_index == 2:
            info_tab.visible = True
            expand_container.visible = False
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
            if end_time == '23:59':
                one = f'{start_time}-24:00'
            else:
                one = page.client_storage.get("one")
            time_1.visible = True
            time_1.content = ft.Text(
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
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = page.client_storage.get("one")
                time_1.visible = True
                time_1.content = ft.Text(
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
            if end_time == '23:59':
                two = f'{start_time}-24:00'
            else:
                two = page.client_storage.get("two")
            time_2.visible = True
            time_2.content = ft.Text(
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
                if end_time == '23:59':
                    two = f'{start_time}-24:00'
                else:
                    two = page.client_storage.get("two")
                time_2.visible = True
                time_2.content = ft.Text(
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
            if end_time == '23:59':
                three = f'{start_time}-24:00'
            else:
                three = page.client_storage.get("three")
            time_3.visible = True
            time_3.content = ft.Text(
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
                if end_time == '23:59':
                    three = f'{start_time}-24:00'
                else:
                    three = page.client_storage.get("three")
                time_3.visible = True
                time_3.content = ft.Text(
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
            if end_time == '23:59':
                four = f'{start_time}-24:00'
            else:
                four = page.client_storage.get("four")
            time_4.visible = True
            time_4.content = ft.Text(
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
                if end_time == '23:59':
                    four = f'{start_time}-24:00'
                else:
                    four = page.client_storage.get("four")
                time_4.visible = True
                time_4.content = ft.Text(
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
            if end_time == '23:59':
                five = f'{start_time}-24:00'
            else:
                five = page.client_storage.get("five")
            time_5.visible = True
            time_5.content = ft.Text(
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
                if end_time == '23:59':
                    five = f'{start_time}-24:00'
                else:
                    five = page.client_storage.get("five")
                time_5.visible = True
                time_5.content = ft.Text(
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
            if end_time == '23:59':
                six = f'{start_time}-24:00'
            else:
                six = page.client_storage.get("six")
            time_6.visible = True
            time_6.content = ft.Text(
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
                if end_time == '23:59':
                    six = f'{start_time}-24:00'
                else:
                    six = page.client_storage.get("six")
                time_6.visible = True
                time_6.content = ft.Text(
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
        all_time.visible = True
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
                if end_time == '23:59':
                    one = f'{start_time}-24:00'
                else:
                    one = page.client_storage.get("one")
                time_1.visible = True
                time_1.content = ft.Text(
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
                    if end_time == '23:59':
                        one = f'{start_time}-24:00'
                    else:
                        one = page.client_storage.get("one")
                    time_1.visible = True
                    time_1.content = ft.Text(
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
                if end_time == '23:59':
                    two = f'{start_time}-24:00'
                else:
                    two = page.client_storage.get("two")
                time_2.visible = True
                time_2.content = ft.Text(
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
                    if end_time == '23:59':
                        two = f'{start_time}-24:00'
                    else:
                        two = page.client_storage.get("two")
                    time_2.visible = True
                    time_2.content = ft.Text(
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
                if end_time == '23:59':
                    three = f'{start_time}-24:00'
                else:
                    three = page.client_storage.get("three")
                time_3.visible = True
                time_3.content = ft.Text(
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
                    if end_time == '23:59':
                        three = f'{start_time}-24:00'
                    else:
                        three = page.client_storage.get("three")
                    time_3.visible = True
                    time_3.content = ft.Text(
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
                if end_time == '23:59':
                    four = f'{start_time}-24:00'
                else:
                    four = page.client_storage.get("four")
                time_4.visible = True
                time_4.content = ft.Text(
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
                    if end_time == '23:59':
                        four = f'{start_time}-24:00'
                    else:
                        four = page.client_storage.get("four")
                    time_4.visible = True
                    time_4.content = ft.Text(
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
                if end_time == '23:59':
                    five = f'{start_time}-24:00'
                else:
                    five = page.client_storage.get("five")
                time_5.visible = True
                time_5.content = ft.Text(
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
                    if end_time == '23:59':
                        five = f'{start_time}-24:00'
                    else:
                        five = page.client_storage.get("five")
                    time_5.visible = True
                    time_5.content = ft.Text(
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
                if end_time == '23:59':
                    six = f'{start_time}-24:00'
                else:
                    six = page.client_storage.get("six")
                time_6.visible = True
                time_6.content = ft.Text(
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
                    if end_time == '23:59':
                        six = f'{start_time}-24:00'
                    else:
                        six = page.client_storage.get("six")
                    time_6.visible = True
                    time_6.content = ft.Text(
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
            all_time.visible = True
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

    one = page.client_storage.get("one")
    two = page.client_storage.get("two")
    three = page.client_storage.get("three")
    four = page.client_storage.get("four")
    five = page.client_storage.get("five")
    six = page.client_storage.get("six")

    progress_bar = ft.ProgressBar(
        visible=True,
        bgcolor="white",
        color="#ffcc66",
        bar_height=5,
    )

    time_1 = ft.Container(
        visible=False,
        shadow=ft.BoxShadow(
            blur_radius=2,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(0, 2),
            color=ft.colors.BLACK54
        ),
        bgcolor='#ffcc66',
        border_radius=5,
        padding=10,
        content=ft.Text(
            one,
            size=21,
            weight='w500',
            color=ft.colors.BLACK,
            font_family="Golos Text"
        )
    )

    time_2 = ft.Container(
        visible=False,
        shadow=ft.BoxShadow(
            blur_radius=2,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(0, 2),
            color=ft.colors.BLACK54
        ),
        bgcolor='#ffcc66',
        border_radius=5,
        padding=10,
        content=ft.Text(
            two,
            size=21,
            weight='w500',
            color=ft.colors.BLACK,
            font_family="Golos Text"
        )
    )

    time_3 = ft.Container(
        visible=False,
        shadow=ft.BoxShadow(
            blur_radius=2,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(0, 2),
            color=ft.colors.BLACK54
        ),
        bgcolor='#ffcc66',
        border_radius=5,
        padding=10,
        content=ft.Text(
            three,
            size=21,
            weight='w500',
            color=ft.colors.BLACK,
            font_family="Golos Text"
        )
    )

    time_4 = ft.Container(
        visible=False,
        shadow=ft.BoxShadow(
            blur_radius=2,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(0, 2),
            color=ft.colors.BLACK54
        ),
        bgcolor='#ffcc66',
        border_radius=5,
        padding=10,
        content=ft.Text(
            four,
            size=21,
            weight='w500',
            color=ft.colors.BLACK,
            font_family="Golos Text"
        )
    )

    time_5 = ft.Container(
        visible=False,
        shadow=ft.BoxShadow(
            blur_radius=2,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(0, 2),
            color=ft.colors.BLACK54
        ),
        bgcolor='#ffcc66',
        border_radius=5,
        padding=10,
        content=ft.Text(
            five,
            size=21,
            weight='w500',
            color=ft.colors.BLACK,
            font_family="Golos Text"
        )
    )

    time_6 = ft.Container(
        visible=False,
        shadow=ft.BoxShadow(
            blur_radius=2,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(0, 2),
            color=ft.colors.BLACK54
        ),
        bgcolor='#ffcc66',
        border_radius=5,
        padding=10,
        content=ft.Text(
            six,
            size=21,
            weight='w500',
            color=ft.colors.BLACK,
            font_family="Golos Text"
        )
    )

    all_time = ft.Row(
        visible=False,
        alignment='center',
        vertical_alignment='center',
        wrap=True,
        spacing=9,
        controls=[
            time_1,
            time_2,
            time_3,
            time_4,
            time_5,
            time_6,
        ]
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

    main_info = ft.Container(
        blur=10,
        padding=15,
        bgcolor=ft.colors.BLACK26,
        border_radius=15,
        content=ft.Column(
            horizontal_alignment='center',
            alignment="center",
            controls=[
                ft.Text(
                    "Графік відключень:",
                    size=24,
                    weight='w500',
                    color=ft.colors.BLACK87,
                    font_family="Golos Text",
                    text_align='center'
                ),
                ft.Divider(
                    height=1,
                    thickness=1,
                    color=ft.colors.BLACK38
                ),
                progress_bar,
                all_time
            ]
        )
    )

    expand_container = ft.SafeArea(
        ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment='center',
                horizontal_alignment='center',
                scroll=ft.ScrollMode.ADAPTIVE,
                controls=[
                    lamp_img,
                    main_info
                ]
            )
        ),
        expand=True
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
                expand_container,
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
