import flet as ft
import sqlite3
from functions import day_num, check_cherg
from datetime import datetime
from urllib.request import urlretrieve

# URL = "https://github.com/Aporial/Svitlo/blob/bd55ffb5ffc04a250201e0b0b33cec260275b805/assets/DATA_BASE.db?raw=true"
# urlretrieve(URL, "assets/DATA_BASE.db")


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
            main_info.visible = True
            lamp_img.visible = True
            info_tab.visible = False
            open_list()
        if my_index == 1:
            main_info.visible = True
            info_tab.visible = False
            lamp_img.visible = True
            page.update()
        if my_index == 2:
            info_tab.visible = True
            main_info.visible = False
            lamp_img.visible = False
            page.update()

    def mono_click(e):
        page.launch_url('https://send.monobank.ua/jar/7rkGHNfQpV',
                        web_window_name='Monobank')

    def cherg_choise(e):
        numb_cherg = e.control.data
        page.client_storage.set("number", numb_cherg)
        bs.open = False
        bs.update()
        DB_NAME = "assets/DATA_BASE.db"
        sqlite_conn = sqlite3.connect(DB_NAME)
        storage_info = storage()
        cherg = check_cherg(storage_info)
        sql_request = f"SELECT {day_num} FROM '{cherg}'"
        sql_cursor = sqlite_conn.execute(sql_request)
        result_one = sql_cursor.fetchone()[0]
        result_two = sql_cursor.fetchone()[0]
        page.client_storage.set("one", result_one)
        page.client_storage.set("two", result_two)
        one_check = page.client_storage.get("one")
        two_check = page.client_storage.get("two")
        if page.client_storage.get("one") == '22:00-23:59':
            one = '22:00-24:00'
        else:
            one = page.client_storage.get("one")
        if page.client_storage.get("two") == '22:00-23:59':
            two = '22:00-24:00'
        else:
            two = page.client_storage.get("two")
        if check_time_interval(one_check) == True:
            pass
        else:
            check_time_interval(two_check)
        time_1.content = ft.Text(
            one,
            size=21,
            weight='w600',
            color=ft.colors.BLACK,
        )
        time_2.content = ft.Text(
            two,
            size=21,
            weight='w600',
            color=ft.colors.BLACK,
        )
        page.update()

    def check_storage():
        if page.client_storage.get("number") == None:
            open_list()
        else:
            DB_NAME = "assets/DATA_BASE.db"
            with sqlite3.connect(DB_NAME) as sqlite_conn:
                storage_info = storage()
                cherg = check_cherg(storage_info)
                sql_request = f"SELECT {day_num} FROM '{cherg}'"
                sql_cursor = sqlite_conn.execute(sql_request)
                result_one = sql_cursor.fetchone()[0]
                result_two = sql_cursor.fetchone()[0]
                page.client_storage.set("one", result_one)
                page.client_storage.set("two", result_two)
                one_check = page.client_storage.get("one")
                two_check = page.client_storage.get("two")
                if page.client_storage.get("one") == '22:00-23:59':
                    one = '22:00-24:00'
                else:
                    one = page.client_storage.get("one")
                if page.client_storage.get("two") == '22:00-23:59':
                    two = '22:00-24:00'
                else:
                    two = page.client_storage.get("two")
                if check_time_interval(one_check) == True:
                    pass
                else:
                    check_time_interval(two_check)
                time_1.content = ft.Text(
                    one,
                    size=21,
                    weight='w600',
                    color=ft.colors.BLACK,
                )
                time_2.content = ft.Text(
                    two,
                    size=21,
                    weight='w600',
                    color=ft.colors.BLACK,
                )
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

    page.title = 'Svitlo Sumy'
    page.bgcolor = ft.colors.BLACK
    page.theme_mode = ft.ThemeMode.DARK
    page.window_height = 700
    page.window_width = 400
    page.window_resizable = True
    page.navigation_bar = ft.NavigationBar(height=80, bgcolor=ft.colors.BLACK, on_change=on_tab, selected_index=1,
                                           destinations=[
                                               ft.NavigationDestination(
                                                   icon=ft.icons.LIST_ROUNDED, label='Черги',),
                                               ft.NavigationDestination(
                                                   icon=ft.icons.HOME_ROUNDED, label='Головна'),
                                               ft.NavigationDestination(
                                                   icon=ft.icons.INFO, selected_icon=ft.icons.INFO_OUTLINE, label='Інформація')
                                           ]
                                           )

    one = page.client_storage.get("one")
    two = page.client_storage.get("two")

    time_1 = ft.Container(
        visible=True,
        bgcolor=ft.colors.RED,
        border_radius=5,
        padding=1,
        height=50,
        width=145,
        alignment=ft.alignment.center,
        content=ft.Text(
            one,
            size=21,
            weight='w600',
            color=ft.colors.BLACK,
        )
    )

    time_2 = ft.Container(
        visible=True,
        bgcolor=ft.colors.RED,
        border_radius=5,
        padding=5,
        height=50,
        width=145,
        alignment=ft.alignment.center,
        content=ft.Text(
            two,
            size=21,
            weight='w600',
            color=ft.colors.BLACK,
        )
    )

    time_3 = ft.Container(
        visible=False,
        bgcolor=ft.colors.RED,
        border_radius=5,
        padding=3,
        height=50,
        width=145,
        alignment=ft.alignment.center,
        content=ft.Text(
            '22:00-24:00',
            size=21,
            weight='w600',
            color=ft.colors.BLACK,
        )
    )

    time_4 = ft.Container(
        visible=False,
        bgcolor=ft.colors.RED,
        border_radius=5,
        padding=3,
        height=50,
        width=145,
        alignment=ft.alignment.center,
        content=ft.Text(
            '22:00-24:00',
            size=21,
            weight='w600',
            color=ft.colors.BLACK,
        )
    )

    time_5 = ft.Container(
        visible=False,
        bgcolor=ft.colors.RED,
        border_radius=5,
        padding=3,
        height=50,
        width=145,
        alignment=ft.alignment.center,
        content=ft.Text(
            '22:00-24:00',
            size=21,
            weight='w600',
            color=ft.colors.BLACK,
        )
    )

    time_6 = ft.Container(
        visible=False,
        bgcolor=ft.colors.RED,
        border_radius=5,
        padding=3,
        height=50,
        width=145,
        alignment=ft.alignment.center,
        content=ft.Text(
            '22:00-24:00',
            size=21,
            weight='w600',
            color=ft.colors.BLACK,
        )
    )

    bs = ft.BottomSheet(
        content=ft.Column(
            horizontal_alignment='center',
            alignment='center',
            width=400,
            spacing=5,
            controls=[
                ft.Text(
                    "Виберіть чергу:",
                    size=20,
                    weight='w500',
                    text_align='center',
                ),
                ft.ElevatedButton(content=ft.Text("Перша", size=20, weight='w600'), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor=ft.colors.WHITE, on_click=cherg_choise, data=1),
                ft.ElevatedButton(content=ft.Text("Друга", size=20, weight='w600'), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor=ft.colors.WHITE, on_click=cherg_choise, data=2),
                ft.ElevatedButton(content=ft.Text("Третя", size=20, weight='w600'), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor=ft.colors.WHITE, on_click=cherg_choise, data=3),
                ft.ElevatedButton(content=ft.Text("Четверта", size=20, weight='w600'), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor=ft.colors.WHITE, on_click=cherg_choise, data=4),
                ft.ElevatedButton(content=ft.Text("П'ята", size=20, weight='w600'), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor=ft.colors.WHITE, on_click=cherg_choise, data=5),
                ft.ElevatedButton(content=ft.Text("Шоста", size=20, weight='w600'), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor=ft.colors.WHITE, on_click=cherg_choise, data=6),
            ]
        ),
        bgcolor=ft.colors.GREY_900,
    )

    lamp_img = ft.Container(
        visible=True,
        content=ft.Image(
            # src=f"https://github.com/Aporial/Svitlo/blob/main/assets/Images/lamp_off.png?raw=true",
            src=f"/Images/lamp_on.png",
            height=280,
            width=280,
        )
    )

    main_info = ft.Container(
        padding=15,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        content=ft.Column(
            horizontal_alignment='center',
            controls=[
                ft.Text(
                    "Графік відключень:",
                    size=25,
                    weight='w600',
                    color='black',
                ),
                ft.Divider(
                    height=1,
                    thickness=1,
                    color=ft.colors.BLACK38
                ),
                ft.Row(
                    alignment='center',
                    vertical_alignment='center',
                    wrap=True,
                    controls=[
                        time_1,
                        time_2,
                        time_3,
                        time_4,
                        time_5,
                        time_6,
                    ]
                ),
            ]
        )
    )

    info_tab = ft.Column(
        visible=False,
        horizontal_alignment='center',
        controls=[
            ft.Container(height=5),
            ft.Container(
                bgcolor=ft.colors.WHITE,
                border_radius=15,
                padding=15,
                content=ft.Column(
                    horizontal_alignment='center',
                    alignment='start',
                    controls=[
                        ft.Text(
                            'Інформація',
                            size=35,
                            color=ft.colors.BLACK87,
                            weight='bolt',
                        ),
                        ft.Divider(height=0.1),
                        ft.Text(
                            "Застосунок розроблений для безкоштовного користування.",
                            size=16,
                            color='black',
                            text_align='center'
                        ),
                        ft.Divider(height=0.1),
                        ft.Text(
                            "Головна мета - максимально спростити пошук актуальної інформації про відключення світла.",
                            size=16,
                            color='black',
                            text_align='center'
                        ),
                        ft.Divider(height=0.1),
                        ft.Text(
                            "В застосунку немає та не буде жодної реклами. Якщо ви хочете підтримати розробника - нижче залишу банку з монобанку.",
                            size=16,
                            color='black',
                            text_align='center'
                        ),
                        ft.Divider(height=0.1),
                        ft.TextButton(
                            on_click=mono_click,
                            content=ft.Image(
                                # src=f"https://github.com/Aporial/Svitlo/blob/main/assets/Images/monobanka.png?raw=true",
                                src=f"/Images/monobanka.png",
                                height=100,
                                width=100,
                            )
                        )
                    ]
                )
            )
        ]
    )

    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.add(lamp_img, main_info, info_tab)
    page.overlay.append(bs)
    page.update()
    check_storage()


ft.app(
    target=main,
    assets_dir='assets',
)
