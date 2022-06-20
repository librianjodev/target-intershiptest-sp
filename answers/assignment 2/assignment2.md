# Questão 2 - Pergunta

Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código.

## Resposta

Para resolver essa questão, é necessário compreender como funciona a lógica por trás da Sequência de Fibonacci:

Os três primeiros números da sequência são 0, 1 e 1. A partir daí, os próximos termos da sequência serão iguais à soma dos dois anteriores:

Exemplo:

>O quarto número da sequência é 2, que equivale à soma dos dois termos anteriores (1+1=2). Logo, o número seguinte a esse será três, que é a soma dos dois termos anteriores (2+1=3).

Sendo assim, o algoritmo criado para solucionar o problema realiza as seguintes operações:

1. Armazena o número digitado pelo usuário.


2. Gerar a sequência de Fibonacci de forma iterativa (com um laço While), que funciona enquanto o número gerado da sequência for menor que o número digitado. Trecho de código abaixo:

``` Python
while numDigitado > num3:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
```

3. Realiza a comparação dos dois números através de laços condicionais (IF), testando as seguintes condições:

```Python
# Caso o número seja igual a zero ou 1:
if numDigitado == 0 | numDigitado == 1:
    print("O número " + str(numDigitado) + " está na sequência de Fibonacci.")

# Caso o número digitado seja igual ao número gerado na sequência, ele pertence à sequência.
elif numDigitado == num3:
    print("O número " + str(numDigitado) + " está na Sequência de Fibonacci.")

# Exceções a estes dois casos não pertencem à sequência de Fibonacci.
else:
    print("O número não está presente na Sequência de Fibonacci.")
```

4. Ao final da execução, o programa informa se o número pertence ou não à Sequência de Fibonacci.

O código-fonte completo pode ser acessado [clicando aqui](./assignment2.py).