# Inserir cada célula de cada linha em um campo do sistema
import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
    # nome
    pyautogui.click(869,524,duration=0.5)
    pyautogui.write(linha[0].value)
    # produto
    pyautogui.click(885,556,duration=0.5)
    pyautogui.write(linha[1].value)
    # quantidade
    pyautogui.click(960,583,duration=0.5)
    pyautogui.write(str(linha[2].value))
    # categoria
    pyautogui.click(815,604,duration=0.5)
    pyautogui.write(linha[3].value)
    pyautogui.click(819,569,duration=0.5)
    pyautogui.click(818,565,duration=0.5)
    
    