import flet as ft
from ui.layout import build_layout

def main(page: ft.Page):
    build_layout(page)  # Build the main UI layout
    page.theme = ft.Theme(color_scheme_seed="#F5F5F5", use_material3=True)
    page.bgcolor = "#F5F5F5"
    page.padding = 10
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
