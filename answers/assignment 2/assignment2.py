# Declarando as variáveis
num1 = int(0)
num2 = int(1)
num3 = int(0)

print("# Sequência de Fibonacci #")
print("Consulte se um número pertence à Sequência de Fibonacci.")

# Recebendo como entrada o número a ser consultado
numDigitado = int(input("Digite um número:"))

# Calculando a sequência com base no número informado
while numDigitado > num3:
    num3 = num1 + num2
    num1 = num2
    num2 = num3

# Caso o número seja igual a zero ou 1:
if numDigitado == 0 | numDigitado == 1:
    print("O número " + str(numDigitado) + " está na sequência de Fibonacci.")

# Caso o número digitado seja igual ao número gerado na sequência, ele pertence à sequência.
elif numDigitado == num3:
    print("O número " + str(numDigitado) + " está na Sequência de Fibonacci.")

# Exceções a estes dois casos não pertencem à sequência de Fibonacci.
else:
    print("O número não está presente na Sequência de Fibonacci.")