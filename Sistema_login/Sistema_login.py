import _tkinter
from tkinter import *
from tkinter import messagebox
import os

users_list = [""]

def janelalog():
    janelalog = Tk()
    janelalog.title("Login")
    
    #user_log = usuário já cadastrado
    usertext_log = Label(janelalog, text='Digite o Usuário : ')
    user_log = Entry(janelalog)
    usertext_log.grid(column=0, row=0, padx=10, pady=10)
    user_log.grid(column=1, row=0, padx=10, pady=10)

    #user_pass = senha já cadastrada
    user_pass = Entry(janelalog)
    usertext_pass = Label(janelalog, text='Digite a Senha : ')
    user_pass.grid(column=1, row=1, padx=10, pady=10)
    usertext_pass.grid(column=0, row=1, padx=10, pady=10)

    #botao_novoCad = botao para cadastrar novo usuário
    #botao_fazerLogin = botao para fazer login do usuário já cadastrado
    botao_novoCad = Button(janelalog, text='Novo Cadastro', command=janelacad)
    botao_fazerLogin = Button(janelalog, text='Fazer Login')
    botao_novoCad.grid(column=0, row=2, padx=10, pady=10)
    botao_fazerLogin.grid(column=1, row=2, padx=10, pady=10)
    
    janelalog.mainloop()

def janelacad():
    global user_cad, usercad_pass
    janelacad = Tk()
    janelacad.title("Cadastre-se")

    #user_cad = usuário a ser cadastrado
    usertext_cad = Label(janelacad, text='Insira um Usuário: ')
    user_cad = Entry(janelacad)
    usertext_cad.grid(column=0, row=0, padx=10, pady=10)
    user_cad.grid(column=1, row=0, padx=10, pady=10)

    #usercad_pass = senha a ser cadastrada
    usercadtext_pass = Label(janelacad, text='Insira uma Senha : ')
    usercad_pass = Entry(janelacad)
    usercadtext_pass.grid(column=0, row=1, padx=10, pady=10)
    usercad_pass.grid(column=1, row=1, padx=10, pady=10)

    #botao_voltar = volta a janelalog
    #botaocad_newUser = cadastra usuário na 'users_list[]'
    botao_voltar = Button(janelacad, text='Voltar', command= janelalog)
    botao_voltar.grid(column=0, row=3, padx=10, pady=20)
    botaocad_newUser = Button(janelacad, text='Cadastrar novo Usuário', command=cod_cadastro)
    botaocad_newUser.grid(column=1, row=3, padx=10, pady=20)

def cod_cadastro():
    user = str(user_cad.get)
    password = str(usercad_pass.get)
    users_list.append(user)
    users_list.append(password)
    
    #abre uma nova janela e informa que o usuário foi cadastrado
    cod_cadastro = Tk()
    cod_cadastro.title("Cadastro Efetuado")
    cad_efetuado = Label(cod_cadastro, text='Cadastro Efetuado com Sucesso!')
    cad_efetuado.grid(column=0, row=0, padx=10, pady=10)


janelalog()
print(users_list)