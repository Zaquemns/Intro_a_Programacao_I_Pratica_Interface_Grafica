# -*- coding: utf-8 -*-
"""
Aula Prática de UI com Tkinter: Mood Tracker App
3 partes, cada uma com 5 blocos de 3 exercícios (1 resolvido + 2 similares)
Objetivo: construir um app para registrar e visualizar o humor diário.
"""

# ------------------------------
# PARTE 1: SETUP, JANELA E BOTÃO (Mood Tracker)
# Narrativa: iniciar o Mood Tracker com um botão para registrar humor.
# ------------------------------

# Bloco 1: Janela e título do app
# 1. (resolvido) Crie a janela com título "Mood Tracker" e cor de fundo clara.
import tkinter as tk

root = tk.Tk()
root.title("Mood Tracker")
root.configure(bg="#F0F0F0")
label = tk.Label(root, text="Bem-vindo ao Mood Tracker!", font=("Arial", 16), bg="#F0F0F0")
label.pack(pady=20)
root.mainloop()

# (prática) Altere o texto de boas‑vindas para incluir a data atual (use datetime).
# (prática) Modifique a cor de fundo para um tom laranja.
import datetime

BACKGROUND_LARANJA = "#FFA500"

root = tk.Tk()
root.title("Mood Tracker")
root.configure(bg=BACKGROUND_LARANJA)
data_atual_formatada = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
label = tk.Label(root, text=f"Bem-vindo ao Mood Tracker! Hoje é {data_atual_formatada}", font=("Arial", 16), bg=BACKGROUND_LARANJA)
label.pack(pady=20)
root.mainloop()


# Bloco 2: Botão de registrar humor
# (resolvido) Adicione um botão “Registrar Humor” que imprima no console “Humor registrado!”:
import tkinter as tk

def registrar():
    print("Humor registrado!")

root = tk.Tk()
btn = tk.Button(root, text="Registrar Humor", command=registrar)
btn.pack(pady=10)
root.mainloop()


# (prática) Crie um botão "Imprimir Data" que imprime a data de hoje no console.
# (prática) Crie um botão "Mostrar Histórico" que imprime no console os momentos que você registrou o humor.
import tkinter as tk
import datetime

historico = []

def registrar():
    agora = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    print("Humor registrado!")
    historico.append(agora)

def imprimir_data():
    hoje = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    print("Data de hoje:", hoje)

def mostrar_historico():
    if historico:
        print("Histórico de registros:")
        for momento in historico:
            print(momento)
    else:
        print("Nenhum registro de humor ainda.")

root = tk.Tk()
btn = tk.Button(root, text="Registrar Humor", command=registrar)
btn.pack(pady=10)
btn_data = tk.Button(root, text="Imprimir Data", command=imprimir_data)
btn_data.pack(pady=5)
btn_hist = tk.Button(root, text="Mostrar Histórico", command=mostrar_historico)
btn_hist.pack(pady=5)
root.mainloop()


# Bloco 3: Layout básico
# (resolvido) Use Frame/pack para empilhar um Label e o botão de registrar humor:
import tkinter as tk


root = tk.Tk()
frame = tk.Frame(root)
frame.pack(pady=20)


lbl = tk.Label(frame, text="Como você se sente hoje?")
lbl.pack()


btn = tk.Button(frame, text="Registrar Humor", command=lambda: None)
btn.pack(pady=5)


root.mainloop()


# (prática) Organize um Entry (TextField) e um botão na mesma Frame.
# (prática) Empilhe um OptionMenu (dropdown) e um botão na Frame.


# Bloco 4: Evento de clique altera texto
# (resolvido) Faça o botão atualizar o Label para “Humor registrado!”:
import tkinter as tk


root = tk.Tk()
msg = tk.Label(root, text="")
msg.pack(pady=10)


def on_click():
    msg.config(text="Humor registrado!")


btn = tk.Button(root, text="Registrar Humor", command=on_click)
btn.pack()


root.mainloop()


# (prática) Faça o botão atualizar para “Salvo com sucesso!” no Label.
# (prática) Faça o botão atualizar para “Gravado com sucesso!” no Label.
import tkinter as tk

root = tk.Tk()
msg = tk.Label(root, text="")
msg.pack(pady=10)

def salvo():
    msg.config(text="Salvo com sucesso!")

def gravado():
    msg.config(text="Gravado com sucesso!")

btn1 = tk.Button(root, text="Salvar", command=salvo)
btn1.pack()
btn2 = tk.Button(root, text="Gravar", command=gravado)
btn2.pack()

root.mainloop()




# ------------------------------
# PARTE 2: COMPONENTES E NAVEGAÇÃO (Mood Tracker)
# Objetivo: adicionar seleção de humor e tela de histórico.
# ------------------------------


# Bloco 1: Dropdown de humor
# (resolvido) Adicione um OptionMenu com emojis e imprima seleção:
import tkinter as tk


def on_select(value):
    print(value)


root = tk.Tk()
var = tk.StringVar(root)
var.set("😀")
opts = ["😀", "😔", "🙃"]
menu = tk.OptionMenu(root, var, *opts, command=on_select)
menu.pack(pady=10)
root.mainloop()


# (prática) Crie um OptionMenu de clima ["☀️","🌧️","❄️"] que imprima escolha.
# (prática) Crie um OptionMenu de níveis de energia ["Alto","Médio","Baixo"].
import tkinter as tk

root = tk.Tk()
# Clima
clima = tk.StringVar(value="☀️")
climas = ["☀️","🌧️","❄️"]
tk.OptionMenu(root, clima, *climas, command=lambda v: print("Clima:", v)).pack()
# Energia
energia = tk.StringVar(value="Alto")
energias = ["Alto","Médio","Baixo"]
tk.OptionMenu(root, energia, *energias, command=lambda v: print("Energia:", v)).pack()
root.mainloop()


# Bloco 2: Checkbox múltipla escolha
# 1. (resolvido) Adicione três Checkbutton para sintomas e imprima lista selecionada:
import tkinter as tk


root = tk.Tk()
sintomas = ["Dor de cabeça", "Fome", "Sono"]
vars = []
def on_change():
    sel = [s for v, s in zip(vars, sintomas) if v.get()]
    print(sel)


for s in sintomas:
    v = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=s, variable=v, command=on_change)
    chk.pack(anchor="w")
    vars.append(v)


root.mainloop()


# (prática) Crie Checkbutton para atividades ["Caminhada","Leitura","Música"].
# (prática) Crie Checkbutton para humor físico ["Bem","Regular","Mal"].
import tkinter as tk

root = tk.Tk()
atividades = ["Caminhada","Leitura","Música"]
vars_ativ = []
def on_ativ():
    sel = [a for v, a in zip(vars_ativ, atividades) if v.get()]
    print("Atividades:", sel)
for a in atividades:
    v = tk.BooleanVar()
    tk.Checkbutton(root, text=a, variable=v, command=on_ativ).pack(anchor="w")
    vars_ativ.append(v)

humor_fisico = ["Bem","Regular","Mal"]
vars_humor = []
def on_humor():
    sel = [h for v, h in zip(vars_humor, humor_fisico) if v.get()]
    print("Humor físico:", sel)
for h in humor_fisico:
    v = tk.BooleanVar()
    tk.Checkbutton(root, text=h, variable=v, command=on_humor).pack(anchor="w")
    vars_humor.append(v)
root.mainloop()


# Bloco 3: Navegação Home/Histórico
# (resolvido) Use Frames e botão para alternar entre Home e Histórico:
import tkinter as tk


root = tk.Tk()
home_frame = tk.Frame(root)
hist_frame = tk.Frame(root)


tk.Label(home_frame, text="Home: registre seu humor").pack()
btn_hist = tk.Button(home_frame, text="Ir para Histórico", command=lambda: show_history())
btn_hist.pack()

tk.Label(hist_frame, text="Histórico:").pack()
for r in ["23/07/2025 - 😀", "22/07/2025 - 😔", "21/07/2025 - 🙃"]:
    tk.Label(hist_frame, text=r).pack()
btn_voltar = tk.Button(hist_frame, text="Voltar", command=lambda: show_home())
btn_voltar.pack()


def show_home():
    hist_frame.pack_forget()
    home_frame.pack()

def show_history():
    home_frame.pack_forget()
    hist_frame.pack()


show_home()
root.mainloop()


# (prática) Na view Histórico, liste 3 registros de humor simulados (use Label).
# (prática) Adicione botão “Voltar” em cada view para navegar.


# Bloco 4: Lista de registros
# (resolvido) Exiba uma lista de Radiobuttons e imprima seleção:
import tkinter as tk


root = tk.Tk()
var = tk.StringVar()
for emoji in ["😀","😔","🙃"]:
    rb = tk.Radiobutton(root, text=emoji, variable=var, value=emoji,
                        command=lambda: print("Selecionado:", var.get()))
    rb.pack(anchor="w")
root.mainloop()


# (prática) Crie lista de dias da semana com Radiobuttons.
# (prática) Crie lista de cores com Radiobuttons.
import tkinter as tk

root = tk.Tk()
# Dias da semana
dias = ["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]
var_dia = tk.StringVar()
for d in dias:
    tk.Radiobutton(root, text=d, variable=var_dia, value=d, command=lambda: print("Dia:", var_dia.get())).pack(anchor="w")
# Cores
cores = ["Vermelho","Verde","Azul"]
var_cor = tk.StringVar()
for c in cores:
    tk.Radiobutton(root, text=c, variable=var_cor, value=c, command=lambda: print("Cor:", var_cor.get())).pack(anchor="w")
root.mainloop()


# Bloco 5: Slider para intensidade
# (resolvido) Adicione um Scale de 1–10 que imprime valor:
import tkinter as tk


def on_slide(v):
    print(v)


root = tk.Tk()
s = tk.Scale(root, from_=1, to=10, orient="horizontal", command=on_slide)
s.pack(pady=10)
root.mainloop()


# (prática) Crie um Scale vertical de 0–100.
# (prática) Crie Scale para ajustar opacidade de um Label (use .config(fg=...) com valor de escala).
import tkinter as tk

root = tk.Tk()
# Scale vertical
def on_slide(v):
    print("Valor:", v)
tk.Scale(root, from_=0, to=100, orient="vertical", command=on_slide).pack(side="left", padx=10)

# Scale para opacidade (ajusta cor do texto)
lbl = tk.Label(root, text="Opacidade ajustável")
lbl.pack(side="left", padx=10)
def ajustar_opacidade(v):
    v = int(v)
    cor = f"#{v:02x}{v:02x}{v:02x}"
    lbl.config(fg=cor)
tk.Scale(root, from_=0, to=255, orient="horizontal", command=ajustar_opacidade).pack(side="left")
root.mainloop()


# ------------------------------
# PARTE 3: GRÁFICOS E COMPONENTES AVANÇADOS
# ------------------------------
# Objetivo: visualizar tendências de humor


# CONFIGURAÇÃO
# você irá precisar instalar o matplotlib, no terminal digite:
# pip instal matplotlib


# Bloco 1: Gráfico de barras de humor semanal
# (resolvido) Exiba um bar chart com matplotlib dentro de um Canvas Tk:
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = tk.Tk()
fig = Figure(figsize=(4,3))
ax = fig.add_subplot(111)
data = [2,1,3]; labels = ["😀","😔","🙃"]
ax.bar(labels, data)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()
root.mainloop()


# 2. (prática) Ajuste dados para proporções diárias de ontem.
# 3. (prática) Alterne ordem das barras (descrescente).


# Bloco 2: Gráfico de pizza dos humores
# (resolvido) Exiba um pie chart:
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = tk.Tk()
fig = Figure(figsize=(3,3))
ax = fig.add_subplot(111)
values = [50,30,20]; labels = ["😀","😔","🙃"]
ax.pie(values, labels=labels, autopct='%1.1f%%')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()
root.mainloop()


# (prática) Modifique valores para refletir dados reais.
# (prática) Adicione texto central indicando total de registros.


# Bloco 3: Tabela de registros
# (resolvido) Crie uma tabela simples com ttk.Treeview:
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
cols = ("Dia","Humor")
tree = ttk.Treeview(root, columns=cols, show="headings")
for c in cols: tree.heading(c, text=c)
rows = [("Segunda","😀"),("Terça","😔"),("Quarta","🙃")]
for r in rows: tree.insert("", tk.END, values=r)
tree.pack()
root.mainloop()


# (prática) Adicione coluna "Intensidade" com valores.
# (prática) Ordene linhas por dia da semana.
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
cols = ("Dia","Humor","Intensidade")
tree = ttk.Treeview(root, columns=cols, show="headings")
for c in cols: tree.heading(c, text=c)
dias_ordem = ["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]
rows = [("Quarta","🙃",5),("Terça","😔",7),("Segunda","😀",9)]
rows.sort(key=lambda r: dias_ordem.index(r[0]))
for r in rows: tree.insert("", tk.END, values=r)
tree.pack()
root.mainloop()


# Bloco 4: Canvas para trend line
# (resolvido) Desenhe uma linha conectando pontos no Canvas Tkinter:
import tkinter as tk


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=200, bg="#FFF")
canvas.pack()
points = [(50,150),(100,100),(150,120),(200,80)]
for i in range(len(points)-1):
    canvas.create_line(*points[i], *points[i+1], width=2, fill="#0000FF")
for x, y in points:
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="#0000FF")
root.mainloop()


# (prática) Ajuste cor da linha para azul.
# (prática) Desenhe círculos nos pontos da linha (use create_oval).
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
fig = Figure(figsize=(4,3))
ax = fig.add_subplot(111)
# Exemplo: ontem 3 felizes, 1 triste, 2 neutros
data = [3,1,2]; labels = ["😀","😔","🙃"]
# Ordenar decrescente
data_labels = sorted(zip(data, labels), reverse=True)
data, labels = zip(*data_labels)
ax.bar(labels, data)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()
root.mainloop()
