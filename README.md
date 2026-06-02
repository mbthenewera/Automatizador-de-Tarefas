# Task Automation API + CLI

![Python](https://img.shields.io/badge/Python-API%20%2B%20CLI-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-portfolio-111111?style=flat-square)

Projeto em Python para automação de arquivos com duas formas de uso: linha de comando e API local.

## English

Python project for file automation with two usage modes: command line and local API.

## Por que esse projeto é bom para currículo

- Mostra automação prática com Python.
- Tem CLI para uso local.
- Tem API HTTP simples para integração com outros sistemas.
- Resolve tarefas reais: organizar pastas, backup e renomeação.

## Funcionalidades

- Organizar arquivos por tipo
- Criar backup de pastas
- Renomear arquivos em lote
- API local com endpoints de simulação
- Estrutura simples e fácil de evoluir

## Rodar CLI

```bash
python main.py organize "C:/Users/SeuUsuario/Downloads"
python main.py backup "C:/Projetos" "D:/Backup"
python main.py rename "C:/Imagens" fotos
```

## Rodar API

```bash
python api.py
```

Depois acesse:

```txt
http://localhost:8000/health
```

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/health` | Status da API |
| POST | `/plan/organize` | Simula plano de organização de arquivos |
| POST | `/plan/rename` | Simula plano de renomeação |

## Roadmap

- [ ] Adicionar FastAPI
- [ ] Adicionar testes com pytest
- [ ] Criar Dockerfile
- [ ] Adicionar GitHub Actions
