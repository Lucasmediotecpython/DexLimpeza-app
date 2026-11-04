
import flet as ft


def main(page: ft.Page):
    # Configurações da página
    page.title = "EcoStop"
    page.window.width = 360
    page.window.height = 740
    page.padding = 15
    page.bgcolor = "#FFFFFF"
    page.theme_mode = ft.ThemeMode.LIGHT

    cor_verde_principal = "#5cb85c"
    cor_verde_claro = "#7bc043"

    # Barra de pesquisa
    barra_pesquisa = ft.Container(
        padding=ft.Padding(left=20, right=10, top=8, bottom=8),
        bgcolor="#f2f2f2",
        border_radius=30,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(
                    "Pesquise",
                    color="#bdbdbd",
                    size=16,
                    weight=ft.FontWeight.W_500,
                ),
                ft.Container(
                    bgcolor=cor_verde_principal,
                    padding=8,
                    border_radius=20,
                    content=ft.Icon(
                        ft.Icons.MIC,
                        color="#FFFFFF",
                        size=20,
                    ),
                ),
            ],
        ),
    )

    # Mapa simulado
    mapa_simulado = ft.Container(
        expand=True,
        bgcolor="#e8eaed",
        border_radius=20,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        margin=ft.Margin.symmetric(vertical=15),
        content=ft.Stack(
            controls=[
                ft.Container(
                    width=400,
                    height=15,
                    bgcolor="#FFFFFF",
                    top=50,
                    left=-20,
                    rotate=0.3,
                ),
                ft.Container(
                    width=18,
                    height=600,
                    bgcolor="#FFFFFF",
                    top=-50,
                    left=140,
                    rotate=-0.1,
                ),
                ft.Container(
                    width=400,
                    height=18,
                    bgcolor="#FFFFFF",
                    top=350,
                    left=-50,
                    rotate=-0.5,
                ),
                ft.Container(
                    width=400,
                    height=12,
                    bgcolor="#FFFFFF",
                    top=450,
                    left=-50,
                    rotate=0.2,
                ),

                # Nomes das ruas
                ft.Text(
                    "R. São Sebastião",
                    top=200,
                    left=155,
                    color="#a0aab5",
                    weight=ft.FontWeight.BOLD,
                    rotate=1.47,
                ),
                ft.Text(
                    "R. Nazaré",
                    top=110,
                    left=200,
                    color="#a0aab5",
                    weight=ft.FontWeight.BOLD,
                    rotate=0.6,
                ),

                # Marcadores de localização
                ft.Icon(
                    ft.Icons.LOCATION_ON,
                    color=cor_verde_claro,
                    size=45,
                    top=50,
                    left=110,
                ),
                ft.Icon(
                    ft.Icons.LOCATION_ON,
                    color="#000000",
                    size=45,
                    top=200,
                    left=100,
                ),
                ft.Icon(
                    ft.Icons.LOCATION_ON,
                    color=cor_verde_claro,
                    size=45,
                    top=350,
                    left=30,
                ),
                ft.Icon(
                    ft.Icons.LOCATION_ON,
                    color=cor_verde_claro,
                    size=45,
                    top=420,
                    left=260,
                ),
            ],
        ),
    )

    # Botões inferiores
    botoes_inferiores = ft.Container(
        padding=ft.Padding(bottom=10, left=10, right=10),
        content=ft.Column(
            spacing=10,
            controls=[
                ft.Row(
                    spacing=15,
                    controls=[
                        ft.Icon(
                            ft.Icons.LOCATION_ON,
                            color="#000000",
                            size=45,
                        ),
                        ft.Container(
                            content=ft.Text(
                                "LOCALIZAÇÃO",
                                color="#FFFFFF",
                                weight=ft.FontWeight.BOLD,
                                size=16,
                            ),
                            bgcolor=cor_verde_principal,
                            padding=ft.Padding.symmetric(vertical=12),
                            border_radius=25,
                            expand=True,
                            alignment=ft.Alignment.CENTER,
                        ),
                    ],
                ),
                ft.Row(
                    spacing=15,
                    controls=[
                        ft.Icon(
                            ft.Icons.LOCATION_ON,
                            color=cor_verde_principal,
                            size=45,
                        ),
                        ft.Container(
                            content=ft.Text(
                                "ECOSTOP",
                                color="#FFFFFF",
                                weight=ft.FontWeight.BOLD,
                                size=16,
                            ),
                            bgcolor=cor_verde_principal,
                            padding=ft.Padding.symmetric(vertical=12),
                            border_radius=25,
                            expand=True,
                            alignment=ft.Alignment.CENTER,
                        ),
                    ],
                ),
            ],
        ),
    )

    # Layout principal
    layout = ft.Column(
        expand=True,
        controls=[
            barra_pesquisa,
            mapa_simulado,
            botoes_inferiores,
        ],
    )

    page.add(layout)


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)