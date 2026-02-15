#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_tg = request.form.get('button_tg')
    button_GitHub = request.form.get('button_GitHub')
    button_gunslol = request.form.get('button_gunslol')
    return render_template('index.html', button_python=button_python,button_tg=button_tg,button_GitHub=button_GitHub,button_gunslol=button_gunslol)


if __name__ == "__main__":
    app.run(debug=True)