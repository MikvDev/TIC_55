# Manipulação de arquivos

#obs:

#Aula:
# a função open()

# open("teste_com_open", "w")
# possui 2 paramentros, "arquivo_nome, modo de execução"

# a função close() - Fecha arquivos 😃 - bem simples

# Modos de execução

# a - append
# abre um arquivo já feito e anexa algo nele

# open("teste_com_open","a")

# w - write
# cria um arquivo novo, se ele ja existir apagada tudo do outro

# open("teste_com_open2","w")


# r - read
# abre um arquivo ja feito e lê ele
# open("teste_com_open","r")

# x - tipo escrever
# ele cria um arquivo e abre para você escrver algo nele
# open("teste_com_open","x")

#rt
# Para ler textos - str
# open("teste_com_open","rt")

# wt ou rt
# O “rt” é a leitura das informações de texto e o “wt” realiza a escrita em arquivos externos.
# open("teste_com_open","wt")

# temos o a+ e w+
# a + abre um arquivo e anexa  informações ao final dele
# w + abre um arquivo, possibilita a leitura e a escrita no arquivo

#obs: se usarmos rb, wb ou o B, lidamos com arquivos binarios

# Testes
#
# with open("teste_com_open2", "w") as arquivo:
#     arquivo.write("OIii isso é um teste com write")
with open("teste_com_open","w+") as arquivo_escrita:

    arquivo_escrita.write(" \n Isso é uma escrita com write")

with open('teste_com_open','r') as arquivo_leitura:
    mensagem = arquivo_leitura.read()
    print(mensagem)


#Resumo: