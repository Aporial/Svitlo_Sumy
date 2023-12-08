import flet as ft


def main(page: ft.Page):
    def open_list():
        bs.open = True
        page.navigation_bar.selected_index = 1
        info_tab.visible = False
        bs.update()
        page.update()

    def close_list(e):
        bs.open = False
        bs.update()

    def on_tab(e):
        my_index = e.control.selected_index
        if my_index == 0:
            main_info.visible = True
            lamp_on.visible = True
            lamp_off.visible = False
            info_tab.visible = False
            open_list()
        if my_index == 1:
            main_info.visible = True
            lamp_on.visible = True
            lamp_off.visible = False
            info_tab.visible = False
            page.update()
        if my_index == 2:
            info_tab.visible = True
            main_info.visible = False
            lamp_on.visible = False
            lamp_off.visible = False
            page.update()

    page.title = 'Svitlo Sumy'
    page.bgcolor = ft.colors.BLACK
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
                ft.ElevatedButton(content=ft.Text("Перша черга", size=20, weight='w600'), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor=ft.colors.WHITE, on_click=close_list),
                ft.ElevatedButton(content=ft.Text("Друга черга", size=20, weight='w600'), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor=ft.colors.WHITE, on_click=close_list),
                ft.ElevatedButton(content=ft.Text("Третя черга", size=20, weight='w600'), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor=ft.colors.WHITE, on_click=close_list),
                ft.ElevatedButton(content=ft.Text("Четверта черга", size=20, weight='w600'), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor=ft.colors.WHITE, on_click=close_list),
                ft.ElevatedButton(content=ft.Text("П'ята черга", size=20, weight='w600'), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor=ft.colors.WHITE, on_click=close_list),
                ft.ElevatedButton(content=ft.Text("Шоста черга", size=20, weight='w600'), width=250, height=50,
                                  color=ft.colors.BLACK, bgcolor=ft.colors.WHITE, on_click=close_list),
            ]
        ),
        bgcolor='gray',
        # show_drag_handle=True,
    )

    info_tab = ft.Column(
        visible=False,
        controls=[
            ft.Container(
                bgcolor=ft.colors.WHITE,
                height=580,
                width=400,
                border_radius=50,
                content=ft.Column(
                    horizontal_alignment='center',
                    alignment='start',
                    controls=[
                        ft.Text(
                            'Інформація',
                            size=50,
                            color=ft.colors.BLACK87,
                            weight='bolt',
                        ),
                    ]
                )
            )
        ]
    )

    lamp_on = ft.Container(
        visible=True,
        content=ft.Image(
            src=f"/Images/lamp_on.png",
            height=200,
            width=200,

        )
    )
    lamp_off = ft.Container(
        visible=False,
        content=ft.Image(
            src=f"/Images/lamp_off.png",
            height=200,
            width=200,

        )
    )

    main_info = ft.Container(
        padding=20,
        bgcolor=ft.colors.WHITE,
        # height=350,
        # width=400,
        border_radius=30,
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
                ft.Container(
                    bgcolor='black',
                    # height=100,
                    # width=350,
                    border_radius=20,
                    padding=15,
                    content=ft.Column(
                        horizontal_alignment='center',
                        controls=[
                            ft.Text(
                                "Години відключень:",
                                size=16,
                                weight='w600',
                            ),
                            ft.Row(
                                alignment='center',
                                wrap=True,
                                controls=[
                                    ft.Container(
                                        visible=True,
                                        bgcolor=ft.colors.RED,
                                        border_radius=5,
                                        padding=3,
                                        height=35,
                                        width=110,
                                        alignment=ft.alignment.center,
                                        content=ft.Text(
                                            "00:00-02:00",
                                            size=18,
                                            weight='w600',
                                            color=ft.colors.BLACK,
                                        )
                                    ),
                                    ft.Container(
                                        visible=True,
                                        bgcolor=ft.colors.RED,
                                        border_radius=5,
                                        padding=3,
                                        height=35,
                                        width=110,
                                        alignment=ft.alignment.center,
                                        content=ft.Text(
                                            "04:00-06:00",
                                            size=18,
                                            weight='w600',
                                            color=ft.colors.BLACK,
                                        )
                                    ),
                                    ft.Container(
                                        visible=True,
                                        bgcolor=ft.colors.RED,
                                        border_radius=5,
                                        padding=3,
                                        height=35,
                                        width=110,
                                        alignment=ft.alignment.center,
                                        content=ft.Text(
                                            "08:00-10:00",
                                            size=18,
                                            weight='w600',
                                            color=ft.colors.BLACK,
                                        )
                                    ),
                                    ft.Container(
                                        visible=True,
                                        bgcolor=ft.colors.RED,
                                        border_radius=5,
                                        padding=3,
                                        height=35,
                                        width=110,
                                        alignment=ft.alignment.center,
                                        content=ft.Text(
                                            "12:00-14:00",
                                            size=18,
                                            weight='w600',
                                            color=ft.colors.BLACK,
                                        )
                                    ),
                                    ft.Container(
                                        visible=True,
                                        bgcolor=ft.colors.RED,
                                        border_radius=5,
                                        padding=3,
                                        height=35,
                                        width=110,
                                        alignment=ft.alignment.center,
                                        content=ft.Text(
                                            "16:00-18:00",
                                            size=18,
                                            weight='w600',
                                            color=ft.colors.BLACK,
                                        )
                                    ),
                                    ft.Container(
                                        visible=True,
                                        bgcolor=ft.colors.RED,
                                        border_radius=5,
                                        padding=3,
                                        height=35,
                                        width=110,
                                        alignment=ft.alignment.center,
                                        content=ft.Text(
                                            "20:00-22:00",
                                            size=18,
                                            weight='w600',
                                            color=ft.colors.BLACK,
                                        )
                                    ),
                                ]
                            )
                        ]
                    )
                ),
                # ft.Container(
                #     bgcolor=ft.colors.GREEN,
                #     height=170,
                #     width=350,
                #     border_radius=20,
                #     content=ft.Column(
                #         horizontal_alignment='center',
                #         controls=[
                #             ft.Text(
                #                 "Зараз світло:",
                #                 size=16,
                #             )
                #         ]
                #     )
                # )
            ]
        )
    )

    # page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.add(info_tab, lamp_on, lamp_off, main_info)
    page.overlay.append(bs)
    page.update()


ft.app(
    target=main,
    assets_dir='assets'
)
