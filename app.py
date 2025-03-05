import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def escolher_icone(condicao):
    condicao = condicao.lower()  # Converter para minúsculas para evitar erros

    if 'nuvens' in condicao:
        return "fa-cloud-sun"
    elif 'nublado' in condicao:
        return "fa-cloud"
    elif 'chuva' in condicao:
        return "fa-cloud-showers-heavy"
    elif 'neve' in condicao:
        return "fa-snowflake"
    elif 'trovoada' in condicao:
        return "fa-bolt"
    elif 'sol' in condicao or 'limpo' in condicao:
        return "fa-sun"
    else:
        return "fa-question-circle"  # Ícone padrão caso não encontre

@app.route('/', methods=['GET', 'POST'])
def previsao():
    api_key = 'SUA API AQUI'
    city = ''
    error_message = ''

    if request.method == 'POST':
        # Pega o valor do input enviado pelo formulário
        city = request.form['city']
        if city:
            link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt_br&units=metric'
            requisicao = requests.get(link)

            if requisicao.status_code == 200:
                dici = requisicao.json()
            
                cidade = dici['name']
                condicao = dici['weather'][0]['description']
                temperatura = dici['main']['temp']

                condicao_formatada = condicao.capitalize()
                temperatura_formatada = f'{temperatura:.0f}'
                icone = escolher_icone(condicao)  # Obtém o ícone correspondente

                return render_template(
                    'index.html',
                    cidade=cidade,
                    condicao=condicao_formatada,
                    temperatura=temperatura_formatada,
                    city=city,
                    error_message=error_message,
                    icone=icone,
                )
            else:
                error_message = 'Cidade não localizada. Tente novamente.'
        else:
            error_message = 'Por favor, digite o nome de uma cidade.'

    return render_template('index.html', city=city, error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True, port=5425)
