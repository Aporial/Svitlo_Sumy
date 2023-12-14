import flet as ft
import sqlite3
from functions import day_num, check_cherg
from datetime import datetime
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
import requests

URL = "https://github.com/Aporial/Svitlo/blob/main/assets/DATA_BASE.db?raw=true"
response = requests.get(URL)
open("assets/DATA_BASE.db", "wb").write(response.content)


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
            weight='w500',
            color=ft.colors.BLACK,
            font_family="Golos Text"
        )
        time_2.content = ft.Text(
            two,
            size=21,
            weight='w500',
            color=ft.colors.BLACK,
            font_family="Golos Text"
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
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
                )
                time_2.content = ft.Text(
                    two,
                    size=21,
                    weight='w500',
                    color=ft.colors.BLACK,
                    font_family="Golos Text"
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

    def save_device_rez():
        if page.client_storage.get("page_height") == None:
            page.client_storage.set("page_height", page.height)
            page.client_storage.set("page_width", page.width)
        main_container.height = page.client_storage.get("page_height")
        main_container.width = page.client_storage.get("page_wight")
        page.update()

    one = page.client_storage.get("one")
    two = page.client_storage.get("two")

    page_height = page.client_storage.get("page_height")
    page_width = page.client_storage.get("page_width")

    time_1 = ft.Container(
        visible=True,
        # gradient=ft.LinearGradient(
        #     begin=ft.alignment.top_center,
        #     end=ft.alignment.bottom_center,
        #     colors=[ft.colors.ORANGE_700, ft.colors.RED]
        # ),
        shadow=ft.BoxShadow(
            blur_radius=2,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(0, 2),
            color=ft.colors.BLACK54
        ),
        bgcolor='#ffcc66',
        border_radius=5,
        padding=1,
        height=50,
        width=150,
        alignment=ft.alignment.center,
        content=ft.Text(
            one,
            size=21,
            weight='w500',
            color=ft.colors.BLACK,
            font_family="Golos Text"
        )
    )

    time_2 = ft.Container(
        visible=True,
        # gradient=ft.LinearGradient(
        #     begin=ft.alignment.top_center,
        #     end=ft.alignment.bottom_center,
        #     colors=[ft.colors.ORANGE_700, ft.colors.RED]
        # ),
        shadow=ft.BoxShadow(
            blur_radius=2,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(0, 2),
            color=ft.colors.BLACK54
        ),
        bgcolor='#ffcc66',
        border_radius=5,
        padding=5,
        height=50,
        width=150,
        alignment=ft.alignment.center,
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
        # gradient=ft.LinearGradient(
        #     begin=ft.alignment.top_center,
        #     end=ft.alignment.bottom_center,
        #     colors=[ft.colors.ORANGE_700, ft.colors.RED]
        # ),
        shadow=ft.BoxShadow(
            blur_radius=6,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(0, 5),
            color=ft.colors.BLACK87
        ),
        bgcolor='#ffcc66',
        border_radius=5,
        padding=3,
        height=50,
        width=150,
        alignment=ft.alignment.center,
        content=ft.Text(
            '10:00-12:00',
            size=21,
            weight='w600',
            color=ft.colors.WHITE,
        )
    )

    time_4 = ft.Container(
        visible=False,
        # gradient=ft.LinearGradient(
        #     begin=ft.alignment.top_center,
        #     end=ft.alignment.bottom_center,
        #     colors=[ft.colors.ORANGE_700, ft.colors.RED]
        # ),
        shadow=ft.BoxShadow(
            blur_radius=6,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(0, 5),
            color=ft.colors.BLACK87
        ),
        bgcolor='#ffcc66',
        border_radius=5,
        padding=3,
        height=50,
        width=150,
        alignment=ft.alignment.center,
        content=ft.Text(
            '4',
            size=21,
            weight='w600',
            color=ft.colors.BLACK,
        )
    )

    time_5 = ft.Container(
        visible=False,
        # gradient=ft.LinearGradient(
        #     begin=ft.alignment.top_center,
        #     end=ft.alignment.bottom_center,
        #     colors=[ft.colors.ORANGE_700, ft.colors.RED]
        # ),
        shadow=ft.BoxShadow(
            blur_radius=6,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(0, 5),
            color=ft.colors.BLACK87
        ),
        bgcolor=ft.colors.AMBER_600,
        border_radius=5,
        padding=3,
        height=50,
        width=150,
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
        # gradient=ft.LinearGradient(
        #     begin=ft.alignment.top_center,
        #     end=ft.alignment.bottom_center,
        #     colors=[ft.colors.ORANGE_700, ft.colors.RED]
        # ),
        shadow=ft.BoxShadow(
            blur_radius=6,
            blur_style=ft.ShadowBlurStyle.NORMAL,
            offset=ft.Offset(0, 5),
            color=ft.colors.BLACK87
        ),
        bgcolor=ft.colors.AMBER_600,
        border_radius=5,
        padding=3,
        height=50,
        width=150,
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
                ft.ElevatedButton(content=ft.Text("Перша", size=22, weight='w500', font_family="Golos Text"),
                                  style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15), overlay_color=ft.colors.AMBER_200), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor='#ffcc66', on_click=cherg_choise, data=1),
                ft.ElevatedButton(content=ft.Text("Друга", size=22, weight='w500', font_family="Golos Text"),
                                  style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15), overlay_color=ft.colors.AMBER_200), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor='#ffcc66', on_click=cherg_choise, data=2),
                ft.ElevatedButton(content=ft.Text("Третя", size=22, weight='w500', font_family="Golos Text"),
                                  style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15), overlay_color=ft.colors.AMBER_200), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor='#ffcc66', on_click=cherg_choise, data=3),
                ft.ElevatedButton(content=ft.Text("Четверта", size=22, weight='w500', font_family="Golos Text"),
                                  style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15), overlay_color=ft.colors.AMBER_200), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor='#ffcc66', on_click=cherg_choise, data=4),
                ft.ElevatedButton(content=ft.Text("П'ята", size=22, weight='w500', font_family="Golos Text"),
                                  style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15), overlay_color=ft.colors.AMBER_200), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor='#ffcc66', on_click=cherg_choise, data=5),
                ft.ElevatedButton(content=ft.Text("Шоста", size=22, weight='w500', font_family="Golos Text"),
                                  style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15), overlay_color=ft.colors.AMBER_200), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor='#ffcc66', on_click=cherg_choise, data=6),
                ft.Container(height=10)
            ]
        ),
        bgcolor=ft.colors.WHITE,
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
        blur=10,
        # shadow=ft.BoxShadow(
        #     blur_radius=2,
        #     blur_style=ft.ShadowBlurStyle.NORMAL,
        #     offset=ft.Offset(0, 2),
        #     color=ft.colors.BLACK54
        # ),
        padding=15,
        bgcolor=ft.colors.BLACK26,
        border_radius=15,
        content=ft.Column(
            horizontal_alignment='center',
            controls=[
                ft.Text(
                    "Графік відключень:",
                    size=25,
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

    info_tab = ft.Container(
        blur=10,
        # shadow=ft.BoxShadow(
        #     blur_radius=2,
        #     blur_style=ft.ShadowBlurStyle.NORMAL,
        #     offset=ft.Offset(0, 2),
        #     color=ft.colors.BLACK87
        # ),
        visible=False,
        bgcolor=ft.colors.BLACK12,
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
                    weight="w400",
                    font_family="Golos Text",
                    text_align="center"
                ),
                ft.Divider(height=0.1, color=ft.colors.BLACK26),
                ft.Text(
                    "Застосунок розроблений для безкоштовного користування.",
                    size=16,
                    color='black',
                    text_align='center',
                    font_family="Golos Text",
                    weight="w500"
                ),
                ft.Divider(height=0.1, color=ft.colors.BLACK26),
                ft.Text(
                    "Головна мета - максимально спростити пошук актуальної інформації про відключення світла.",
                    size=16,
                    color='black',
                    text_align='center',
                    font_family="Golos Text",
                    weight="w500"
                ),
                ft.Divider(height=0.1, color=ft.colors.BLACK26),
                ft.Text(
                    "В застосунку немає та не буде жодної реклами. Якщо ви хочете підтримати розробника - нижче залишу банку з монобанку.",
                    size=16,
                    color='black',
                    text_align='center',
                    font_family="Golos Text",
                    weight="w500"
                ),
                ft.Divider(height=0.1, color=ft.colors.BLACK26),
                ft.TextButton(
                    style=ft.ButtonStyle(overlay_color=ft.colors.AMBER_200),
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

    main_container = ft.Container(
        height=page_height,
        width=page_width,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_right,
            end=ft.alignment.bottom_left,
            colors=['#ffcc66', '#ff6666']
            # colors=[ft.colors.AMBER, ft.colors.RED]
        ),
        padding=15,
        content=ft.Column(
            horizontal_alignment='center',
            alignment='center',
            controls=[
                lamp_img,
                main_info,
                info_tab,
                ft.Container(height=65)
            ]
        ),
    )

    page.fonts = {
        "Golos Text": "/fonts/GolosText.ttf"
    }
    page.title = 'Svitlo Sumy'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.BLUE_GREY_50
    page.window_height = 700
    page.window_width = 400
    page.padding = 0
    # page.window_center()
    page.window_resizable = True
    page.navigation_bar = ft.NavigationBar(surface_tint_color='#ffcc66',
                                           indicator_color='#ffcc66',
                                           height=65,
                                           bgcolor=ft.colors.WHITE,
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
    page.update()
    check_storage()
    save_device_rez()


ft.app(
    target=main,
    assets_dir='assets',
)
