import requests
import all_dict
# ---- Dicionário português - inglês ----- #
"""
##########################################################################################
Nome do programa: Dict_Client.                                                           #
Criadoras: Emanuele Mayara                                                               #
           Fabiana Carla                                                                 #
           Iara de Melo                                                                  #
                                                                                         #
Função : Conectar com um servidor onde pode acerssar, adicionar e/ou remover palavras    #
         de um banco de dados, estruturado com duas tabelas (pt-en e en-pt).             #
                                                                                         #
Data de Criação :16/02/2017                                                              #
Data de Ultima Atualização :24/02/2017                                                   #
Versão 0.1 - Escrita e organização das opções, acesso ao servidor, obtenção              #
             da resposta pelo servidor.(IARA)                                            #
Versao 1.0 - Adição de opções de acrescentar traduções (port / ing) e configurar         #
             a opção de listar as 10 mais acessadas. (IARA)                              #
##########################################################################################
"""

# menu se repete até o user escolher 'sair'
while True:
    url = "http://127.0.0.1:3030"

    all_dict.spc("Menu Principal".center(30, "_"), "", "1 - Para Adicionar palavra / tradução")
    all_dict.spc("2 - Para Remover palavra ", "3 - Para Realizar Consultas", "4 - Para Sair")
    print()
    opcao = int(input(">> "))
    print()
##########################################################################################

    # opção para encerrar o programa e fechar a guia. NÃO MEXER AQUI.
    if opcao == 4:
        all_dict.spc("Encerrando programa", "", "_".center(30, "_"))
        break


    # opção para adicionar palavras (de acordo com o idioma escolhido) port - ing. NÃO MEXER AQUI. 100%
    elif opcao == 1:
        all_dict.spc("Menu".center(30, "_"), "", "1 - Para Adicionar palavra em Português")
        all_dict.spc("2 - Para Adicionar palavra em Inglês",
                     "3 - Acrescentar tradução para uma palavra em português",
                     "4 - Acrescentar tradução para uma palavra em inglês")
        all_dict.spc("5 - Voltar ao menu principal","","")

        escolha = int(input(">> "))
        print()

        # retornar para o menu principal
        if escolha == 5:
            all_dict.spc("...", "", "")

        # Adicionar palavras em port.
        elif escolha == 1:
            palavra = input("Digite a palavra: ")
            traducao = input("Digite a tradução: ")

            url += ("/add/port/%s/%s" % (palavra, traducao))

            acesso = requests.get(url)
            acesso_js = acesso.json()

            print()
            print("Situação:", acesso_js["Status"])
            print()


        elif escolha == 2:
            palavra_ing = input("Digite a palavra: ")
            traducao_ing = input("Digite a tradução: ")

            url += ("/add/ing/%s/%s" % (palavra_ing, traducao_ing))

            acesso = requests.get(url)
            acesso_js = acesso.json()

            print()
            print("Situação:", acesso_js["Status"])
            print()


        elif escolha == 3:
            palavra = input("Digite a palavra: ")
            traducao = input("Digite a tradução: ")

            url += ("/acr/port/%s/%s" % (palavra, traducao))

            acesso = requests.get(url)
            acesso_js = acesso.json()

            print()
            print("Situação:", acesso_js["Status"])
            print()


        elif escolha == 4:
            palavra = input("Digite a palavra: ")
            traducao = input("Digite a tradução: ")

            url += ("/acr/ing/%s/%s" % (palavra, traducao))

            acesso = requests.get(url)
            acesso_js = acesso.json()

            print()
            print("Situação:", acesso_js["Status"])
            print()

        else:
            all_dict.spc("","OPS, opção inválida !","")


    # opção para remover palavra de acordo com o idioma escolhido port - ing. NÃO MEXER AQUI. 100%
    elif opcao == 2:
        all_dict.spc("Menu".center(30, "_"), "", "1 - Para Remover palavra em Português")
        all_dict.spc("2 - Para Remover palavra em Inglês", "3 - Para voltar ao menu principal", "")

        print()
        escolha = int(input(">> "))
        print()

        if escolha == 3:
            all_dict.spc("...", "", "")

        elif escolha == 1:
            palavra = input("Digite a palavra: ")

            url += ("/rmv/port/%s" % palavra)

            acesso = requests.get(url)
            acesso_js = acesso.json()

            print()
            print("Situação:", acesso_js["Status"])
            print()


        elif escolha == 2:
            palavra_ing = input("Digite a palavra: ")

            url += ("/rmv/ing/%s" % palavra_ing)

            acesso = requests.get(url)
            acesso_js = acesso.json()

            print()
            print("Situação:", acesso_js["Status"])
            print()


    # opçãp para consultar palavra de acordo com o idioma escolhido
    elif opcao == 3:
        all_dict.spc("Menu".center(30, "_"), "", "1 - Consultar palavra em Português")
        all_dict.spc("2 - Consultar palavra em Inglês", "3 - Consultar as 10 mais acessadas port -> ing", "4 - Consultar as 10 mais acessadas ing -> port")
        print("5 - Voltar ao menu principal")
        print()
        escolha = int(input(">> "))
        print()

        # opção de encerrar o programa
        if escolha == 5:
            all_dict.spc("...", "", "")

        elif escolha == 1:
            palavra = input("Digite a palavra: ")

            url += ("/con/port/%s" % palavra)

            acesso = requests.get(url)
            acesso_js = acesso.json()

            marcador = acesso_js["marcador"]

            if marcador == 1:
                print()
                print("Situação:", acesso_js["Status"])
                print()

            else:
                print()
                print("Situação:", acesso_js["Status"])
                print("Palavra:", acesso_js["Palavra"])
                print("Tradução:", acesso_js["Traducao"])
                print("Acessos:", acesso_js["Acessos"])
                print()


        elif escolha == 2:
            palavra_ing = input("Digite a palavra: ")

            url += ("/con/ing/%s" % palavra_ing)

            acesso = requests.get(url)
            acesso_js = acesso.json()

            marcadori = acesso_js["marcador"]

            if marcadori == 1:
                print()
                print("Situação:", acesso_js["Status"])
                print()

            else:
                print()
                print("Situação:", acesso_js["Status"])
                print("Palavra:", acesso_js["Palavra"])
                print("Tradução:", acesso_js["Traducao"])
                print("Acessos:", acesso_js["Acessos"])
                print()


        elif escolha == 3:
            print("As 10 palavras mais consultadas port --> ing".center(30, "_"))
            print()
            url += ("/con10/port")
            acesso = requests.get(url)

            # aqui eu recebo duas listas, uma com as palavras e outra com os acessos
            acesso_js = acesso.json()
            nomes = acesso_js["palavras"].split(",")
            acess = acesso_js["acessos"].split(",")

            for i in range(len(nomes) - 1):
                print("%dª: %s | Acessos: %s" % (i, nomes[i], acess[i]))
            print()



        elif escolha == 4:
            print("As 10 palavras mais consultadas ing --> port".center(30, "_"))
            print()
            url += ("/con10/ing")
            acesso = requests.get(url)

            # aqui eu recebo duas listas, uma com as palavras e outra com os acessos
            acesso_js = acesso.json()
            nomes = acesso_js["palavras"].split(",")
            acess = acesso_js["acessos"].split(",")

            for i in range(len(nomes) - 1):
                print("%dª: %s | Acessos: %s" % (i, nomes[i], acess[i]))
            print()


    else:
        print("Ops, opção inválida. Tente novamente !")
