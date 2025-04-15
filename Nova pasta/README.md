# Sniper API

Esta é uma API simples em Flask que recebe e lista sinais de entrada para operações.

## Rotas disponíveis

### `GET /sinais`
Retorna os sinais mais recentes (limite de 10).

### `POST /novo-sinal`
Adiciona um novo sinal.
Exemplo de JSON:
```json
{
  "par": "EUR/USD",
  "direcao": "call",
  "forca": 90,
  "horario": "12:01"
}
```

### `GET /`
Verifica se a API está online.

## Como rodar localmente

```bash
pip install -r requirements.txt
python app.py
```
