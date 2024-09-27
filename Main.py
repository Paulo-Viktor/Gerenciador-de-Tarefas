from Funções import *
from time import sleep

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
    


    
        

    



