from flet import *
from chergs import *
from database_1 import db1_day_num_one, db1_day_num_two, db1_day_num_three, db1_day_num_four, db1_day_num_five, db1_day_num_six
from database_2 import db2_day_num_one, db2_day_num_two, db2_day_num_three, db2_day_num_four, db2_day_num_five, db2_day_num_six
from firebase import firebase


def main(page: Page):

    database_connection = firebase.FirebaseApplication(
        'https://svitlo-sumy-default-rtdb.europe-west1.firebasedatabase.app/', authentication=None)
    main_database = database_connection.get("/", None)
    database = main_database.get("database")
    print('DATABASE:', database)
    page.client_storage.set("database_storage", database)
    page.client_storage.set("main_database", main_database)

    

    def one_cherg():
        if page.client_storage.get("database_storage") == 1:
            day_num_one = db1_day_num_one
            day_num_two = db1_day_num_two
            day_num_three = db1_day_num_three
            day_num_four = db1_day_num_four
            day_num_five = db1_day_num_five
            day_num_six = db1_day_num_six
        if page.client_storage.get("database_storage") == 2:
            day_num_one = db2_day_num_one
            day_num_two = db2_day_num_two
            day_num_three = db2_day_num_three
            day_num_four = db2_day_num_four
            day_num_five = db2_day_num_five
            day_num_six = db2_day_num_six
            
        result_one = main_database.get("1_cherg").get(f"{day_num_one}")
        if result_one == None:
            one_cherg_1.visible = False
            print("One not found!")
        else:
            one_cherg_1.visible = True
            one_cherg_1.content = Row(
                alignment="center",
                vertical_alignment='center',
                controls=[
                    Text(
                        result_one,
                        size=21,
                        weight='w500',
                        color=colors.BLACK,
                        font_family="Golos Text"
                    )
                ]
            )
            page.update()
            print("One found!")
            

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
                        Text('1 черга'),
                        Container(
                            alignment=alignment.center,
                            padding=10,
                            content=Column(
                                scroll=ScrollMode.ADAPTIVE,
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=9,
                                controls=[
                                    one_cherg_1,
                                    one_cherg_2,
                                    one_cherg_3,
                                    one_cherg_4,
                                    one_cherg_5,
                                    one_cherg_6,
                                ]
                            )
                        )
                    ]
                ),
                Column(
                    controls=[
                        Text('2 черга'),
                        Container(
                            alignment=alignment.center,
                            padding=10,
                            content=Column(
                                scroll=ScrollMode.ADAPTIVE,
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=9,
                                controls=[
                                    two_cherg_1,
                                    two_cherg_2,
                                    two_cherg_3,
                                    two_cherg_4,
                                    two_cherg_5,
                                    two_cherg_6,
                                ]
                            )
                        )
                    ]
                ),
                Column(
                    controls=[
                        Text('3 черга'),
                        Container(
                            alignment=alignment.center,
                            padding=10,
                            content=Column(
                                scroll=ScrollMode.ADAPTIVE,
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=9,
                                controls=[
                                    three_cherg_1,
                                    three_cherg_2,
                                    three_cherg_3,
                                    three_cherg_4,
                                    three_cherg_5,
                                    three_cherg_6,
                                ]
                            )
                        )
                    ]
                ),
                Column(
                    controls=[
                        Text('4 черга'),
                        Container(
                            alignment=alignment.center,
                            padding=10,
                            content=Column(
                                scroll=ScrollMode.ADAPTIVE,
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=9,
                                controls=[
                                    four_cherg_1,
                                    four_cherg_2,
                                    four_cherg_3,
                                    four_cherg_4,
                                    four_cherg_5,
                                    four_cherg_6,
                                ]
                            )
                        )
                    ]
                ),
                Column(
                    controls=[
                        Text('5 черга'),
                        Container(
                            alignment=alignment.center,
                            padding=10,
                            content=Column(
                                scroll=ScrollMode.ADAPTIVE,
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=9,
                                controls=[
                                    five_cherg_1,
                                    five_cherg_2,
                                    five_cherg_3,
                                    five_cherg_4,
                                    five_cherg_5,
                                    five_cherg_6,
                                ]
                            )
                        )
                    ]
                ),
                Column(
                    controls=[
                        Text('6 черга'),
                        Container(
                            alignment=alignment.center,
                            padding=10,
                            content=Column(
                                scroll=ScrollMode.ADAPTIVE,
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=9,
                                controls=[
                                    six_cherg_1,
                                    six_cherg_2,
                                    six_cherg_3,
                                    six_cherg_4,
                                    six_cherg_5,
                                    six_cherg_6,
                                ]
                            )
                        )
                    ]
                ),

            ]
        )
    )

    page.fonts = {
        "Golos Text": "/fonts/GolosText.ttf"
    }
    page.title = 'Svitlo Sumy'
    page.theme_mode = ThemeMode.LIGHT
    page.window_height = 500
    page.window_width = 700
    page.padding = 0
    # page.window_center()
    page.window_resizable = False
    # page.window_title_bar_hidden = True
    page.add(main_container)
    page.update()
    one_cherg()


app(
    target=main,
    name="Svitlo Sumy",
    assets_dir='assets',
)
