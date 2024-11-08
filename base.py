# Lista de ingredientes com informações nutricionais (por exemplo, calorias, proteínas, carboidratos)
ingredientes = {
    '(GRÃOS):': {' '},
    'Arroz': {'Gramas': 200, 'calorias': 130, 'proteinas': 2.7, 'carboidratos': 28},
    'Feijão': {'calorias': 132, 'proteinas': 8.5, 'carboidratos': 24},
    # Adicione mais ingredientes conforme necessário
}

def montar_prato():
    prato = []
    while True:
        print("Ingredientes disponíveis:")
        print(' ')
        for ingrediente in ingredientes.keys():
            print(ingrediente)
        escolha = input("Escolha um ingrediente (ou 'sair' para finalizar): ")
        if escolha.lower() == 'sair':
            break
        elif escolha not in ingredientes.keys():
            print("Ingrediente não disponível. Tente novamente.")
        else:
            prato.append(escolha)
    return prato

def tabela_nutricional(prato):
    tabela = {'calorias': 0, 'proteinas': 0, 'carboidratos': 0}
    for ingrediente in prato:
        for nutriente in tabela.keys():
            tabela[nutriente] += ingredientes[ingrediente][nutriente]
    return tabela

prato = montar_prato()
tabela = tabela_nutricional(prato)

print("– Prato feito:", prato)
print("– Informoções Nutricionais:", tabela)




