from tkinter import *;
from tkinter import ttk

#cores
preto_fosco = '#212020'
preto = '#050505'
cinza = '#7d7c7c'
laranja_escuro = '#ff6600'
azul_escuro = '#121d3b'
branco = '#FFFFFF'

#criar janela configurar Tamanho 
janela = Tk()
janela.title("Calculadora")
janela.geometry("420x520")
janela.config(bg= preto)


#separando em 2 telas e configurando
frame_tela = Frame(janela, width=425, height=150, bg=preto)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=425, height=440, bg=preto)
frame_corpo.grid(row=1, column=0)

#variaveis
valor_texto = StringVar()
aparecer = ""

#função para mostrar na tela
def entrar_valores(evento):
    global aparecer
    aparecer = aparecer + str(evento)
    valor_texto.set(aparecer)

#função para calcular
def calcular():
    global aparecer
    resultado = ''
    if "+" in aparecer:
        numeros = aparecer.split("+")
        resultado = sum([float(numero) for numero in numeros])
    elif "-" in aparecer:
        numeros = aparecer.split("-")
        resultado = float(numeros[0]) - sum([float(numero) for numero in numeros[1:]])
    elif "*" in aparecer:
        numeros = aparecer.split("*")
        resultado = 1
        for numero in numeros:
            resultado *= float(numero)
    elif "/" in aparecer:
        numeros = aparecer.split("/")
        resultado = float(numeros[0])
        for numero in numeros[1:]:
            resultado /= float(numero)
    valor_texto.set(str(resultado))
    aparecer = str(resultado)

# função para o Clear
def limpar():
    global aparecer
    aparecer = ""
    valor_texto.set("0")

# função para o CE
def cancelar_registro():
    global aparecer
    aparecer = aparecer[:-1]
    valor_texto.set(aparecer if aparecer else "0")

#configurando tela para mostrar resultado
app_label = Label(frame_tela, textvariable=valor_texto , width=30, height=6, font=('Arial Rounded MT Bold', 15, "bold"))
app_label.place(x=0, y=0)

#botoes primeira fileira

botao_clear = Button(frame_corpo, text='C', width=17, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=cinza, fg=branco, overrelief=GROOVE, command = limpar)
botao_clear.place(x=4, y=0)

botao_ce = Button(frame_corpo, text='CE', width=18, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=cinza, fg=branco, overrelief=GROOVE, command =cancelar_registro)
botao_ce.place(x=157, y=0)

botao_divisao = Button(frame_corpo, text='/', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=laranja_escuro , overrelief=GROOVE, command = lambda: entrar_valores('/'))
botao_divisao.place(x=318, y=0)

#segunda fileira
botao_vezes = Button(frame_corpo, text='*', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=laranja_escuro, overrelief=GROOVE, command = lambda: entrar_valores('*'))
botao_vezes.place(x=318, y=73)

botao_nove = Button(frame_corpo, text='9', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=preto_fosco, fg=branco, overrelief=GROOVE, command = lambda: entrar_valores('9'))
botao_nove.place(x=213, y=73)

botao_oito = Button(frame_corpo, text='8', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=preto_fosco, fg=branco, overrelief=GROOVE, command = lambda: entrar_valores('8'))
botao_oito.place(x=109, y=73)

botao_sete = Button(frame_corpo, text='7', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9),  bg=preto_fosco, fg=branco, overrelief=GROOVE, command = lambda: entrar_valores('7'))
botao_sete.place(x=4, y=73)

#terceira fileira
botao_menos = Button(frame_corpo, text='-', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=laranja_escuro, overrelief=GROOVE, command = lambda: entrar_valores('-'))
botao_menos.place(x=318, y=146)

botao_seis = Button(frame_corpo, text='6', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9),  bg=preto_fosco, fg=branco, overrelief=GROOVE, command = lambda: entrar_valores('6'))
botao_seis.place(x=213, y=146)

botao_cinco = Button(frame_corpo, text='5', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9),  bg=preto_fosco, fg=branco, overrelief=GROOVE, command = lambda: entrar_valores('5'))
botao_cinco.place(x=109, y=146)

botao_quatro = Button(frame_corpo, text='4', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=preto_fosco, fg=branco, overrelief=GROOVE, command = lambda: entrar_valores('4'))
botao_quatro.place(x=4, y=146)

#quarta fileira
botao_mais = Button(frame_corpo, text='+', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=laranja_escuro, overrelief=GROOVE, command=lambda: entrar_valores('+'))
botao_mais.place(x=318, y=219)

botao_tres = Button(frame_corpo, text='3', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=preto_fosco, fg=branco, overrelief=GROOVE, command = lambda: entrar_valores('3'))
botao_tres.place(x=213, y=219)

botao_dois = Button(frame_corpo, text='2', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=preto_fosco, fg=branco, overrelief=GROOVE, command = lambda: entrar_valores('2'))
botao_dois.place(x=109, y=219)

botao_um = Button(frame_corpo, text='1', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=preto_fosco, fg=branco, overrelief=GROOVE, command = lambda: entrar_valores('1'))
botao_um.place(x=4, y=219)

#ultima fileira
botao_igual = Button(frame_corpo, text='=', width=24, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=azul_escuro, fg=branco, overrelief=GROOVE, command = calcular)
botao_igual.place(x=213, y=292)

botao_zero = Button(frame_corpo, text='0', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=preto_fosco, fg=branco, overrelief=GROOVE, command = lambda: entrar_valores('0'))
botao_zero.place(x=109, y=292)

botao_virgula = Button(frame_corpo, text='.', width=11, height=4, relief='raised', font=('Arial Rounded MT Bold', 9), bg=preto_fosco, fg=branco, overrelief=GROOVE, command = lambda: entrar_valores('.'))
botao_virgula.place(x=4, y=292)


calcular()
cancelar_registro()
limpar()
janela.mainloop()