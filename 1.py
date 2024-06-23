from flet import *


def main(page: Page):
    aboba = Text('aboba')
    aboba1 = Text('aboba1')
    aboba2 = Text('aboba2')
    one = DataRow(
        cells=[]
    )
    def start():
        one.cells.append(DataCell(aboba))
    def start1():
        one.cells.append(DataCell(aboba1))
    def start2():
        one.cells.append(DataCell(Text()))
    page.add(
        DataTable(
            columns=[
                DataColumn(Text("First name")),
                DataColumn(Text("Last name")),
                DataColumn(Text("Age"), numeric=True),
            ],
            rows=[
                one,
                DataRow(
                    cells=[
                        DataCell(Text("Jack")),
                        DataCell(Text("Brown")),
                        DataCell(Text("19")),
                    ],
                ),
                DataRow(
                    cells=[
                        DataCell(Text("Alice")),
                        DataCell(Text("Wong")),
                        DataCell(Text("25")),
                    ],
                ),
            ],
        ),
    )
    start()
    start1()
    start2()
    page.update()

app(target=main)
