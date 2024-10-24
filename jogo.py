def inicio_jogo():
  print("Bem-vindo à Aventura do aventureiro na Floresta Encantada!")
  print("Tu és um aventureiro em busca de um tesouro.")
  print("Antes de entrar na floresta, precisas de coletar alguns equipamentos.")
  ingredientes = coletar_ingredientes()
  entrar_floresta(ingredientes)

def coletar_ingredientes():
  print("\nNa aldeia, encontras três ingredientes mágicos disponíveis:")
  print("1. espada magica")
  print("2. arquiflexa escandado")
  print("3. escudo de escama de dragão")
  while len(ingredientes) < 1:
    escolha = input("Escolhe um ingrediente para coletar (1/2/3): ")
    if escolha == '1' and "espada magica" not in ingredientes:
        ingredientes.append("espada mgica")
        print("Coletaste espada magica!")
    elif escolha == '2' and "arquiflexa escantado" not in ingredientes:
        ingredientes.append("arquiflexa encantado")
        print("Coletaste arquiflexa encantado!")
    elif escolha == '3' and "escudo de escama de dragão" not in ingredientes:
        ingredientes.append("escudo de escama de dragão")
        print("Coletaste escudo de escama de dragão!")
    else:
        print("Escolha inválida ou já coletaste esse ingrediente. Tenta novamente.")
      
  entrar_floresta(ingredientes)
      

  
