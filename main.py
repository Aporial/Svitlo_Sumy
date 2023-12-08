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
            open_list()
        if my_index == 1:
            info_tab.visible = False
            page.update()
        if my_index == 2:
            info_tab.visible = True
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
            height=300,
            width=300,

        )
    )
    lamp_off = ft.Container(
        visible=False,
        content=ft.Image(
            src=f"/Images/lamp_off.png",
            height=300,
            width=300,

        )
    )



    # page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.add(info_tab, lamp_on, lamp_off)
    page.overlay.append(bs)
    page.update()


ft.app(
    target=main,
    assets_dir='assets'
)
