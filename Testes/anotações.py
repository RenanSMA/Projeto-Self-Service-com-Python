# Lista de ingredientes com informações nutricionais (por exemplo, Calorias, proteínas, Carboidratos)
ingredientes = [
    {'nome': '(Frango):', 'Calorias =': 335, 'Proteínas =': 25, 'Carboidratos =': 0},
    {'nome': '(Arroz):', 'Calorias =': 130, 'Proteínas =': 2.7, 'Carboidratos =': 28},
    {'nome': '(Feijão):', 'Calorias =': 132, 'Proteínas =': 8.5, 'Carboidratos =': 24},
    # Adicione mais ingredientes conforme necessário
]

# Ajuda do Professor:

for ingrediente in ingredientes:

  for item in ingrediente:
    if item == 'nome':
      print(ingrediente[item])
    else:
      print(item, ingrediente[item])

