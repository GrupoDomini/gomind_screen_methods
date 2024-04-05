#########################################################################
##                                                                     ##
##     Métodos relacionados a criação de telas em tempo de execução    ##
##                                                                     ##
#########################################################################

from dataclasses import dataclass
from typing import Literal
import requests
from io import BytesIO
import os


def get_image(url):
    from PIL import Image

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


def keyboard_listener():
    import os
    from pynput import keyboard
    import customtkinter as ctk

    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.end:

                def msg_key_end():
                    print("O usuário interrompeu a executação geral do processo.")
                    os._exit(0)

                def btn_nao():
                    print("O usuário optou por não interromper a execução.")
                    tk.destroy()

                tk = ctk.CTk()
                tk.overrideredirect(True)
                altura = 390
                largura = 600
                largura_monitor = tk.winfo_screenwidth()
                altura_monitor = tk.winfo_screenheight()
                x = (largura_monitor // 2) - (largura // 2)
                y = (altura_monitor // 2) - (altura // 2)
                tk.geometry(f"{largura}x{altura}+{x}+{y}")

                # Carregue a imagem
                imagem_fundo = ctk.CTkImage(
                    get_image(
                        "https://raw.githubusercontent.com/GrupoDomini/Public/main/frame_end.png"
                    ),
                    size=(largura, altura),
                )

                fundo = ctk.CTkLabel(
                    tk, text="", image=imagem_fundo, bg_color="darkgray"
                )
                fundo.pack()

                # Texto principal
                texto = ctk.CTkLabel(
                    tk,
                    text="Deseja encerrar o processo automatizado?",
                    font=("Helvetica", 25),
                    bg_color="white",
                    fg_color="white",
                    text_color="#0B4A4F",
                )
                texto.pack()
                texto.place(x=60, y=230)

                # Botao Ok
                botao_confirmar = ctk.CTkButton(
                    tk,
                    text="Sim",
                    width=50,
                    height=50,
                    bg_color="white",
                    hover_color="#0B745B",
                    fg_color="#0EA899",
                    font=("Arial", 20),
                    corner_radius=40,
                    command=msg_key_end,
                )
                botao_confirmar.pack()
                botao_confirmar.place(x=150, y=300)

                # Botao Cancelar
                botao_confirmar = ctk.CTkButton(
                    tk,
                    text="Não",
                    width=50,
                    height=50,
                    bg_color="white",
                    hover_color="#FF6565",
                    fg_color="#25645E",
                    font=("Arial", 20),
                    corner_radius=40,
                    command=btn_nao,
                )
                botao_confirmar.pack()
                botao_confirmar.place(x=350, y=300)

                tk.wm_attributes("-transparentcolor", "darkgray")
                tk.wm_attributes("-topmost", 1)
                tk.mainloop()


def msg_screen(status: Literal["start", "final"] = "start"):
    # Bibliotecas necessárias
    import webbrowser
    import keyboard as tecla
    import customtkinter as ctk

    # Variáveis
    url = "http://www.gomind.com"

    def cancelar():
        tk.destroy()
        print("Processo cancelado pelo usuário")
        os._exit(0)

    tk = ctk.CTk()
    tk.overrideredirect(True)
    altura = 529
    largura = 600

    largura_monitor = tk.winfo_screenwidth()
    altura_monitor = tk.winfo_screenheight()
    x = (largura_monitor // 2) - (largura // 2)
    y = (altura_monitor // 2) - (altura // 2)
    tk.geometry(f"{largura}x{altura}+{x}+{y}")

    if status == "start":
        imagem_fundo = ctk.CTkImage(
            get_image(
                "https://raw.githubusercontent.com/GrupoDomini/Public/main/frame_inicial.png"
            ),
            size=(largura, altura),
        )
    elif status == "final":
        imagem_fundo = ctk.CTkImage(
            get_image(
                "https://raw.githubusercontent.com/GrupoDomini/Public/main/frame_fim.png"
            ),
            size=(largura, altura),
        )
    else:
        try:
            tecla.press_and_release("END")
        except Exception as _:
            os._exit(0)

    fundo = ctk.CTkLabel(tk, text="", image=imagem_fundo, bg_color="darkgray")
    fundo.pack()

    # Botão Cancelar
    if status == "start":
        botao_cancelar = ctk.CTkButton(
            tk,
            text="Cancelar",
            bg_color="white",
            height=35,
            hover_color="#0B615E",
            fg_color="#0C756B",
            font=("Arial", 14),
            text_color="white",
            corner_radius=20,
            command=cancelar,
        )
        botao_cancelar.pack()
        botao_cancelar.place(x=230, y=340)

    # Rodapé Tecnoloigia
    texto = ctk.CTkLabel(
        tk,
        text="©2024 - Desenvolvido pelo departamento de Tecnologia - GO Mind",
        bg_color="white",
        font=("Arial", 13),
        text_color="#074140",
    )
    texto.pack()
    texto.place(x=105, y=400)

    # Link website
    link_site = ctk.CTkButton(
        tk,
        text="www.gomind.com.br",
        bg_color="white",
        fg_color="transparent",
        hover=False,
        font=("Arial", 13),
        text_color="#1B548B",
        command=lambda: webbrowser.open(url),
    )
    link_site.pack()
    link_site.place(x=230, y=440)

    time_msg_screen = 10000 if status == "start" else 7000

    tk.after(time_msg_screen, tk.destroy)

    tk.wm_attributes("-transparentcolor", "darkgray")
    tk.wm_attributes("-topmost", 1)
    tk.mainloop()

    if status == "final":
        print("Processo concluído com sucesso")
        os._exit(0)


@dataclass
class Competencia:
    mes_ant: str
    mes_cmpt: str
    ano: str
    dia_final: str


def janela_competencia():
    from tkinter import messagebox as msgbox
    import customtkinter as ctk
    from time import localtime
    import calendar

    data_atual = localtime()
    i_mes_ant = data_atual.tm_mon - 1
    meses_ext = [
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
    ]
    mes_ext_ant = meses_ext[i_mes_ant - 1]
    mes_ant = int(data_atual.tm_mon - 1)
    if data_atual.tm_mon == 1:
        ano = str(data_atual.tm_year - 1)
        mes_ant = 12
    else:
        ano = str(data_atual.tm_year)
    # endregion

    # função para confirmar a data no tkinter
    def confirmaDatas():
        mes_selecionado = var_mes.get()
        ano_selecionado = var_ano.get()

        if mes_selecionado and ano_selecionado:
            tk.destroy()
            print("A data selecionada é: " + f"{mes_selecionado}/{ano_selecionado}")

    def btnCancela():
        tk.destroy()
        print("Processo cancelado pelo usuário")
        os._exit(0)

    while True:  # Usuário determina Mês e Ano de Competência
        tk = ctk.CTk()
        tk.overrideredirect(True)
        altura = 529
        largura = 600
        largura_monitor = tk.winfo_screenwidth()
        altura_monitor = tk.winfo_screenheight()
        x = (largura_monitor // 2) - (largura // 2)
        y = (altura_monitor // 2) - (altura // 2)
        tk.geometry(f"{largura}x{altura}+{x}+{y}")

        # Carregue a imagem
        imagem_fundo = ctk.CTkImage(
            get_image(
                "https://raw.githubusercontent.com/GrupoDomini/Public/main/frame_competencia.png"
            ),
            size=(largura, altura),
        )

        fundo = ctk.CTkLabel(tk, text="", image=imagem_fundo, bg_color="darkgray")
        fundo.pack()

        var_mes = ctk.StringVar(tk, mes_ext_ant)
        var_ano = ctk.StringVar(tk, ano)

        # DropDown meses
        mes = ctk.CTkOptionMenu(
            tk,
            values=meses_ext,
            bg_color="#F7F7F7",
            fg_color="#F7F7F7",
            font=("Arial", 12),
            dropdown_fg_color="white",
            dropdown_hover_color="#0FBEA0",
            button_color="#F7F7F7",
            button_hover_color="#0FBEA0",
            corner_radius=2,
            text_color="#074140",
            variable=var_mes,
        )
        mes.pack()
        mes.place(x=170, y=365)

        # DropDown anos
        ano = ctk.CTkOptionMenu(
            tk,
            values=[str(ano) for ano in range(2022, data_atual.tm_year + 6)],
            bg_color="#F7F7F7",
            fg_color="#F7F7F7",
            font=("Arial", 12),
            dropdown_fg_color="white",
            dropdown_hover_color="#0FBEA0",
            button_color="#F7F7F7",
            button_hover_color="#0FBEA0",
            corner_radius=2,
            text_color="#074140",
            variable=var_ano,
        )
        ano.pack()
        ano.place(x=170, y=285)

        # Botao confirma
        botao_confirmar = ctk.CTkButton(
            tk,
            text="Confirmar",
            bg_color="white",
            height=35,
            hover_color="#0B745B",
            fg_color="#0EA899",
            font=("Arial", 14),
            text_color="white",
            corner_radius=10,
            command=confirmaDatas,
        )
        botao_confirmar.pack()
        botao_confirmar.place(x=400, y=295)

        # Botao cancela
        botao_cancelar = ctk.CTkButton(
            tk,
            text="Cancelar",
            bg_color="white",
            height=35,
            hover_color="#FF6565",
            fg_color="#25645E",
            font=("Arial", 14),
            text_color="white",
            corner_radius=10,
            command=btnCancela,
        )
        botao_cancelar.pack()
        botao_cancelar.place(x=400, y=345)

        # Rodapé Tecnoloigia
        texto = ctk.CTkLabel(
            tk,
            text="©2024 - Desenvolvido pelo departamento de Tecnologia - GO Mind",
            bg_color="white",
            font=("Arial", 11),
            text_color="#074140",
        )
        texto.pack()
        texto.place(x=130, y=490)

        tk.focus_force()
        tk.wm_attributes("-transparentcolor", "darkgray")
        tk.wm_attributes("-topmost", 1)
        tk.mainloop()

        # Coleta as informações da janela
        mes_cmpt = var_mes.get()
        ano_cmpt = var_ano.get()

        confirmado = msgbox.askyesno(
            title="Confirmação de competência",
            message=f"Confirme a competência definida: {str(mes_cmpt)}/{str(ano_cmpt)}",
            icon="question",
        )

        if confirmado is True:
            print("Processo confirmado pelo usuário")
            break

    ano = ano_cmpt
    meses_para_numeros = {
        nome: numero for numero, nome in enumerate(meses_ext, start=1)
    }
    dia_final = calendar.monthrange(int(ano), int(meses_para_numeros[mes_cmpt]))[1]
    mes_ant = str(meses_para_numeros[mes_cmpt]).zfill(2)

    return Competencia(mes_ant, mes_cmpt, ano, dia_final)


def erro_msg():
    # Bibliotecas necessárias
    import customtkinter as ctk  # utiliza o customTKINTER para costumizar a tela

    # Botao Ok
    def confirmar():
        tk.destroy()
        os._exit(0)

    tk = ctk.CTk()
    tk.overrideredirect(True)
    altura = 390
    largura = 600
    largura_monitor = tk.winfo_screenwidth()
    altura_monitor = tk.winfo_screenheight()
    x = (largura_monitor // 2) - (largura // 2)
    y = (altura_monitor // 2) - (altura // 2)
    tk.geometry(f"{largura}x{altura}+{x}+{y}")

    imagem_fundo = ctk.CTkImage(
        get_image(
            "https://raw.githubusercontent.com/GrupoDomini/Public/main/frame_erro.png"
        ),
        size=(largura, altura),
    )

    fundo = ctk.CTkLabel(tk, text="", image=imagem_fundo, bg_color="darkgray")
    fundo.pack()

    # Texto principal
    texto = ctk.CTkLabel(
        tk,
        text="O processo foi encerrado inesperadamente. Contate o departamento de Tecnologia.",
        font=("Helvetica", 20),
        bg_color="white",
        fg_color="white",
        wraplength=400,
        text_color="#0B4A4F",
    )
    texto.pack()
    texto.place(x=110, y=230)

    botao_confirmar = ctk.CTkButton(
        tk,
        text="Ok",
        width=50,
        height=50,
        bg_color="white",
        fg_color="#09858E",
        font=("Arial", 20),
        corner_radius=40,
        command=confirmar,
    )
    botao_confirmar.pack()
    botao_confirmar.place(x=255, y=320)

    tk.wm_attributes("-transparentcolor", "darkgray")
    tk.wm_attributes("-topmost", 1)
    tk.mainloop()

