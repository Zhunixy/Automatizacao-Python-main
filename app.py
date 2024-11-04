# Inserir cada célula de cada linha em um campo do sistema
import openpyxl
import pyautogui

# Carregar o arquivo Excel de vendas
workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']  # Selecionar a planilha chamada 'vendas'

# Iterar sobre cada linha do arquivo Excel, começando da segunda linha (índice 2)
for linha in vendas_sheet.iter_rows(min_row=2):
    # Nome do cliente
    pyautogui.click(869,524,duration=0.5)  # Clicar no campo de nome do cliente
    pyautogui.write(linha[0].value)  # Digitar o nome do cliente obtido da célula A
    
    # Produto
    pyautogui.click(885,556,duration=0.5)  # Clicar no campo de produto
    pyautogui.write(linha[1].value)  # Digitar o nome do produto obtido da célula B
    
    # Quantidade
    pyautogui.click(960,583,duration=0.5)  # Clicar no campo de quantidade
    pyautogui.write(str(linha[2].value))  # Digitar a quantidade como string obtida da célula C
    
    # Categoria do produto
    pyautogui.click(815,604,duration=0.5)  # Abrir o menu de seleção de categoria
    pyautogui.write(linha[3].value)  # Digitar a primeira letra da categoria obtida da célula D
    pyautogui.click(819,569,duration=0.5)  # Clicar no ícone de seta para baixo
    pyautogui.click(818,565,duration=0.5)  # Selecioinar a categoria do produto
