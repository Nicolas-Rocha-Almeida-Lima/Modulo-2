from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return '''<h1>---------------------------------------------Bem-vindo à página inicial--------------------------------------------</h1>
    <p>Esta é a página inicial do nosso site</p>
    <ul>
        <li>Aqui temos uma imagem da sala de aula </li>
        <a href='http://127.0.0.1:5000/sobre'>Sobre a página</a>
        <li>Aqui temos imagem da sala de aula </li>
        <a href='http://127.0.0.1:5000/imagem'>Imagem da sala de aula</a>
    </ul>
    <style>
        li {
            text-size: 40px;
            color: black;}
        a {
            color: blue;
            text-size: 30px;}
    </style>
    '''
@app.route("/sobre")
def sobre():
    return '''<h1>----------------------------------------------Bem-vindo à página sobre---------------------------------------------</h1>
    <p>Esta é a página foi criada para testar o funcionamento do Flask, e testa caminhos tipo o /sobre</p>
    <style>
        body {
            background-color: white;}
        h1 {
        color: black;
        text-align: center;
        font-family: Arial, sans-serif;}
        p {
        color: black;
        size: 30px;
        font-family: Arial, sans-serif;}
    </style>'''
@app.route("/imagem")
def imagem():
    return '''<h1>----------------------------------------------Bem-vindo à página da imagem---------------------------------------------</h1>
    <p>Esta é a página foi criada para testar o funcionamento do Flask, e testa caminhos tipo o /imagem</p>
    <img src=oi.png width="500" height="300">
    <h2>Se a imagem não aparecer, e porque a imagem não esta rederizando</h2>
    <style>
        body {
            background-color: white;}
        h1 {
        color: black;
        text-align: center;
        font-family: Arial, sans-serif;}
        p {
        color: black;
        size: 30px;
        font-family: Arial, sans-serif;}
    </style>'''
app.run(debug=True)