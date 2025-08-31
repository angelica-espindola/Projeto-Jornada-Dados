# Projeto Jornada de Dados - Extração de Cotações de Commodities

Este projeto tem como objetivo extrair as últimas cotações de commodities financeiras usando a API Yahoo Finance, através da biblioteca `yfinance`.

---

## Descrição

O script principal (`GetCommodities.py`) coleta os preços atuais (intervalo de 1 minuto) das seguintes commodities:

- Ouro (`GC=F`)
- Petróleo (`CL=F`)
- Prata (`SI=F`)

Os dados são organizados em um `DataFrame` com as seguintes colunas:

- **ativo**: código do ativo
- **preco**: último preço de fechamento
- **moeda**: moeda da cotação (USD)
- **horario_coleta**: timestamp da coleta dos dados

---

## Tecnologias utilizadas

- Python 3.x
- [pandas](https://pandas.pydata.org/)
- [yfinance](https://pypi.org/project/yfinance/)

---

## Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/angelica-espindola/Projeto-Jornada-Dados.git
   cd Projeto-Jornada-Dados

