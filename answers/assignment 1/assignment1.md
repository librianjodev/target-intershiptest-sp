# Questão 1 - Pergunta

Observe o trecho de código abaixo:

```
int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça {
    K = K + 1;
    SOMA = SOMA + K;
}

imprimir(SOMA);
```

Ao final do processamento, qual será o valor da variável SOMA?

## Resposta

Para resolver essa questão, podemos realizar o teste de "mesa" através da tabela abaixo:

Iteração  | INDICE | K | SOMA
----------|--------|---|-----
1         |   13   | 1 |  1
2         |   13   | 2 |  3
3         |   13   | 3 |  6
4         |   13   | 4 |  10
5         |   13   | 5 |  15
6         |   13   | 6 |  21
7         |   13   | 7 |  28
8         |   13   | 8 |  36
9         |   13   | 9 |  45
10        |   13   | 10|  55
11        |   13   | 11|  66
12        |   13   | 12|  78
13        |   13   | 13|  91
Fim       |   --   | --|  --

Sendo assim, ao final das execuções, a variável soma terá como valor o número 91.
Foi criado um algoritmo em Python para testar e comprovar essa resposta, que pode ser acessado [clicando aqui](assignment1.py).