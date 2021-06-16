import sqlite3
"""
#########################################################################
Nome do programa: all_dict.                                             #
Criadoras: Emanuele Mayara                                              #
           Fabiana Carla                                                #
           Iara de Melo                                                 #
                                                                        #
Função : Armazenar funções para outros programas utilizarem.            #
                                                                        #
Data de Criação :16/02/2017                                             #
Data de Ultima Atualização :23/02/2017                                  #
                                                                        #
Versão  :0.1                                                            #
Versão  :0.2 adicão da função remover e consultar; banco                #
         de dados atualizado,incremenar contador(FABIANA)               #
Versão  :0.3 Adição de funções para mostrar na tela e de atualização    #
             de valores em um banco de dados.(IARA)                     #
#########################################################################
"""

conexao_bd = None


def iniciar():
    global conexao_bd
    conexao_bd = sqlite3.connect("BANCO_PALAVRAS.db")
    print("Conexão iniciada")


def listar_v(x, y):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("SELECT %s FROM %s" % (x, y))
    conexao_bd.commit()
    resp = conex_sel.fetchall()
    conex_c.close()
    return resp


# adiciona a palavra e sua tradução mas não encrementa o contador, pois tera uma função
# separada para isso, para atualizar o contador.
def adicionar(tabela, palavra, tradu, conta, valorp, valort, valorc):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("insert into %s (%s, %s, %s) values (?, ?, ?)" % (tabela, palavra, tradu, conta), (valorp, valort, valorc))
    conexao_bd.commit()
    resp = conex_sel.fetchall()
    conex_c.close()
    return resp


#  update conta set saldo = ? where numero = ? and agencia = ?
def incrementar_contador(tabela, campo_contador, cont, campo_palavra, palavra):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("update %s set %s = ? where %s = ?" % (tabela, campo_contador, campo_palavra), (cont, palavra))
    conexao_bd.commit()
    resp = conex_sel.fetchall()
    conex_c.close()



#  delete from words where word = 'test'
def remover_palavra(tabela, campo_palavra, palavra):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("delete from %s where %s = '%s'" % (tabela, campo_palavra, palavra))
    conexao_bd.commit()
    conex_c.close()
    return conex_sel.rowcount == 1


#  select traducao from palavras where palavra = 'teste'
def consultar(campo_traducao, campo_contador, tabela, campo_palavra, palavra):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_c.execute("select %s,%s from %s where %s = '%s'" % (campo_traducao, campo_contador, tabela, campo_palavra, palavra))
    resultado = conex_c.fetchone()
    conex_c.close()

    return resultado



# SELECT palavra, traducao, contador_acesso from palavras order by contador_acesso asc LIMIT 10;
def consultar_as_10_mais(campo_palavra, campo_traducao, campo_contador, tabela, campo_contador2):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_c.execute("select %s,%s,%s from %s order by %s asc limit 10" % (campo_palavra,campo_traducao,
                                                                       campo_contador,tabela,campo_contador2))
    resultado = conex_c.fetchone()
    conex_c.close()
    return resultado


# EX: update produto set quantidade = 33 where medida = "Kg";
def atualizar_contador(tabela, campo, n_valor, nome, palavra):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("update %s set %s = %d where %s = '%s'" % (tabela, campo, n_valor, nome, palavra))
    conexao_bd.commit()
    conex_c.close()


def atualizar_trad(tabela, campo,nc, nome, palavra):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("update %s set %s = '%s' where %s = '%s'" % (tabela, campo, nc, nome, palavra))
    conexao_bd.commit()
    conex_c.close()


def spc(x, y, z):
    print(x)
    print(y)
    print(z)


