import flet as ft


def main(page: ft.Page):

    logo = ft.Image(
        src=f"/logo.png",
        height=150,
        width=150,
        border_radius=100,
    )

    lable_name = ft.Text(
        "Світло Суми",
            size=22,
            color=ft.colors.BLACK87,
            weight="w400",
            font_family="Golos Text",
            text_align="center"
    )

    lable_text = ft.Container(
        blur=10,
        bgcolor=ft.colors.BLACK12,
        border_radius=15,
        padding=15,
        alignment=ft.alignment.center,
        content=ft.Text(
            "1000 підписників",
            size=30,
            color=ft.colors.BLACK87,
            weight="w400",
            font_family="Golos Text",
            text_align="center"
        )
    )



    main_container = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_right,
            end=ft.alignment.bottom_left,
            colors=['#ffc366', '#ff6666']
        ),
        padding=15,
        content=ft.Column(
            horizontal_alignment='center',
            alignment='center',
            controls=[
                logo,
                lable_name,
                lable_text
            ]
        )
    )

    page.fonts = {
        "Golos Text": "/fonts/GolosText.ttf"
    }
    page.title = 'Svitlo Sumy'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_height = 350
    page.window_width = 350
    page.padding = 0
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    # page.window_center()
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.add(main_container)
    page.update()


ft.app(
    target=main,
    assets_dir='assets',
    name="Svitlo Sumy",
)
