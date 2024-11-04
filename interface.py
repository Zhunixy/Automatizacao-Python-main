# instale o PySimpleGUI antes de rodar este arquivo:
# pip install PySimpleGUI 
# para mac/linux
# pip3 install PySimpleGUI
import PySimpleGUI as sg

# Definir o tema do PySimpleGUI
sg.theme('Reddit')  # Escolher um tema visual agradável

# Lista de categorias de produtos
product_categories = ["Eletrônicos", "Móveis", "Roupas", "Brinquedos", "Comida", "Bebidas", 
                      "Cosméticos", "Livros", "Esportes", "Jardinagem"]  # Opções disponíveis para seleção

def validate_input(value):
    """Função auxiliar para validar entradas"""
    if value.strip():  # Remover espaços em branco
        return value
    else:
        return None

def validate_quantity(quantity):
    """Validar se a quantidade é um número inteiro positivo"""
    try:
        int_quantity = int(quantity)
        if int_quantity > 0:
            return str(int_quantity)
        else:
            return None
    except ValueError:
        return None

# Configurar a layout do formulário
layout = [
    [sg.Text('Cliente', size=(6, 0)), sg.Input(key='1', size=(20, 0))],
    [sg.Text('Produto', size=(6, 0)), sg.Input(size=(20, 0), key='2')],
    [sg.Text('Quantidade'), sg.Input(key='3', size=(3, 0))],
    [sg.Text('Categoria do Produto'), sg.Combo(product_categories, key='4')],
    [sg.Button('Salvar'), sg.Button('Limpar'), sg.Button('Sair')]
]

# Criar a janela do formulário
window = sg.Window('Cadastro de Produtos',layout)  # Título da janela e layout configurado

while True:
    event, values = window.read()  # Ler eventos e valores atualizados da janela
    
    # Verificar se o usuário fechou a janela
    if event == sg.WIN_CLOSED:
        break  # Encerrar o loop se a janela for fechada
    
    # Verificar se o botão 'Salvar' foi clicado
    elif event == 'Salvar':

        client_name = validate_input(values['1'])
        product_name = validate_input(values['2'])
        quantity = validate_quantity(values['3'])

        if all([client_name, product_name, quantity]):
            sg.popup(f'Produto salvo:\n'
                     f'Nome do Cliente: {client_name}\n'
                     f'Nome do Produto: {product_name}\n'
                     f'Quantidade: {quantity}')
            window['1'].update('')
            window['2'].update('')
            window['3'].update('')
            window['4'].update('')
        else:
            sg.popup_error('Por favor, preencha todos os campos corretamente.')

    # Verificar se o botão 'Limpar' foi clicado
    elif event == 'Limpar':
        window['1'].update('')
        window['2'].update('')
        window['3'].update('')
        window['4'].update('')

    # Verificar se o botão 'Sair' foi clicado
    elif event == 'Sair':
        confirm = sg.popup_yes_no('Deseja realmente sair do aplicativo?')
        if confirm == 'Yes':
            break
        sg.popup('Produto Cadastrado')  # Exibir uma mensagem de confirmação
        window['1'].update('')  # Limpar o campo de cliente
        window['2'].update('')  # Limpar o campo de produto
        window['3'].update('')  # Limpar o campo de quantidade
        window['4'].update('')  # Limpar o campo de categoria

    if event == sg.WIN_CLOSED:
        break
