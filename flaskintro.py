# flaskintro.py
#
# Lektionspass 2 (timme 2), tisdag 08-april-2025
#
# Robin startade dagen med att koda biblioteket Tkinter
# Detta är hänvisning till biblioteket Flask
#
# Dagens föreläsning blev följande fyra filer
#       ./part1.py          # 1a timmen, med bas i Tkinter
#       ./demo.py           # 1a timmen, med bas i Tkinter
#       ./flaskintro.py             # 2a timmen, med bas i Flask
#       ./templates/index.html      # 2a timmen, med bas i Flask
#  
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    #return "<h1> Hello world! </h1>"
    return render_template('index.html')


@app.route('/contact')
def contact():
    return "<h1> Kontakta oss!!!! </h1>"


@app.route('/about')
def about():
    #return "<h1> Detta är \"about page\", här hittas info om... om... !!!! </h1>"
    return render_template('about.html')


@app.route('/mitt_foto')
def mitt_foto():
    return render_template('mitt_foto.html')



if __name__ == '__main__':
    app.run(debug=True)



