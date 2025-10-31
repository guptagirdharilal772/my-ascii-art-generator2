from flask import Flask, render_template, request
from pyfiglet import Figlet

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
#def index():
    ascii_art = None
    if request.method == 'POST':
        text = request.form.get('text')
        font = request.form.get('font')
        if text and font:
            figlet = Figlet(font=font)
            ascii_art = figlet.renderText(text)
    #return render_template('index.html', ascii_art=ascii_art)

if __name__ == '__main__':
    app.run(debug=True)
