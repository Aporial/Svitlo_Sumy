from flet import *
from datetime import datetime


def main(page: Page):
    day = "28.11.2024"

    day_container = Container(
        blur=10,
        padding=1,
        bgcolor=colors.BLACK26,
        border_radius=15,
        content=Text(
            f" {day} ",
            size=60,
            weight='w500',
            color='#ffcc66',
            font_family="Golos Text"
        )
    )

    logo = Container(
        content=Image(
            src=f"/icon.png",
            gapless_playback=True,
            height=500,
            width=500,
        )
    )

    title = Text(
        'Аварійні відключення',
        size=60,
        weight='w500',
        color=colors.BLACK,
        font_family="Golos Text"
    )

    head = Row(
        alignment='center',
        controls=[
            title,
            # day_container
        ]
    )

    main_container = Container(
        expand=True,
        gradient=LinearGradient(
            begin=alignment.top_right,
            end=alignment.bottom_left,
            colors=['#ffc366', '#ff6666']
        ),
        padding=15,
        content=Column(
            alignment='center',
            horizontal_alignment='center',
            # alignment=MainAxisAlignment.SPACE_AROUND,
            spacing=90,
            controls=[
                logo,
                head
            ]
        )
    )

    page.fonts = {
        "Golos Text": "/fonts/GolosText.ttf"
    }
    page.title = 'Svitlo Sumy'
    page.theme_mode = ThemeMode.LIGHT
    page.window.height = 1000
    page.window.width = 1000
    page.padding = 0
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window.center()
    page.window_resizable = False
    page.window.title_bar_hidden = True
    page.window.title_bar_buttons_hidden = True
    page.add(main_container)
    page.update()


app(
    target=main,
    name="Svitlo Sumy",
    assets_dir='assets',
)
