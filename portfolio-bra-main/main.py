# Importar
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

def txt(infor):
    with open('feedback.txt', 'a') as f:
        f.write(infor + '\n')

# Conteúdo da página
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades Dinâmicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    form = str(request.form.get('feedback__form'))
    txt(form)
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db, form=form)
    


if __name__ == "__main__":
    app.run(debug=True)
