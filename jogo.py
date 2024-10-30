import random
nome = input("Qual o teu nome meu chapa: ")
def intro():
    print("Bem-vindo à Aventura do aventureiro na Floresta Encantada!")
    print("Era uma vez, num reino distante, uma floresta conhecida como a Floresta Encantada.")
    print(f"Um jovem explorador chamado {nome}, encontrou um mapa que promete levar ao coração da floresta,")
    print("onde um antigo tesouro está escondido.")
    print("Você está pronto para a aventura meu chapa? Vamos começar!")

def escolha_inicial():
    print("\nVocê está na entrada da Floresta Encantada.")
    print("1. Entrar na floresta.")
    print("2. Voltar para casa.")
    escolha = input("O que você deseja fazer? (1/2): ")
    return escolha

def floresta():
    print("\nVocê entrou na floresta. A luz da lua brilha através das árvores.")
    print("Você ouve sons estranhos ao seu redor.")
    print("1. Seguir o som misterioso.")
    print("2. Seguir um caminho iluminado por flores brilhantes.")
    escolha = input("O que você deseja fazer? (1/2): ")
    return escolha

def som_misterioso():
    print("\nVocê segue o som misterioso e encontra uma criatura mágica!")
    print("Ela oferece um desafio: resolver um enigma para continuar.")
    enigma = random.choice([
        ("O que é que quanto mais você tira, maior fica?", "buraco"),
        ("O que tem olhos mas não pode ver?", "batata")
    ])
    resposta = input(f"Enigma: {enigma[0]} ")

    if resposta.lower() == enigma[1]:
        print("Você acertou! A criatura mágica abre um caminho para o tesouro.")
        return "tesouro"
    else:
        print("Resposta errada! A criatura desaparece.")
        return "perdido"

def caminho_iluminado():
    print("\nVocê segue o caminho iluminado e encontra um lindo lago.")
    print("À beira do lago, há um velho sábio.")
    print("1. Perguntar sobre o tesouro.")
    print("2. Ignorar o sábio e continuar a explorar.")
    escolha = input("O que você deseja fazer? (1/2): ")
    return escolha

def interacao_sabio():
    print("\nO sábio lhe conta sobre um antigo tesouro, mas diz que você deve ser digno dele.")
    print("Você deve fazer uma boa ação na floresta antes de prosseguir.")
    print("1. Ajudar um animal ferido.")
    print("2. Ignorar e continuar a explorar.")
    escolha = input("O que você deseja fazer? (1/2): ")

    if escolha == "1":
        print("Você ajudou o animal e ganhou a gratidão da floresta.")
        return "tesouro"
    else:
        print("Você ignorou o sábio. A floresta se torna sombria.")
        return "sombrio"

def main():
    intro()
    while True:
        escolha = escolha_inicial()
        if escolha == "1":
            escolha_floresta = floresta()
            if escolha_floresta == "1":
                resultado = som_misterioso()
                if resultado == "tesouro":
                    print("\nVocê encontrou o tesouro escondido! Parabéns, explorador!")
                    break
                else:
                    print("\nVocê se perdeu na floresta e nunca mais foi visto.")
                    break
            elif escolha_floresta == "2":
                escolha_sabio = caminho_iluminado()
                if escolha_sabio == "1":
                    resultado = interacao_sabio()
                    if resultado == "tesouro":
                        print("\nVocê encontrou o tesouro escondido! Parabéns, explorador!")
                        break
                    else:
                        print("\nVocê ignorou o sábio e a floresta se tornou sombria. Você nunca saiu dela.")
                        break
                else:
                    print("\nVocê ignorou o sábio e a floresta se tornou sombria. Você nunca saiu dela.")
                    break
        elif escolha == "2":
            print("\nVocê voltou para casa. A aventura termina aqui.")
            break
        else:
            print("\nEscolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
