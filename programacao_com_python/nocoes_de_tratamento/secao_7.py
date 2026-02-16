# obs

# aula:
# tratando erros!
# quando pedimos o nome de um usuario para o cadastro, confiamos em sua acertividade, e que ele possivelmente não irá simplesmente digitar numeros invés de letras!!!

# Para resolver, possiveis erros usamos o try/except
# 
# 
try:
    numero_text = "26"
    numero = 123

    soma = numero_text + numero
except TypeError as e:
    print(f"Erro: {e}")
    print("Digite apenas letras camarada!")

try:
    n = 0
    r = 0 / n 

except ValueError as e:
    print(f"Error: {e}")
    print("Apenas numeros")
except ZeroDivisionError as e:
    print(f"Error: {e}") # template string ou f-string(esse é o nome em py)

except Exception as e: # Erro generico, preguiça pra codar? vai nesse.
    print(f"Error: {e}")
    print("Apenas numeros")
else:
    print(f"O resultado foi: {r:.2f}")
finally: # podemos usar para sempre aparecer no fim
    print("Fim da execução")
    # O finally é essencial quando desejamos finalizar um fluxo com a limpeza do campo de preenchimento ou mesmo fechar um arquivo de texto aberto.

# tambem chamadad de exceções do tipo build-in, já vem junto como padrão no python(comandos basicos )
# resumo:
