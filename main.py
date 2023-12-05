import flet as ft


def main(page: ft.Page):
    def on_tab(e):
        my_index = e.control.selected_index
        if my_index == 0:
            img.visible = False
            name_cherg.visible = False
            time_cherg.visible = False
            info_tab.visible = False
            list_cherg2.visible = True
            page.update()
        if my_index == 1:
            img.visible = True
            name_cherg.visible = True
            time_cherg.visible = True
            info_tab.visible = False
            list_cherg2.visible = False
            page.update()
        if my_index == 2:
            img.visible = False
            name_cherg.visible = False
            time_cherg.visible = False
            info_tab.visible = True
            list_cherg2.visible = False
            page.update()
    page.bgcolor = ft.colors.BLACK
    page.title = 'Svitlo Sumy'
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
    time_cherg = ft.Container(
        content=ft.Text('Перша Черга:', size=20),
        alignment=ft.alignment.center,
        margin=10,
        height=60,
        # width=200,
        padding=10,
        border_radius=10,
        bgcolor=ft.colors.RED,
        visible=True

    )
    name_cherg = ft.Container(
        content=ft.Text('06:00 - 08:00', size=20),
        alignment=ft.alignment.center,
        margin=10,
        height=100,
        padding=10,
        border_radius=10,
        bgcolor=ft.colors.GREEN,
        visible=True
    )
    img = ft.Image(
        src=f'/Images/lamp.jpg',
        border_radius=10,
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
        visible=True
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
                        ft.Text(
                            'КОХАЮ ТЕТЯН!',
                            size=20,
                            color=ft.colors.BLACK38,
                        ),
                        ft.Text(
                            'КОХАЮ ТЕТЯН!',
                            size=20,
                            color=ft.colors.BLACK38,
                        ),
                        ft.Text(
                            'КОХАЮ ТЕТЯН!',
                            size=20,
                            color=ft.colors.BLACK38,
                        ),
                        ft.Text(
                            'КОХАЮ ТЕТЯН!',
                            size=20,
                            color=ft.colors.BLACK38,
                        ),
                        ft.Text(
                            'КОХАЮ ТЕТЯН!',
                            size=20,
                            color=ft.colors.BLACK38,
                        ),
                        ft.Text(
                            'КОХАЮ ТЕТЯН!',
                            size=20,
                            color=ft.colors.BLACK38,
                        ),
                        ft.Text(
                            'КОХАЮ ТЕТЯН!',
                            size=20,
                            color=ft.colors.BLACK38,
                        ),
                        ft.Text(
                            'КОХАЮ ТЕТЯН!',
                            size=20,
                            color=ft.colors.BLACK38,
                        ),
                        ft.Text(
                            'КОХАЮ ТЕТЯН!',
                            size=20,
                            color=ft.colors.BLACK38,
                        ),
                        ft.Text(
                            'КОХАЮ ТЕТЯН!',
                            size=20,
                            color=ft.colors.BLACK38,
                        ),
                        ft.Text(
                            'КОХАЮ ТЕТЯН!',
                            size=20,
                            color=ft.colors.BLACK38,
                        ),
                        ft.Text(
                            'КОХАЮ ТЕТЯН!',
                            size=20,
                            color=ft.colors.BLACK38,
                        ),

                    ]
                )
                
                



            )
        ]
    )

    list_cherg2 = ft.Column(
        visible=False,
        horizontal_alignment='center',
        spacing=18,
        controls=[
            ft.ElevatedButton(
                width=600,
                height=80,
                color=ft.colors.BLACK,
                bgcolor=ft.colors.WHITE,
                content=ft.Text(
                    'Перша черга',
                    color='black',
                    size=40,
                    weight='w500',
                )
            ),
            ft.ElevatedButton(
                width=600,
                height=80,
                color=ft.colors.BLACK,
                bgcolor=ft.colors.WHITE,
                content=ft.Text(
                    'Друга черга',
                    color='black',
                    size=40,
                    weight='w500',
                )
            ),
            ft.ElevatedButton(
                width=600,
                height=80,
                color=ft.colors.BLACK,
                bgcolor=ft.colors.WHITE,
                content=ft.Text(
                    'Третя черга',
                    color='black',
                    size=40,
                    weight='w500',
                )
            ),
            ft.ElevatedButton(
                width=600,
                height=80,
                color=ft.colors.BLACK,
                bgcolor=ft.colors.WHITE,
                content=ft.Text(
                    'Четверта черга',
                    color='black',
                    size=40,
                    weight='w500',
                )
            ),
            ft.ElevatedButton(
                width=600,
                height=80,
                color=ft.colors.BLACK,
                bgcolor=ft.colors.WHITE,
                content=ft.Text(
                    "П'ята черга",
                    color='black',
                    size=40,
                    weight='w500',
                )
            ),
            ft.ElevatedButton(
                width=600,
                height=80,
                color=ft.colors.BLACK,
                bgcolor=ft.colors.WHITE,
                content=ft.Text(
                    'Шоста черга',
                    color='black',
                    size=40,
                    weight='w500',
                )
            ),
        ]
    )

    list_cherg = ft.Column(
        visible=True,
        horizontal_alignment='center',
        spacing=18,
        controls=[
            ft.Container(
                bgcolor=ft.colors.WHITE,
                height=80,
                width=700,
                border_radius=20,
                alignment=ft.alignment.center,
                content=ft.Text(
                    'Перша черга',
                    size=50,
                    color='black',
                    text_align='center',
                    weight='w500'
                )
            ),
            ft.Container(
                bgcolor=ft.colors.WHITE,
                height=80,
                width=700,
                border_radius=20,
                alignment=ft.alignment.center,
                content=ft.Text(
                    'Друга черга',
                    size=50,
                    color='black',
                    text_align='center',
                    weight='w500'
                )
            ),
            ft.Container(
                bgcolor=ft.colors.WHITE,
                height=80,
                width=700,
                border_radius=20,
                alignment=ft.alignment.center,
                content=ft.Text(
                    'Третя черга',
                    size=50,
                    color='black',
                    text_align='center',
                    weight='w500'
                )
            ),
            ft.Container(
                bgcolor=ft.colors.WHITE,
                height=80,
                width=700,
                border_radius=20,
                alignment=ft.alignment.center,
                content=ft.Text(
                    'Четверта черга',
                    size=50,
                    color='black',
                    text_align='center',
                    weight='w500'
                )
            ),
            ft.Container(
                bgcolor=ft.colors.WHITE,
                height=80,
                width=700,
                border_radius=20,
                alignment=ft.alignment.center,
                content=ft.Text(
                    "П'ята черга",
                    size=50,
                    color='black',
                    text_align='center',
                    weight='w500'
                )
            ),
            ft.Container(
                bgcolor=ft.colors.WHITE,
                height=80,
                width=700,
                border_radius=20,
                alignment=ft.alignment.center,
                content=ft.Text(
                    'Шоста черга',
                    size=50,
                    color='black',
                    text_align='center',
                    weight='w500'
                )
            ),

        ]
    )
    
    page.vertical_alignment = 'End'
    page.add(img, time_cherg, name_cherg, info_tab, list_cherg2)
    page.update()


ft.app(
    target=main,
    assets_dir='assets'
)
