# pip install pyautogui

import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.8  # Pausa de 0.8 segundos entre cada ação

# pyautogui.click -> Clicar em um ponto da tela
# pyautogui.write -> Escrever um texto
# pyautogui.press -> Pressionar uma tecla
# pyautogui.hotkey -> Pressionar uma combinação de teclas (atalho)

# Passo 1: Abrir o sistema da empresa 

# abrir o google chrome
# Apertar a tecla "win" 
# pyautogui.press("win")

# # digitar o texto chrome
# pyautogui.write("chrome")

# # apertar a tecla "enter"
# pyautogui.press("enter")

# # Entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login"   )
# pyautogui.press("enter")

# # #pedir pro computador esperar 1 segundo
# time.sleep(1)

# # Passo 2: Fazer o login
# pyautogui.click(x=874, y=462)  # clicar no campo de e-mail
# pyautogui.write("emailaqui@gmail.com")

# pyautogui.press("tab") # passa para o campo da senha
# pyautogui.write("suasenhaaqui")

# pyautogui.press("tab")

# pyautogui.press("enter")

# Passo 3: Importar a base e dados dos produtos

tabela = pandas.read_csv("produtos.csv")  

pyautogui.click(x=1165, y=1044) 

time.sleep(2)
# Passo 4: Cadastrar 1 produto


for linha in tabela.index: # Passo 5: Repetir o passo 4 até acabar todos os produtos

    pyautogui.click(x=787, y=319)

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan": # nan = valor vazio (not a number)
        pyautogui.write(str(obs))

    pyautogui.press("tab")

    pyautogui.press("enter") #apertar o botão de enviar

    # numero posiitivo = scroll para cima
    # numero negativo = scroll para baixo
    pyautogui.scroll(10000)
