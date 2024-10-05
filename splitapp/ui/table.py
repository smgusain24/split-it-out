import flet as ft
from splitapp.ui.colors import COLORS


def create_contribution_table(page):
    return ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Name", color=COLORS["table_header"], weight=ft.FontWeight.BOLD, size=16)),
            ft.DataColumn(ft.Text("Contribution", color=COLORS["table_header"], weight=ft.FontWeight.BOLD, size=16)),
        ],
        rows=[]
    )

def add_contribution(contributions, name_input, contribution_input, contribution_table, page):
    name = name_input.value
    contribution = contribution_input.value
    if name and contribution:
        contributions[name] = float(contribution)
        row_bg_color = COLORS["table_row_bg"] if len(contribution_table.rows) % 2 == 0 else COLORS["table_row_alt_bg"]
        contribution_table.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(name, color=COLORS["text"], font_family="Comic Sans MS")),
                    ft.DataCell(ft.Text(contribution, color=COLORS["text"], font_family="Comic Sans MS")),
                ],
                color=row_bg_color
            )
        )
        page.update()
        name_input.value = ""
        contribution_input.value = ""
        name_input.focus()
        page.update()
