import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.title = 'Svitlo'
    page.navigation_bar = ft.NavigationBar(height=80, bgcolor = ft.colors.BLACK,
        destinations = [
            ft.NavigationDestination(icon=ft.icons.LIST_ROUNDED, label='Черги'),
            ft.NavigationDestination(icon=ft.icons.HOME_ROUNDED, label='Головна'),
            ft.NavigationDestination(icon=ft.icons.INFO, selected_icon=ft.icons.INFO_OUTLINE, label='Інформація')
        ]
    )
    c1 = ft.Container(
        content=ft.Text('Перша Черга:', size=20),
        alignment=ft.alignment.center,
        margin=10,
        width=600,
        height=100,
        padding=10,
        border_radius=10,
        bgcolor=ft.colors.RED,
    )
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.add(c1)
    page.update()


ft.app(target=main)