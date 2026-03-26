import flet as ft

def main(page: ft.Page):
    # --- CONFIGURAÇÃO DA PÁGINA ---
    page.title = "Conselho Fiscal"
    page.theme_mode = "dark" 
    page.bgcolor = "#121212" 
    page.window_bgcolor = "#121212"
    
    page.appbar = ft.AppBar(
        toolbar_height=0,
        bgcolor="#121212",
    )
    
    largura_screen = 420 
    page.window_width = largura_screen
    page.window_height = 800
    page.padding = 0 
    page.scroll = False 

    # ---------------- CONTROLE DO MENU ----------------
    aberto = {"value": False}

    # --- OVERLAY ESCURO (SOMBRA) ---
    overlay = ft.Container(
        bgcolor="black",
        opacity=0,
        animate_opacity=300,
        expand=True,
        visible=False
    )

    # --- FUNÇÃO AUXILIAR PARA O RIPPLE (EFEITO DE ONDA) ---
    def item_menu(icone, texto, cor_icone):
        return ft.Container(
            content=ft.Row([
                ft.Icon(icone, size=28, color=cor_icone),
                ft.Text(texto, size=16, color="black", weight="bold")
            ], spacing=15),
            padding=10,
            border_radius=10,
            on_click=lambda _: print(f"Clicou em {texto}"),
        )

    # --- PAINEL QUE SOBE ---
    painel = ft.Container(
        bgcolor="white",
        height=0,
        animate=ft.Animation(300, "ease"),
        border_radius=ft.BorderRadius.only(top_left=30, top_right=30),
        padding=20,
        content=ft.Column([
            ft.Container(height=10),
            ft.Text("Lançamentos", size=18, weight="bold", color="black"),

            item_menu(ft.Icons.MONETIZATION_ON, "Dízimo", "green"),
            item_menu(ft.Icons.VOLUNTEER_ACTIVISM, "Ofertas", "blue"),
            item_menu(ft.Icons.HANDSHAKE, "Votos", "orange"),
            item_menu(ft.Icons.PAYMENT, "Saída", "red"),
            item_menu(ft.Icons.HISTORY, "Saldo Anterior", "grey"),
            item_menu(ft.Icons.PUBLIC, "Missões", "purple"),
            
        ], spacing=10, visible=False),
        bottom=0,
        left=0,
        right=0 
    )

    def abrir_fechar_menu(e):
        aberto["value"] = not aberto["value"]

        if aberto["value"]:
            overlay.visible = True
            overlay.opacity = 0.5
            painel.height = 550 
            painel.content.visible = True
            # --- CORREÇÃO DEFINITIVA ---
            # Trocamos o ícone por um NOVO objeto de ícone X
            page.floating_action_button.content = ft.Icon(ft.Icons.CLOSE, color="white")
        else:
            overlay.opacity = 0
            painel.height = 0
            painel.content.visible = False
            # Trocamos o ícone por um NOVO objeto de ícone +
            page.floating_action_button.content = ft.Icon(ft.Icons.ADD, color="white")

        page.update()

    def fechar_clicando_fora(e):
        if aberto["value"]:
            abrir_fechar_menu(None)

    overlay.on_click = fechar_clicando_fora

    # --- 1. CABEÇALHO ---
    header_container = ft.Container(
        content=ft.Row([
            ft.Column([
                ft.Text("Seja bem vindo(a)", color="grey", size=12),
                ft.Text("Elyomidson Brandão", size=22, weight="bold"),
                ft.Text("ADMINISTRADOR", color="grey", size=10, weight="bold"),
            ], spacing=1),
            ft.Row([
                ft.Text("Conectado", size=10, color="grey"),
                ft.Container(bgcolor="#00FF00", width=10, height=10, border_radius=5)
            ], vertical_alignment="center", spacing=5)
        ], alignment="spaceBetween"),
        padding=ft.Padding.only(left=20, right=20, top=30)
    )

    # --- 2. SELETOR DE MÊS ---
    seletor_meses = ft.Container(
        content=ft.Row([
            ft.Container(content=ft.Text("Jan 26", color="white70", size=12, weight="bold"), bgcolor="#333333", padding=ft.Padding.symmetric(horizontal=20, vertical=8), border_radius=20),
            ft.Container(content=ft.Text("Fev 26", color="white70", size=12, weight="bold"), bgcolor="#333333", padding=ft.Padding.symmetric(horizontal=20, vertical=8), border_radius=20),
            ft.Container(content=ft.Text("Mar 26", color="black", size=12, weight="bold"), bgcolor="white", padding=ft.Padding.symmetric(horizontal=20, vertical=8), border_radius=20),
            ft.Container(content=ft.Text("Abr 26", color="white70", size=12, weight="bold"), bgcolor="#333333", padding=ft.Padding.symmetric(horizontal=20, vertical=8), border_radius=20),
            ft.Container(content=ft.Text("Mai 26", color="white70", size=12, weight="bold"), bgcolor="#333333", padding=ft.Padding.symmetric(horizontal=20, vertical=8), border_radius=20),
        ], scroll="hidden", spacing=10), 
        padding=ft.Padding.symmetric(horizontal=20)
    )

    # --- 3. CARDS DE SALDO ---
    def criar_card_saldo_carrossel(titulo, valor_principal, receitas, despesas):
        return ft.Container(
            expand=1, 
            content=ft.Column([
                ft.Container(
                    content=ft.Column([
                        ft.Text(titulo, color="white70", size=11), 
                        ft.Row([
                            ft.Text(valor_principal, color="white", size=22, weight="bold"),
                            ft.Icon(ft.Icons.VISIBILITY_OFF, color="white70", size=14) 
                        ], alignment="spaceBetween"),
                    ], spacing=2),
                    bgcolor="#333333",
                    padding=12, 
                    border_radius=ft.BorderRadius.only(top_left=20, top_right=20), 
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text(f"Ant: R$ 1.658,95", color="white38", size=9),
                        ft.Row([
                            ft.Column([
                                ft.Text("Rec.", size=10, color="white70"),
                                ft.Text(f"R$ {receitas}", size=12, weight="bold")
                            ], spacing=2),
                            ft.Column([
                                ft.Text("Desp.", size=10, color="white70"),
                                ft.Text(f"R$ {despesas}", size=12, weight="bold")
                            ], spacing=2),
                        ], alignment="spaceBetween"),
                    ], spacing=5),
                    bgcolor="#444446",
                    padding=12,
                    border_radius=ft.BorderRadius.only(bottom_left=20, bottom_right=20),
                ),
            ], spacing=0)
        )

    card_financeiro = criar_card_saldo_carrossel("Saldo Financeiro", "R$ 12.316", "95.418", "84.761")
    card_missoes = criar_card_saldo_carrossel("Saldo Missões", "R$ 4.250", "15.000", "10.750")
    
    balance_carousel_container = ft.Container(
        margin=ft.Margin.symmetric(horizontal=20),
        content=ft.Row(
            controls=[card_financeiro, card_missoes],
            spacing=15, 
            alignment="spaceBetween" 
        )
    )

    # --- 4. MINI CARDS ---
    def criar_mini_card_entrada(titulo, valor, percentual_value, cor_grafico):
        return ft.Container(
            width=180,
            content=ft.Column([
                ft.Container(
                    content=ft.Row([
                        ft.Text(titulo, color="black", size=14, weight="bold"),
                        ft.Icon(ft.Icons.VISIBILITY, color="grey", size=14) 
                    ], alignment="spaceBetween"),
                    bgcolor="#F2F2F2",
                    padding=15,
                    border_radius=ft.BorderRadius.only(top_left=25, top_right=25),
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Receitas", size=10, color="grey"),
                        ft.Text(f"R$ {valor}", color="black", size=20, weight="bold"),
                        ft.Container(height=10),
                        ft.Row([
                            ft.ProgressRing(
                                value=percentual_value, 
                                color=cor_grafico, 
                                bgcolor="#D3D3D3", 
                                width=60, 
                                height=60, 
                                stroke_width=7
                            )
                        ], alignment="center"),
                        ft.Container(height=5),
                        ft.Row([
                            ft.Text(f"{int(percentual_value*100)}%", size=14, color="black", weight="bold")
                        ], alignment="center")
                    ], spacing=2),
                    bgcolor="#EDEDED",
                    padding=15, 
                    border_radius=ft.BorderRadius.only(bottom_left=25, bottom_right=25),
                ),
            ], spacing=0),
        )

    conteudo_branco_gallery = ft.Container(
        bgcolor="white",
        border_radius=ft.BorderRadius.only(top_left=40, top_right=40),
        expand=True, 
        padding=ft.Padding.only(top=30, bottom=100), 
        content=ft.Column([
            ft.Container(
                content=ft.Text("Resumo de Entradas", size=16, weight="bold", color="black54"),
                padding=ft.Padding.symmetric(horizontal=25)
            ),
            ft.Container(height=10),
            ft.Row(
                controls=[
                    ft.Container(width=15), 
                    criar_mini_card_entrada("Dízimos", "77.107", 0.65, "green"),
                    criar_mini_card_entrada("Ofertas", "12.450", 0.30, "blue"),  
                    criar_mini_card_entrada("Votos", "5.320", 0.05, "orange"),   
                    ft.Container(width=15), 
                ],
                scroll="hidden", 
                spacing=15, 
            )
        ])
    )

    # --- 5. FAB (Criação inicial) ---
    page.floating_action_button = ft.FloatingActionButton(
        content=ft.Icon(ft.Icons.ADD, color="white"),
        bgcolor="#333333",
        width=90,
        height=50,
        shape=ft.StadiumBorder(),
        on_click=abrir_fechar_menu
    )
    page.floating_action_button_location = "centerFloat"

    # --- 6. MONTAGEM FINAL (STACK) ---
    page.add(
        ft.Stack([
            ft.Column([
                ft.Container(height=10),
                header_container,
                ft.Container(height=20),
                seletor_meses,
                ft.Container(height=20),
                balance_carousel_container,
                ft.Container(height=30),
                conteudo_branco_gallery 
            ], expand=True, spacing=0),

            overlay,
            painel
        ], expand=True)
    )

if __name__ == "__main__":
    ft.app(target=main, view="web_browser", host="127.0.0.1", port=8550)