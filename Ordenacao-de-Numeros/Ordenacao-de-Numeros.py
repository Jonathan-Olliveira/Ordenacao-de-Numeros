lista_com_ordem = []
lista_sem_ordem = []

while True:
    try:
        print("Escolha a quantidade de números que deseja colocar:")
        escolha = int(input())

        for i in range(escolha):
            print("\nInsira o número", i, ":")
            for j in range(1):
                numb = float(input())
                lista_com_ordem.append(numb)
                lista_sem_ordem.append(numb)
        sem_ordem = lista_sem_ordem
        com_ordem = lista_com_ordem.sort()

        resultado_sem_ordem = ", ".join(map(str, lista_sem_ordem))
        print("Números digitado(s): ", resultado_sem_ordem)

        resultado_com_ordem = ", ".join(map(str, lista_com_ordem))
        print("Números ordenado(s) :", resultado_com_ordem)

        break
    except ValueError:
        print("\nÉ permitido somente numeros, tente novamente!\n")
        lista_com_ordem.clear()
        lista_sem_ordem.clear()

#DEU MUITOOOO TRABALHO

#COLOQUEI A OPÇÃO DE O USUARIO ESCOLHER QUANTOS NUMEROS ELE QUER ADICIONAR

#PERCEBI UM BUG QUANDO VOCÊ ADICIONAVA O PRIMEIRO NUMERO, E DEPOIS AO ADICIONAR O SEGUNDO, SE COLOCASSE UMA LETRA, ELE ARMAZENAVA O PRIMEIRO, E SEGUIA O EXCEPT,
#NISSO QUANDO O LOOP RODAVA E COLOCAVA TUDO CERTO, NA SAIDA APARECIA O NUMERO QUE NAO SEGUIU O FLUXO + O FLUXO QUE DEU CERTO, POR ISSO COLOQUEI UM CLEAR NO EXCEPT

#GITHUB: https://github.com/Jonathan-Olliveira