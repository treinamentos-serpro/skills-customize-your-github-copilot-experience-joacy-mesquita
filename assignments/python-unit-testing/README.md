# 📘 Atividade: Automated Testing with unittest

## 🎯 Objetivo

Aprenda a testar funções Python com a biblioteca padrão `unittest`. Você vai verificar resultados esperados, valores-limite e entradas inválidas para encontrar defeitos antes que eles cheguem aos usuários.

## 📝 Tarefas

### 🛠️ Escrever testes para cálculos simples

#### Descrição
Use o arquivo `starter-code.py` para escrever testes para a função `calculate_average`. Comece com entradas comuns e confirme os resultados esperados.

#### Requisitos
O programa concluído deve:

- Criar uma classe de testes derivada de `unittest.TestCase`.
- Verificar a média de uma lista com vários valores e de uma lista com um único valor.
- Usar assertions do `unittest` para comparar os resultados esperados com os obtidos.
- Executar os testes com `python starter-code.py`.

### 🛠️ Testar classificações e valores-limite

#### Descrição
Adicione testes para `classify_score`, que converte uma nota entre 0 e 100 em uma classificação de A a F. Verifique os limites entre as faixas, não apenas valores no meio de cada faixa.

#### Requisitos
O programa concluído deve:

- Verificar as faixas A (90 a 100), B (80 a 89), C (70 a 79), D (60 a 69) e F (0 a 59).
- Testar os valores de limite 0, 59, 60, 69, 70, 79, 80, 89, 90 e 100.
- Organizar os testes de forma que cada caso com falha indique claramente qual comportamento precisa ser corrigido.

### 🛠️ Verificar entradas inválidas

#### Descrição
Complete a cobertura de testes verificando como as funções respondem a dados inválidos e rode toda a suíte para revisar os resultados.

#### Requisitos
O programa concluído deve:

- Confirmar que `calculate_average` gera `ValueError` para uma lista vazia.
- Confirmar que `classify_score` gera `ValueError` para notas menores que 0 ou maiores que 100.
- Usar `assertRaises` para verificar as exceções esperadas.
- Executar a suíte completa com `python starter-code.py` e corrigir os defeitos encontrados nos testes ou nas funções.
