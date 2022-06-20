# Este programa tem como função receber uma palavra digitada pelo usuário e devolver a palavra invertida.
print("--- Inversor de palavras ---")

# Recebendo o input do usuário
palavra = input("Digite uma palavra:")

# Declarando o array que irá receber os caracteres da palavra
caracteres = []

# Declarando a string que irá receber os caracteres invertidos para formar a nova palavra
inverse = ''

# Laço de repetição: executa uma iteração para cada letra da palavra
for letra in palavra:
    # Salva a letra no array de caracteres
    caracteres.append(letra)

# Salvando o tamanho do array (quantidade de letras) menos 1 para usar como base para o próximo laço de repetição.
tam = len(caracteres) - 1

# Laço de repetição: percorre o array de caracteres de forma inversa e salva cada caractere na String inverse.
while tam >= 0:
    inverse += (caracteres[tam])
    tam -= 1

print("Palavra invertida: ")
print(inverse)