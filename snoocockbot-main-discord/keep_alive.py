# I don't really know where this is from. But I use it because I'm broke and use repl.it

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return 'Cocks are being dispensed' # Feel free to change to something like 'Cocks are being dispensed' or something, no one will see it.

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
