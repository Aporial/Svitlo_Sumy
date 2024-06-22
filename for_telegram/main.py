from flet import *


def main(page: Page):

    main_container = Container(
        expand=True,
        gradient=LinearGradient(
            begin=alignment.top_right,
            end=alignment.bottom_left,
            colors=['#ffcc66', '#ff6666']
        ),
        padding=15,
        content=Row(
            controls=[
                Column(
                    controls=[
                        Text('1'),
                        Container(width=10, height=10, bgcolor=colors.WHITE)]
                ),
                Column(
                    controls=[Text('2')]
                ),
                Column(
                    controls=[Text('3')]
                ),
                Column(
                    controls=[Text('4')]
                ),
                Column(
                    controls=[Text('5')]
                ),
                Column(
                    controls=[Text('6')]
                ),

            ]
        )
    )

    page.fonts = {
        "Golos Text": "/fonts/GolosText.ttf"
    }
    page.title = 'Svitlo Sumy'
    page.theme_mode = ThemeMode.LIGHT
    page.window_height = 400
    page.window_width = 700
    page.padding = 0
    page.window_center()
    page.window_resizable = False
    # page.window_title_bar_hidden = True
    page.add(main_container)
    page.update()


app(
    target=main,
    name="Svitlo Sumy",
    assets_dir='assets',
)
