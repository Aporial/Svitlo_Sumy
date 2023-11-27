import flet as ft


def main(page: ft.Page):
    text = ft.Text(value="Helljjjjjjjjjo Wold", color='Green')
    page.controls.append(text)
    page.update()


ft.app(target=main)
