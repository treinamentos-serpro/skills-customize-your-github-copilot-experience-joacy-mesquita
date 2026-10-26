# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI. Você praticará rotas HTTP, modelos de dados, validação de entrada e códigos de resposta.

## 📝 Tarefas

### 🛠️ Criar a aplicação e as rotas de leitura

#### Descrição
Prepare o ambiente, inicie a aplicação FastAPI e implemente rotas para consultar todas as tarefas e uma mensagem inicial da API.

#### Requisitos
O programa concluído deve:

- Instalar FastAPI e Uvicorn com `python -m pip install fastapi uvicorn`.
- Criar a aplicação no arquivo `main.py`.
- Implementar `GET /` com uma resposta JSON que identifique a API.
- Implementar `GET /tasks` para retornar a lista de tarefas com `id`, `title` e `completed`.
- Iniciar o servidor com `uvicorn main:app --reload` e permitir testar as rotas em `/docs`.

### 🛠️ Criar e consultar tarefas

#### Descrição
Adicione um modelo de dados para validar as informações recebidas e implemente a criação de tarefas e a consulta de uma tarefa específica.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic com título obrigatório e não vazio e campo `completed` com valor padrão `false`.
- Implementar `POST /tasks` para criar uma tarefa com um identificador único.
- Retornar a tarefa criada com o código HTTP `201`.
- Implementar `GET /tasks/{task_id}` para retornar uma tarefa pelo identificador.
- Retornar o código HTTP `404` quando o identificador não existir.

### 🛠️ Atualizar e remover tarefas

#### Descrição
Complete as operações da API permitindo atualizar ou remover uma tarefa existente e tratando identificadores desconhecidos.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /tasks/{task_id}` para atualizar o título e o estado `completed` da tarefa.
- Implementar `DELETE /tasks/{task_id}` para remover a tarefa e retornar o código HTTP `204`.
- Retornar o código HTTP `404` ao tentar atualizar ou remover uma tarefa inexistente.
