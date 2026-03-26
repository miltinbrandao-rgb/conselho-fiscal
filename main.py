import flet as ft
import dashboard  # Importa o seu arquivo dashboard.py

def main(page: ft.Page):
    dashboard.main(page)  # Chama a função main que está lá dentro

if __name__ == "__main__":
    ft.app(target=main)
