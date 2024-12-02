from flask import Flask

app= Flask(__name__)
from views import *

app.config['SECRET_KEY'] = 'ITALO'

if __name__ == "__main__":
    app.run(debug=True)
    