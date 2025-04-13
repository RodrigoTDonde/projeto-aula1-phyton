# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=654, y=494)

# escrever o seu email
pyautogui.write("rodrigotdonde@gmail.com")
# preencher a senha
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("senha")
# botao logar
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas

tabela = pandas.read_csv("Aula 1 - Python PowerUp/produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index: # para cada linha da tabela

    pyautogui.click(x=604, y=351)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)


    




