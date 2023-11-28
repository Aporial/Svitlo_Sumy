import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.title = 'Svitlo'
    page.navigation_bar = ft.NavigationBar(height=80, bgcolor=ft.colors.BLACK,
                                           destinations=[
                                               ft.NavigationDestination(
                                                   icon=ft.icons.LIST_ROUNDED, label='Черги'),
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
        height=50,
        # width=200,
        padding=10,
        border_radius=10,
        bgcolor=ft.colors.RED,
    )
    name_cherg = ft.Container(
        content=ft.Text('06:00 - 08:00', size=20),
        alignment=ft.alignment.center,
        margin=10,
        height=100,
        padding=10,
        border_radius=10,
        bgcolor=ft.colors.GREEN,
    )
    img = ft.Image(
        src=f'/Images/lamp.jpg',
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    page.vertical_alignment = 'End'
    page.add(time_cherg, name_cherg)
    page.update()


ft.app(target=main)
