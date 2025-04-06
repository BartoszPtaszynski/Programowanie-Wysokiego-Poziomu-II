from flask import Flask, jsonify, abort

app = Flask(__name__)

users = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30}
}

@app.route('/')
def home():
    return "Witaj na naszej stronie! Możesz sprawdzić listę użytkowników, odwiedzić stronę 'O nas', lub sprawdzić profil konkretnego użytkownika."

@app.route('/about')
def about():
    return "Jesteśmy grupą od tworzenia aplikacji webowych."

@app.route('/users')
def user_list():
    user_names = [user["name"] for user in users.values()]
    return "Lista użytkowników: " + ", ".join(user_names)

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    user = users.get(user_id)
    if user:
        return f"Profil użytkownika: {user['name']}, {user['age']} lat"
    else:
        return "Użytkownik nie istnieje"

if __name__ == '__main__':
    app.run(debug=True)
