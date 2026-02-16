
## estudo de instalação de pacotes - seção 6.4



## obs:


# Aula:
## Podemos usar o comando 'pip' + install para intalar pacotes, é como em java - java i (pacote), ou JS, node i (pacote)
# os pacotes:

# matemática
# O pacote denominado numpy nos permite o acesso a funções de manipulação de dados e cálculos matemáticos.

# visualização de dados 
# O matplotlib e seaborn são utilizados para a visualização de dados e plotagem de gráficos.

# Requisições HTTP
# O requests nos ajuda a fazer solicitações HTTP

# desenvolvimento web
# O django e flask são utilizados para o desenvolvimento Web.

# ex:
# Baixar
# pip i nome_pacote == versao
# pip install pacote >= versao(instala essa versao ou qualquer versao mais recente)
# Atualizar
# pip i --upgrade nome_pacote
# listar
# pip list
# 
# Temos o camando freeze, ele tira uma 'foto' de nossas bibliotecas instaladas 
# pip freeze > arquivo.txt - todas as lb instaladas vão estar aqui
# e depois usar ooo:
# pip install -r arquivo.txt(vai baixar todas as lbm muito pratico e rapido)
# 
# Para desinstalar 
# pip uninstall nome_pacote
# seção 6.5 exemplos de aplicação
import requests
def main():
    url = 'https://www.python.org'
    resposta = requests.get(url)
    print(resposta)
    if resposta.status_code == 200:
        print(resposta.text)

if __name__ == '__main__':
    main()





# Resumo:
