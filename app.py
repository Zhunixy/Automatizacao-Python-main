# Inserir cada célula de cada linha em um campo do sistema
import openpyxl
import pyautogui
import threading
import time

workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']

def stop():
    global stopped
    if not stopped:
        stopped = True
        print("Automatação encerrada")
    
stopped = False

def automation_loop():
    global stopped
    
    # Carregar o arquivo Excel de vendas
    workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
    vendas_sheet = workbook['vendas']
    
    # Iterar sobre cada linha do arquivo Excel, começando da segunda linha (índice 2)
    for linha in vendas_sheet.iter_rows(min_row=2):
        # Nome do cliente
        pyautogui.click(1164,314,duration=0.5)  # Clicar no campo de nome do cliente
        pyautogui.write(linha[0].value)  # Digitar o nome do cliente obtido da célula A
        
        # Produto
        pyautogui.click(1148,406,duration=0.5)  # Clicar no campo de produto
        pyautogui.write(linha[1].value)  # Digitar o nome do produto obtido da célula B
        
        # Quantidade
        pyautogui.click(1158,509,duration=0.5)  # Clicar no campo de quantidade
        pyautogui.write(str(linha[2].value))  # Digitar a quantidade como string obtida da célula C
        
        # Categoria do produto
        pyautogui.click(1353,604,duration=0.5)  # Abrir o menu de seleção de categoria
        pyautogui.write(linha[3].value)  # Digitar a primeira letra da categoria obtida da célula D
        pyautogui.click(1120,612,duration=0.5)  # Clicar no ícone de seta para baixo
        pyautogui.click(1187,685,duration=0.5)  # Selecioinar a categoria do produto
        pyautogui.click(1371,189,duration=0.5)
    
    print("Automatação concluída")

def mouse_monitor():
    global stopped
    
    last_click_time = time.time()
    click_interval = 0.5  # Tempo máximo entre cliques
    
    while True:
        current_time = time.time()
        if current_time - last_click_time > click_interval:
            stop()
            break
        time.sleep(0.1)

def main():
    global stopped
       
    # Iniciar a thread de automação
    automation_thread = threading.Thread(target=automation_loop)
    automation_thread.start()
    
    # Aguardar até que a automação seja encerrada ou o programa seja fechado
    while not stopped:
        time.sleep(0.1)


if __name__ == "__main__":
    main()
    main()
