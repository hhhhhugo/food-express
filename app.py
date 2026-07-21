import os;
restaurantes = ['Irmaos pizzaria', 'Mc Ronalds']
def exibir_nome_do_prgrama():
    print ('🆂🅰🅱🅾🆁 🅴🆇🅿🆁🅴🆂🆂 \n');
def listar_restaurante():
    os.system('cls')
    print('Listas de restaurantes')
    for restaurante in restaurantes:
        print('- '+ f'{restaurante}')
    input('\nDigite uma tecla para voltar ao menu principal')
    main()
def exibir_opcoes ():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. sair\n')
def finalizar_app():
    os.system('cls')
    print ('finalizando o app\n')
def opcao_invalida():
    print('opcao invalida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()
def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:\n')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal')
    main()
def escolher_opcao ():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurante()
            case 3:
                print('Ativar restaurante')  
            case 4:
                finalizar_app()  
            case int():
                opcao_invalida()
    except:
        opcao_invalida()

def main ():
    os.system('cls')
    exibir_nome_do_prgrama()
    exibir_opcoes()
    escolher_opcao()

if __name__ ==    '__main__':
    main()