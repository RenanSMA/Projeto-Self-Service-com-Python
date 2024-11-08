# Selfservice com PYTHON - Um restaurante com self-service deseja oferecer aos seus clientes uma maneira de montar seus pratos e obter informações nutricionais detalhadas. Isso permitiria que os clientes escolhessem seus alimentos com base em suas necessidades dietéticas, preferências e objetivos nutricionais. A gerência do restaurante quer implementar um sistema interativo para ajudar os clientes a compor seus pratos e ver instantaneamente as informações nutricionais dos alimentos selecionados.

'PARTE 1 - Definição dos Ingredientes e Suas Informações Nutricionais'
# Lista de ingredientes com informações nutricionais (por exemplo, calorias, proteínas, carboidratos)

# "ingredientes" é um dicionário onde cada chave é o nome de um ingrediente, e o valor associado é outro dicionário com informações nutricionais como quantidade em gramas, calorias, proteínas e carboidratos.

# Categorias de Ingredientes: Linhas como '– (CARNES BOVINAS):' são usadas como separadores visuais no dicionário para organizar as categorias de ingredientes.

# Entradas vazias: Linhas como ' ': {' '} são entradas vazias que servem para adicionar espaçamento entre categorias.


ingredientes = {
    '– (CARNES BOVINAS):': {' '},
    'Bife': {'gramas(g)': 150, 'calorias(kcal)': 270, 'proteínas(g)': 30, 'carboidratos(g)': 0.7},
    'Filé Mignon': {'gramas(g)': 150, 'calorias(kcal)': 348, 'proteínas(g)': 23, 'carboidratos(g)': 0.5},
    'Picanha': {'gramas(g)': 150, 'calorias(kcal)': 414, 'proteínas(g)': 25, 'carboidratos(g)': 0},
    'Contrafilé': {'gramas(g)': 160, 'calorias(kcal)': 330, 'proteínas(g)': 22, 'carboidratos(g)': 0},
    'Costela Desfiada': {'gramas(g)': 155, 'calorias(kcal)': 350, 'proteínas(g)': 58, 'carboidratos(g)': 0},
    ' ': {' '},
    '– (CARNES DE FRANGO):': {' '},
    'Peito de Frango': {'gramas(g)': 150, 'calorias(kcal)': 240, 'proteínas(g)': 31, 'carboidratos(g)': 0},
    'Coxa de Frango': {'gramas(g)': 150, 'calorias(kcal)': 310, 'proteínas(g)': 24, 'carboidratos(g)': 0},
    'Asa de Frango': {'gramas(g)': 150, 'calorias(kcal)': 290, 'proteínas(g)': 23, 'carboidratos(g)': 0},
    ' ': {' '},
    '– (CARNES DE PORCO):': {' '},
    'Costelinha': {'gramas(g)': 150, 'calorias(kcal)': 410, 'proteínas(g)': 23, 'carboidratos(g)': 0},
    'Lombo': {'gramas(g)': 150, 'calorias(kcal)': 320, 'proteínas(g)': 31, 'carboidratos(g)': 0},
    'Bacon': {'gramas(g)': 70, 'calorias(kcal)': 270, 'proteínas(g)': 10, 'carboidratos(g)': 1},
    'Panceta': {'gramas(g)': 150, 'calorias(kcal)': 600, 'proteínas(g)': 15, 'carboidratos(g)': 0},
    ' ': {' '},
    '– (FRUTOS DO MAR):': {' '},
    'Salmão': {'gramas(g)': 150, 'calorias(kcal)': 370, 'proteínas(g)': 34, 'carboidratos(g)': 0},
    'Atum': {'gramas(g)': 150, 'calorias(kcal)': 200, 'proteínas(g)': 42, 'carboidratos(g)': 0},
    'Tilápia': {'gramas(g)': 150, 'calorias(kcal)': 180, 'proteínas(g)': 35, 'carboidratos(g)': 0},
    'Truta': {'gramas(g)': 150, 'calorias(kcal)': 220, 'proteínas(g)': 30, 'carboidratos(g)': 0},
    'Bacalhau': {'gramas(g)': 150, 'calorias(kcal)': 215, 'proteínas(g)': 51, 'carboidratos(g)': 0},
    ' ': {' '},
    '– (GRÃOS):': {' '},
    'Arroz': {'gramas(g)': 200, 'calorias(kcal)': 216, 'proteínas(g)': 4.2, 'carboidratos(g)': 45},
    'Feijão': {'gramas(g)': 100, 'calorias(kcal)': 92, 'proteínas(g)': 6.2, 'carboidratos(g)': 17.7},
    'Macarrão': {'gramas(g)': 150, 'calorias(kcal)': 210, 'proteínas(g)': 7.5, 'carboidratos(g)': 41},
    ' ': {' '},
    '– (LEGUMES E VARIADOS):': {' '},
    'Abobrinha': {'gramas(g)': 150, 'calorias(kcal)': 27, 'proteínas(g)': 2, 'carboidratos(g)': 6},
    'Alface': {'gramas(g)': 50, 'calorias(kcal)': 5, 'proteínas(g)': 0.5, 'carboidratos(g)': 1},
    'Batata Cozida': {'gramas(g)': 150, 'calorias(kcal)': 135, 'proteínas(g)': 2, 'carboidratos(g)': 31},
    'Batata Frita': {'gramas(g)': 150, 'calorias(kcal)': 420, 'proteínas(g)': 4, 'carboidratos(g)': 49},
    'Berinjela': {'gramas(g)': 150, 'calorias(kcal)': 33, 'proteínas(g)': 1.5, 'carboidratos(g)': 8},
    'Brócolis': {'gramas(g)': 150, 'calorias(kcal)': 50, 'proteínas(g)': 4, 'carboidratos(g)': 10},
    'Cebola': {'gramas(g)': 100, 'calorias(kcal)': 40, 'proteínas(g)': 1.1, 'carboidratos(g)': 9.3},
    'Cebolinha': {'gramas(g)': 10, 'calorias(kcal)': 2, 'proteínas(g)': 0.3, 'carboidratos(g)': 0.4},
    'Cenoura': {'gramas(g)': 100, 'calorias(kcal)': 41, 'proteínas(g)': 0.9, 'carboidratos(g)': 9.6},
    'Chuchu': {'gramas(g)': 100, 'calorias(kcal)': 19, 'proteínas(g)': 0.7, 'carboidratos(g)': 4.5},
    'Couve': {'gramas(g)': 100, 'calorias(kcal)': 49, 'proteínas(g)': 4.3, 'carboidratos(g)': 8},
    'Couve-flor': {'gramas(g)': 100, 'calorias(kcal)': 25, 'proteínas(g)': 1.9, 'carboidratos(g)': 4.97},
    'Mandioca Cozida': {'gramas(g)': 100, 'calorias(kcal)': 125, 'proteínas(g)': 1.4, 'carboidratos(g)': 30},
    'Mandioca Frita': {'gramas(g)': 200, 'calorias(kcal)': 640, 'proteínas(g)': 3.4, 'carboidratos(g)': 132},
    'Mandioquinha Refogada': {'gramas(g)': 100, 'calorias(kcal)': 90, 'proteínas(g)': 1.4, 'carboidratos(g)': 20},
    'Pepino': {'gramas(g)': 100, 'calorias(kcal)': 16, 'proteínas(g)': 0.7, 'carboidratos(g)': 3.6},
    'Repolho': {'gramas(g)': 100, 'calorias(kcal)': 25, 'proteínas(g)': 1.3, 'carboidratos(g)': 5.8},
    'Rúcula': {'gramas(g)': 100, 'calorias(kcal)': 25, 'proteínas(g)': 2.6, 'carboidratos(g)': 3.7},
    'Tomate': {'gramas(g)': 100, 'calorias(kcal)': 18, 'proteínas(g)': 0.9, 'carboidratos(g)': 3.9},

    # Adicione mais ingredientes conforme necessário
}

'PARTE 2'
# print("Ingredientes disponíveis:"): Exibe um cabeçalho para a lista de ingredientes.

# for ingrediente in ingredientes.keys(): Itera sobre as chaves do dicionário ingredientes, que são os nomes dos ingredientes e categorias.

# print(ingrediente): Exibe cada ingrediente ou categoria na tela.


'PARTE 3 - Função para Montar o Prato'
# def montar_prato(): Define uma função chamada montar_prato que permite ao usuário escolher ingredientes para o prato.

# prato = []: Inicializa uma lista vazia chamada prato para armazenar os ingredientes escolhidos.

# while True:: Inicia um loop infinito para que o usuário possa adicionar ingredientes ou optar por sair.

# escolha = input("Escolha um ingrediente (ou 'sair' para finalizar): "): Solicita ao usuário para digitar o nome de um ingrediente ou 'sair' para terminar.

# if escolha.lower() == 'sair':: Verifica se o usuário digitou 'sair' (independente de maiúsculas ou minúsculas), e encerra o loop se for o caso.

# elif escolha not in ingredientes.keys():: Verifica se o ingrediente digitado não está na lista de ingredientes disponíveis e, se não estiver, exibe uma mensagem de erro.

# else:: Se o ingrediente estiver disponível, adiciona-o à lista prato.

# return prato: Retorna a lista de ingredientes escolhidos.

print("Ingredientes disponíveis:")
print(' ')
for ingrediente in ingredientes.keys():
  print(ingrediente)

def montar_prato():
    prato = []
    while True:
        escolha = input("Escolha um ingrediente (ou 'sair' para finalizar): ")
        if escolha.lower() == 'sair':
            break
        elif escolha not in ingredientes.keys():
            print("Ingrediente não disponível. Tente novamente.")
        else:
            prato.append(escolha)
    return prato

'PARTE 5 - Função para Calcular a Tabela Nutricional'
# def tabela_nutricional(prato): Define uma função que calcula a tabela nutricional do prato montado.

# tabela = {'gramas(g)': 0, 'calorias(kcal)': 0, 'proteínas(g)': 0, 'carboidratos(g)': 0}: Inicializa um dicionário tabela com todos os nutrientes zerados.

# for ingrediente in prato:: Itera sobre cada ingrediente na lista prato.

# for nutriente in tabela.keys():: Itera sobre cada nutriente na tabela (gramas, calorias, proteínas, carboidratos).

# tabela[nutriente] += ingredientes[ingrediente][nutriente]: Soma o valor de cada nutriente do ingrediente ao valor correspondente na tabela.

# return tabela: Retorna o dicionário tabela com os valores nutricionais totais.


def tabela_nutricional(prato):
    tabela = {'gramas(g)': 0, 'calorias(kcal)': 0, 'proteínas(g)': 0, 'carboidratos(g)': 0}
    for ingrediente in prato:
        for nutriente in tabela.keys():
            tabela[nutriente] += ingredientes[ingrediente][nutriente]
    return tabela


'PARTE 6 - Execução do Programa'

# prato = montar_prato(): Chama a função montar_prato para permitir que o usuário monte seu prato. O resultado é armazenado na variável prato.

# tabela = tabela_nutricional(prato): Chama a função tabela_nutricional com o prato montado para calcular as informações nutricionais. O resultado é armazenado na variável tabela.

# print("– Prato feito:", prato): Exibe a lista de ingredientes que compõem o prato.

# print("– Informações Nutricionais:", tabela): Exibe a tabela nutricional do prato montado.


prato = montar_prato()
tabela = tabela_nutricional(prato)

print('')
print("– Prato feito:", prato)
print("– Informações Nutricionais:", tabela)
