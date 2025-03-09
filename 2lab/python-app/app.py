from flask import Flask, jsonify
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)

app = Flask(__name__)

# Отключаем стандартное логирование Flask
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Главная страница
@app.route('/')
def home():
    return jsonify(message="Welcome to the Colorful Flask API!", status="OK")

# Маршрут /api/hello
@app.route('/api/hello', methods=['GET'])
def hello():
    print(Fore.GREEN + "Someone accessed the /api/hello endpoint!")
    return jsonify(message="Hello, World! This is a colorful Flask API.", status="OK")

# Маршрут /api/colors
@app.route('/api/colors', methods=['GET'])
def colors():
    color_list = ["Red", "Green", "Blue", "Yellow", "Magenta", "Cyan"]
    print(Fore.BLUE + "Someone accessed the /api/colors endpoint!")
    return jsonify(colors=color_list, status="OK")

# Маршрут /api/quote
@app.route('/api/quote', methods=['GET'])
def quote():
    quotes = [
        "Vanyarina",
        "Vanyarina Julia",
        "Vanyarina Julia student",
        "Vanyarina Julia student of MCU"
    ]
    import random
    selected_quote = random.choice(quotes)
    print(Fore.MAGENTA + f"Someone accessed the /api/quote endpoint! Quote: {selected_quote}")
    return jsonify(quote=selected_quote, status="OK")

if __name__ == '__main__':
    print(Fore.YELLOW + "Starting the Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=False)