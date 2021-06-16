import flask
import all_dict
# Projeto --- Dicionário português/inglês ----- <3#
"""
##############################################################################################
Nome do programa: Dict_Server.                                                               #
Criadoras: Emanuele Mayara                                                                   #
           Fabiana Carla                                                                     #
           Iara de Melo                                                                      #
                                                                                             #
Função : Conectar com um cliente que possa acerssar, adicionar e/ou remover palavras         #
         de um banco de dados, estruturado com duas tabelas (pt-en e en-pt).                 #
                                                                                             #
Data de Criação :16/02/2017                                                                  #
Ultima alteração:24/02/2017                                                                  #
                                                                                             #
Versão 0.1 - Organização estrutural das rotas principais (IARA)                              #
Versão 0.2 - escrita das estrututas (rotas) e conexão com o banco de dados (IARA)            #
Versão 0.3 - mudança na estrutura com a adição de novas opções e construção da               #
             opção adicionar, remover, consultar. (FABIANA)                                  #
Versão 0.4 - criação da parte básica da opção das 10 mais acessadas (FABIANA)                #
                                                                                             #
Versão 0.5 - Criação de teste para existência da palavra, antes da implemantação             #
             das funções em cada opção, alteração na atualização do contador                 #
             de acesso das palavras(IARA)                                                    #
Versão 0.6 - Adição de opções de adicionar traduções (port / ing) e implementação            #
            da opção de listar as 10 palavras mais acessadas. (IARA)                         #
##############################################################################################
"""
# inicia a conexao com o banco de dados, antes do servidor realizar uma função
all_dict.iniciar()


# iniciar a aplicação -- OK
app = flask.Flask("Dicionario_Web")
app.config["JSON_AS_ASCII"] = False


# rota de inicio - pagina em branco 100% -- NÃO MEXER ONDE ESTÁ 'OK' !!
@app.route("/")
def pag_inicial():
    resposta = {
        "Ansewer": "Pagina em branco",
        "url/OP1": "/add/ing - para adicionar palavras em ingles",
        "url/OP2": "/add/port - para adicionar palavras em portugues",
        "url/OP3": "/rmv/ing - para remover palavras do ingles",
        "url/OP4": "/rmv/port - para remover palavras do portugues",
        "url/OP5": "/con/ing - para consultar palavras",
        "url/OP6": "/con/port - para consultar palavras",
        "url/OP7": "/con10/port - para consultar as 10 mais acessados port --> ing",
        "url/OP8": "/con10/ing - para consultar as 10 mais acessadas ing --> port",
        "url/OP9": "/acr/port - para acrescentar tradução para palavra em português",
        "url/OP10": "/acr/ing - para acrescentar tradução para palavra em inglês"
    }
    return flask.jsonify(resposta)


# 1ª opção adicionar uma palavra em português (com teste de existência) OK
@app.route("/add/port/<string:palavra>/<string:traducao>")
def add(palavra,traducao):
    existe = all_dict.listar_v("count(id)", "palavras where palavra = '%s'" % palavra)[0][0]
    resposta = {"Status": ""}

    if existe == 0:
        all_dict.adicionar("palavras", "palavra", "traducao", "contador_acesso", palavra, traducao, 0)
        resposta["Status"] = "Palavra adicionada com sucesso!"
        return flask.jsonify(resposta)

    else:
        resposta["Status"] = "Palavra já cadastrada no dicionário!"
        return flask.jsonify(resposta)


#2ª opcção adiconar um apalavra em inglês (com teste de existência) OK
@app.route("/add/ing/<string:palavra>/<string:traducao>")
def addi(palavra, traducao):
    resposta = {"Status": ""}
    existe = all_dict.listar_v("count(id)", "words where palavra = '%s'" % palavra)[0][0]

    if existe > 0:
        resposta["Status"] = "Palavra já cadastrada no dicionário"
        return flask.jsonify(resposta)

    else:
        all_dict.adicionar("words", "palavra", "traducao", "contador_acesso", palavra, traducao, 0)
        resposta["Status"] = "Palavra %s cadastrada com sucesso!" % palavra
        return flask.jsonify(resposta)


# 3ª opção remover uma palavra português(com teste de existência) OK
@app.route("/rmv/port/<string:palavra>")
def rm(palavra):
    resposta = {"Status": ""}
    existe = all_dict.listar_v("count(id)", "palavras where palavra = '%s'" % palavra)[0][0]

    if existe > 0:
        all_dict.remover_palavra("palavras", "palavra", palavra)
        resposta["Status"] = "Palavra %s removida com sucesso !"%(palavra)
        return flask.jsonify(resposta)

    else:
        all_dict.remover_palavra("palavras", "palavra", palavra)
        resposta["Status"] = "Palavra %s não cadastrada no dicionário!" % palavra

        return flask.jsonify(resposta)


# 4ª opção remover palavra  inglês (com teste de existência) OK
@app.route("/rmv/ing/<string:palavra>")
def rmi(palavra):
    resposta = {"Status": ""}
    existe = all_dict.listar_v("count(id)", "words where palavra = '%s'" % palavra)[0][0]

    if existe > 0:
        all_dict.remover_palavra("words", "palavra", palavra)
        resposta["Status"] = "Palavra %s removida com sucesso !" % (palavra)
        return flask.jsonify(resposta)

    else:
        all_dict.remover_palavra("words", "palavra", palavra)
        resposta["Status"] = "Palavra %s não cadastrada no dicionário!" % (palavra)

        return flask.jsonify(resposta)


# 5ª opção consultar palavras português (com teste de existência) OK
@app.route("/con/port/<string:palavra>")
def con(palavra):

    existe = all_dict.listar_v("count(id)", "palavras where palavra = '%s'" % palavra)[0][0]

    if existe > 0:
        resposta = {
            "Status": "",
            "Palavra": "",
            "Traducao": "",
            "Acessos": "",
            "marcador": 0
        }

        trad = all_dict.listar_v("traducao", "palavras where palavra = '%s'" % palavra)[0][0]
        acess = all_dict.listar_v("contador_acesso", "palavras where palavra = '%s'" % palavra)[0][0]
        contador_atual = (acess + 1)

        resposta["Status"] = "Palavra Encontrada !"
        resposta["Palavra"] = "%s" % palavra
        resposta["Traducao"] = "%s" % trad
        resposta["Acessos"] = "%d" % contador_atual

        all_dict.atualizar_contador("palavras", "contador_acesso", contador_atual, "palavra", palavra)
        return flask.jsonify(resposta)


    else:
        resposta = {
            "Status": "",
            "marcador": 1}

        resposta["Status"] = "Palavra não cadastrada no dicionário"
        return flask.jsonify(resposta)


# 6ª opção consultar palavras inglês (com teste de existência) OK
@app.route("/con/ing/<string:palavra>")
def coni(palavra):

    existe = all_dict.listar_v("count(id)", "words where palavra = '%s'" % palavra)[0][0]

    if existe > 0:
        trad = all_dict.listar_v("traducao", "palavras where palavra = '%s'" % palavra)[0][0]
        acess = all_dict.listar_v("contador_acesso", "words where palavra = '%s'" % palavra)[0][0]

        resposta = {
            "Status": "",
            "Palavra": "",
            "Traducao": "",
            "Acessos": "",
            "marcador": 0
        }
        contador_atual = acess + 1
        resposta["Status"] = "Palavra existe"
        resposta["Palavra"] = "%s" % palavra
        resposta["Traducao"] = "%s" % trad
        resposta["Acessos"] = "%d" % contador_atual
        all_dict.atualizar_contador("words", "contador_acesso", contador_atual, "palavra", palavra)
        return flask.jsonify(resposta)


    else:
        resposta = {
            "Status": "",
            "marcador": 1
        }
        resposta["Status"] = "Palavra não cadastrada no dicionário"
        return flask.jsonify(resposta)


# 7ª opção consultar as 10 mais port --> ing(com teste) OK --
@app.route("/con10/port")
def as_10_mais_port():

    dezmais_p = all_dict.listar_v("palavra, contador_acesso", "palavras order by contador_acesso desc limit 10" )

    #print(dez_mais)

    # concateno as palavras em uma variavel e os acessos em outra variavel
    # em seguida atualizo os valores do dicionário com o conjunto das variaveis.

    resposta = {
        "Status": "As dez palavras mais acessadas",
        "palavras": "",
        "acessos": ""
    }

    palav = ""
    acess = ""

    for i in dezmais_p:
        palav += "%s," % i[0]
        acess += "%s," % str(i[1])

    resposta["palavras"] = palav
    resposta["acessos"] = acess

    return flask.jsonify(resposta)


# 8ª opção consultar as 10 mais ing --> port(com teste) OK --
@app.route("/con10/ing")
def as_10_mais_ing():

    dezmais_i = all_dict.listar_v("palavra, contador_acesso", "words order by contador_acesso desc limit 10" )

    #print(dez_mais)

    # concateno as palavras em uma variavel e os acessos em outra variavel
    # em seguida atualizo os valores do dicionário com o conjunto das variaveis.

    resposta = {
        "Status": "As dez palavras mais acessadas",
        "palavras": "",
        "acessos": ""
    }

    palav = ""
    acess = ""

    for i in dezmais_i:
        palav += "%s," % i[0]
        acess += "%s," % str(i[1])

    resposta["palavras"] = palav
    resposta["acessos"] = acess

    return flask.jsonify(resposta)


# 9ª opção acrescentar uma tradução a uma palavra em português OK
@app.route("/acr/port/<string:palavra>/<string:traducao>")
def acrport(palavra,traducao):

    existe = all_dict.listar_v("count(id)", "palavras where palavra = '%s'" % palavra)[0][0]

    resposta = {"Status": ""}

    if existe == 0:
        resposta["Status"] = "Palavra não existe!"
        return flask.jsonify(resposta)

    else:
        resposta["Status"] = "Tradução adicionada com sucesso!"

        # função para atualização da tradução
        trads = all_dict.listar_v("traducao", "palavras where palavra = '%s'" % palavra)[0][0]
        trads += "-%s" % traducao
        all_dict.atualizar_trad("palavras", "traducao", trads, "palavra", palavra)
        return flask.jsonify(resposta)


# 10ª opção acrescentar uma tradução a uma palavra em inglês. OK
@app.route("/acr/ing/<string:palavra>/<string:traducao>")
def acring(palavra, traducao):

    resposta = {"Status": ""}

    existe = all_dict.listar_v("count(id)", "words where palavra = '%s'" % palavra)[0][0]

    if existe > 0:
        resposta["Status"] = "Tradução adicionada com sucesso !"

        # função para atualização da tradução
        trads = all_dict.listar_v("traducao", "words where palavra = '%s'" % palavra)[0][0]
        trads += ("-%s" % traducao)
        all_dict.atualizar_trad("words", "traducao", trads, "palavra", palavra)
        return flask.jsonify(resposta)

    else:
        resposta["Status"] = "Palavra não existe!"
        return flask.jsonify(resposta)



# executa o servidor
app.run("0.0.0.0", 3030)