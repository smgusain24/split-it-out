import flet as ft

from splitapp.logic.validators import validate_name, validate_contribution
from splitapp.ui.colors import COLORS
from splitapp.ui.result import display_result
from splitapp.ui.table import create_contribution_table, add_contribution


def build_layout(page: ft.Page):
    contributions = {}

    # Input Fields and Errors
    name_error = ft.Text(value="", color=COLORS["error"])
    contribution_error = ft.Text(value="", color=COLORS["error"])

    name_input = ft.TextField(
        label="Name", expand=True, bgcolor=COLORS["background"], border_color=COLORS["secondary"], color=COLORS["text"],
        keyboard_type=ft.KeyboardType.TEXT, cursor_color="#000000",
        on_change=lambda e: validate_name(e, name_error, add_contribution_btn, page)
    )

    contribution_input = ft.TextField(
        label="Contribution", expand=True, keyboard_type=ft.KeyboardType.NUMBER, bgcolor=COLORS["background"],
        border_color=COLORS["secondary"], color=COLORS["text"], cursor_color="#000000",
        on_change=lambda e: validate_contribution(e, contribution_error, add_contribution_btn, page)
    )

    # Table for contributions
    contribution_table = create_contribution_table(page)

    # Add contribution button
    add_contribution_btn = ft.ElevatedButton("Add Contribution",
                                             on_click=lambda e: add_contribution(contributions, name_input,
                                                                                 contribution_input, contribution_table,
                                                                                 page), bgcolor=COLORS["primary"],
                                             color="#FFFFFF", disabled=True)

    calculate_btn = ft.ElevatedButton("Calculate Split",
                                      on_click=lambda e: display_result(contributions, result_text, page),
                                      bgcolor=COLORS["accent"], color="#FFFFFF")

    result_text = ft.Text("", color=COLORS["accent"], expand=True, font_family="Comic Sans MS")

    # Page Layout
    layout = ft.Column(
        controls=[
            ft.Text("Party Expense Splitter", style="headlineMedium", size=20, color=COLORS["text"]),
            name_input, name_error,
            contribution_input, contribution_error,
            ft.Row([add_contribution_btn, calculate_btn]),
            ft.Text("Contributions", style="titleMedium", color=COLORS["text"]),
            contribution_table,
            ft.Text("Results:", style="titleMedium", color=COLORS["text"]),
            result_text
        ],
        expand=True, scroll="auto"
    )

    page.add(layout)
