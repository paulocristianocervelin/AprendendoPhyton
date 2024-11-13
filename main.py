import pandas as pd
import xml.etree.ElementTree as ET

def ler_csv(caminho):
    try:
        df = pd.read_csv(caminho)
        print("Dados do CSV:")
        print(df)
    except Exception as e:
        print(f"Erro ao ler CSV: {e}")

def ler_txt(caminho):
    try:
        with open(caminho, 'r') as file:
            conteudo = file.read()
            print("Dados do TXT:")
            print(conteudo)
    except Exception as e:
        print(f"Erro ao ler TXT: {e}")

def ler_xml(caminho):
    try:
        tree = ET.parse(caminho)
        root = tree.getroot()
        print("Dados do XML:")
        for elem in root:
            print(elem.tag, elem.attrib, elem.text)
    except Exception as e:
        print(f"Erro ao ler XML: {e}")

if __name__ == "__main__":
    arquivo = input("Digite o caminho do arquivo (CSV, TXT, XML): ")

    if arquivo.endswith(".csv"):
        ler_csv(arquivo)
    elif arquivo.endswith(".txt"):
        ler_txt(arquivo)
    elif arquivo.endswith(".xml"):
        ler_xml(arquivo)
    else:
        print("Formato de arquivo não suportado.")
