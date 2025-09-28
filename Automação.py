import pyautogui as py #RESUME O NOME
import pandas as pd #RESUME O NOME
import time as tm #RESUME O NOME


py.PAUSE = 1

# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.hotkey -> atalho de teclado (ctrl, C)

#  Passo 1: Abrir o sistema da empresa

# abrir o google chrome
# apertar a tecla win
py.press("win")

# digitar o texto chrome
py.write("chrome")

# apertar enter
py.press("enter")

# entrar no lik https://dlp.hashtagtreinamentos.com/python/intensivao/login
py.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py.press("enter")

# pedir pro computador esperar 3 segundos
tm.sleep(2)

# passo 2: Fazer login
py.click(x=191, y=449,  click=2) # clicar no campo do email # (x e y exemplo)
py.write("tutu@gmail.com") # digitar o seu email de login

py.press("tab") #passa para o campo da senha
py.write("121341212") #a sua senha


py.press("tab") #passar para o botão "logar"
py.press("enter") #pressionar o botão "logar"

# passo 3: importar a base de dados dos produtos
tabela = pd.read_csv("produtos (1).csv") #lendo a base de dados

print(tabela) #mostrando a base de dados
 
tm.sleep(2)

# passo 4: Cadastrar 1 produto
py.click(x=123, y=319) # clicar no botão "produtos" (x e y exemplo)


# passo 5: Repetir o passo 4 até acabar todos os produtos

