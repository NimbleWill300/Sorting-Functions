import random


def sortear(pessoas, funcoes, antigas):
    novas_funcoes = []
    for i in range(len(pessoas)):
        num = random.randint(0, 15)
        while funcoes[num] == antigas[i]:
            num = random.randint(0, 15)

        novas_funcoes.append(funcoes[num])
    
    return novas_funcoes

def ler_arquivo():
    # Abre o arquivo para leitura
    with open("strings.txt", "r") as file:
        # Lê todas as linhas do arquivo e as armazena em uma lista
        lista_strings = file.readlines()

    # Remove o caractere '\n' de cada elemento da lista
    lista_strings = [string.strip() for string in lista_strings]

    file.close()
    # retorna a lista resultante
    return lista_strings


def atualizar_data(funcoes):
    # Abre um arquivo para escrita
    with open("strings.txt", "w") as file:

        # Escreve cada string em uma nova linha no arquivo
        for i in funcoes:
            file.write(i + "\n")
        file.close()

moradores = ["Bide", "Beyblade", "Bilu", "Banguela", "Fanta", "Grinch",
             "Mighelas", "Kiara", "Belucci", "Flaudio", "Ronald", "Shot",
             "Markteto", "Perda", "Tezinho", "Miles"]
funcoes = ["cozinha", "cozinha", "cozinha", "sala", "sala", "sala", "napoleao",
           "napoleao", "area externa", "area externa", "area externa", "sala de estudos e ping pong",
           "sala de estudos e ping pong", "lavanderia", "lavanderia", "banheiros"]

antigas = ler_arquivo()
novas_funcoes = sortear(moradores, funcoes, antigas)
atualizar_data(novas_funcoes)

print("\n----------------------------------------------------------------")
for i in range(len(moradores)):
    if len(moradores[i]) < 6:
        print(f"{moradores[i]}: \t\t{novas_funcoes[i]}")
    else:
        print(f"{moradores[i]}: \t{novas_funcoes[i]}")
print("----------------------------------------------------------------\n")