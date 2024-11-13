import pandas as pd
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def ler_csv(caminho):
    try:
        df = pd.read_csv(caminho)
        return df
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler CSV: {e}")
        return None

def ler_txt(caminho):
    try:
        with open(caminho, 'r') as file:
            conteudo = file.readlines()
            df = pd.DataFrame(conteudo, columns=["Conteúdo"])
            return df
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler TXT: {e}")
        return None

def ler_xml(caminho):
    try:
        tree = ET.parse(caminho)
        root = tree.getroot()
        data = []

        # Adiciona os elementos XML na lista
        for elem in root:
            data.append({subelem.tag: subelem.text for subelem in elem})
        
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler XML: {e}")
        return None

def abrir_arquivo():
    caminho = filedialog.askopenfilename(filetypes=[("Todos os arquivos", "*.csv *.txt *.xml")])
    if caminho:
        caminho_arquivo.set(caminho)
        carregar_dados()

def carregar_dados():
    caminho = caminho_arquivo.get()
    if caminho.endswith(".csv"):
        df = ler_csv(caminho)
    elif caminho.endswith(".txt"):
        df = ler_txt(caminho)
    elif caminho.endswith(".xml"):
        df = ler_xml(caminho)
    else:
        messagebox.showwarning("Aviso", "Formato de arquivo não suportado.")
        return

    if df is not None:
        mostrar_dados(df)

def mostrar_dados(df):
    # Limpar a grid antes de exibir novos dados
    for item in grid.get_children():
        grid.delete(item)

    # Configurar as colunas
    grid["columns"] = list(df.columns)
    grid["show"] = "headings"

    # Adicionar colunas
    for col in df.columns:
        grid.heading(col, text=col)
        grid.column(col, width=150)

    # Adicionar dados na grid
    for _, row in df.iterrows():
        grid.insert("", tk.END, values=list(row))

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Leitor de Arquivos CSV, TXT e XML")

# Variável para armazenar o caminho do arquivo
caminho_arquivo = tk.StringVar()

# Layout da interface
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Caminho do arquivo:")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame, textvariable=caminho_arquivo, width=50)
entry.grid(row=0, column=1, padx=5, pady=5)

botao_abrir = tk.Button(frame, text="Abrir", command=abrir_arquivo)
botao_abrir.grid(row=0, column=2, padx=5, pady=5)

botao_carregar = tk.Button(frame, text="Carregar Dados", command=carregar_dados)
botao_carregar.grid(row=1, column=1, pady=10)

# Grade para exibir os dados
grid = ttk.Treeview(root)
grid.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Ajustar as barras de rolagem
scrollbar_y = ttk.Scrollbar(root, orient="vertical", command=grid.yview)
scrollbar_y.pack(side=tk.RIGHT, fill="y")
grid.configure(yscroll=scrollbar_y.set)

scrollbar_x = ttk.Scrollbar(root, orient="horizontal", command=grid.xview)
scrollbar_x.pack(side=tk.BOTTOM, fill="x")
grid.configure(xscroll=scrollbar_x.set)

root.mainloop()
