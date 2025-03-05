# **Previsão do Tempo - Flask App**

Este é um aplicativo web simples desenvolvido em Flask para exibir a previsão do tempo de uma cidade informada pelo usuário. Ele consome a API do OpenWeatherMap e exibe informações sobre temperatura, condição climática e ícone correspondente.

## Tecnologias Utilizadas

- **Flask** - Framework web para Python
- **Bootstrap** - Para estilização e responsividade
- **API OpenWeatherMap** - Fonte de dados meteorológicos

## Como Executar o Projeto

### 1. Clonar o Repositório

```bash
    git clone https://github.com/DanDosSantos/clima-tempo.git
    cd clima-tempo
```

### 2. Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)

```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
```

### 3. Instalar as Dependências

```bash
    pip install -r requirements.txt
```

### 4. Configurar a API Key do OpenWeatherMap

Substitua `SEU_API_KEY` pela sua chave da API no arquivo `app.py`:

```python
    api_key = 'SEU_API_KEY'
```

### 5. Executar o Servidor Flask

```bash
    python app.py
```

Acesse `http://127.0.0.1:5425/` no navegador.

## Como Usar

1. Digite o nome da cidade no campo de pesquisa.
2. Clique no botão para buscar a previsão.
3. Veja a temperatura, condição climática e um ícone representando o clima.
4. Se uma cidade inválida for inserida ou o campo estiver vazio, uma mensagem de erro será exibida.

## Estrutura do Projeto

```
/
|-- /static/images/          # Pasta para imagens (ex: generated.jpg)
|-- /templates/index.html    # Template principal
|-- app.py                   # Código principal do Flask
|-- requirements.txt         # Dependências do projeto
|-- README.md                # Este arquivo
```

---

Feito com ❤️ usando Flask e Bootstrap!
