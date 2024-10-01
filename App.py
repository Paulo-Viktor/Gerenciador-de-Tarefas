from time import sleep

def titulos(msg):
    print('=' * 70)
    print(f'{msg}'.center(70).upper())
    print('=' * 70)

def subtitulos(msg):
    print('=-' * 35)
    print(f'{msg}'.center(70).upper())
    print('=-' * 35)

def menu_principal():
    print()
    subtitulos('Menu Principal')
    print('''Selecione uma ação com base em seu número de correspondência:
    
1 - Adicionar uma tarefa
2 - Alterar uma tarefa
3 - Concluir tarefa
4 - Excluir tarefa
5 - Mostras todas as tarefas
0 - Sair do programa\n''')

    tarefa = input('-> ')

    while tarefa not in ['0', '1', '2', '3', '4', '5']:
        tarefa = input('\nERRO! Por favor, digite um número válido:\n-> ')
    
    return tarefa

def adicionar_tarefa(dicionario):
    subtitulos('Adicionando tarefa')
    add_tarefa = input('Digite a tarefa que deseja adicionar (Exe.: Fazer lição de casa...):\n-> ')
     
    while add_tarefa == '':
        add_tarefa = input('\nERRO! A tarefa não pode estar vazia.\n-> ')

    if dicionario:
        ultima_tarefa = next(reversed(dicionario))
        chave_tarefa = int(ultima_tarefa) + 1

        dicionario[f'{str(chave_tarefa)}'] = add_tarefa
    else:
        dicionario['1'] = add_tarefa

    print('\nTarefa adicionada com sucesso!')

def alterar_tarefa(dicionario):
    if not dicionario:
        print('\nNão é possível alterar nenhuma tarefa, pois a lista está vazia')
    else:
        subtitulos('Alterando Tarefa')
        print('Digite o número da tarefa que deseja alterar:\n')
        for chave, valor in dicionario.items():
            print(f'{chave} - {valor}')

        alt_tarefa = input('\n-> ')

        if alt_tarefa in dicionario:
            print(f'\nAlterando a tarefa: "{dicionario[alt_tarefa]}"')
            alteracao = input('-> ')

            dicionario[alt_tarefa] = alteracao

            print('\nTarefa alterada com sucesso!')
        else:
            print('\nTarefa não encontrada!')

def concluir_tarefa(dicionario):
    if not dicionario:
        print('Não é possível concluir nenhuma tarefa, pois a lista está vazia!')
    else:
        subtitulos('Concluir tarefa')
        print('\nDigite o número da tarefa que deseja concluir:\n')
        for chave, valor in dicionario.items():
            print(f'{chave} - {valor}')

        concluir_tarefa = input('\n-> ')

        if concluir_tarefa in dicionario:
            tarefa_para_concluir = dicionario[concluir_tarefa]

            dicionario[concluir_tarefa] = f'{tarefa_para_concluir} (CONCLUÍDA)'

            print('\nTarefa concluída com sucesso!')
        else:
            print('\nTarefa não encontrada!')

def mostrar_todas_as_tarefas(dicionario):
    if not dicionario:
        print('Não é possível mostrar nenhuma tarefa, pois a lista está vazia!')
    else:
        subtitulos('Mostrando todas as tarefas')
        print()
        for chave, valor in dicionario.items():
            print(f'{chave} - {valor}')
    
def excluir_tarefa(dicionario):
    if not dicionario:
        print('Não é possível excluir nenhuma tarefa, pois a lista está vazia!')
        return
    else:
        subtitulos('Excluindo tarefa')
        print('Digite o número da tarefa que deseja excluir:\n')
        for chave, valor in dicionario.items():
            print(f'{chave} - {valor}')

        del_tarefa = input('-> ')

        if del_tarefa in dicionario: 
            del dicionario[del_tarefa]

            print('\nTarefa excluída com sucesso!')        
        else:
            print('\nTarefa não encontrada!')
            
def criar_arquivo_ou_ler_existente():
    ''' Verificar se já existe o arquivo, caso não, cria um novo'''
    import os

    dicionario = {}

    try:
        if os.path.exists('Lista de Tarefas.txt'):
            with open('Lista de Tarefas.txt', 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    tarefa = linha.split(':')

                    dicionario[tarefa[0]] = f'{tarefa[1].strip()}'
        else:
            with open('Lista de Tarefas.txt', 'w', encoding='utf-8') as arquivo:
                pass
    except IndexError:
        print('ERRO! O arquivo criado contém muitas linhas vazias!\nPor favor, elimine-as para continuar.')
        return None
        
    return dicionario

def salvar_tarefas_no_arquivo_e_reordenar_dicionario(dicionario):
    novo_dicionario = {indice: valor for indice, (chave, valor) in enumerate(dicionario.items(), start=1)}

    dicionario = novo_dicionario

    with open('Lista de Tarefas.txt', 'w', encoding='utf-8') as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(f'{chave}: {valor}\n')

titulos('lista de tarefas')

sleep(1)

while True:
    lista_tarefas = criar_arquivo_ou_ler_existente()

    if lista_tarefas is None:
        sleep(0.75)
        print('\nSaindo do programa...')
        sleep(0.75)
        break

    tarefa = menu_principal()     

    if tarefa == '1':
        adicionar_tarefa(lista_tarefas)

    elif tarefa == '2':
        alterar_tarefa(lista_tarefas)

    elif tarefa == '3':
        concluir_tarefa(lista_tarefas)

    elif tarefa == '4':
        excluir_tarefa(lista_tarefas)
        
    elif tarefa == '5':
        mostrar_todas_as_tarefas(lista_tarefas)   
    
    elif tarefa == '0':
        print('\nSaindo do programa...')
        if lista_tarefas:
            salvar_tarefas_no_arquivo_e_reordenar_dicionario(lista_tarefas)

        sleep(0.75)
        break
    
    salvar_tarefas_no_arquivo_e_reordenar_dicionario(lista_tarefas)

    continuar = input('\nDeseja continuar? (S/N)\n-> ').upper()

    while continuar not in ['S', 'N']:
        continuar = input('\nERRO! Por favor, digite S ou N:\n-> ').upper()

    if continuar == 'N':
        print('\nSaindo do programa...')
        sleep(1)
        break
    


    
        

    



