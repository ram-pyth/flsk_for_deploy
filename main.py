from flask import Flask

app = Flask(__name__)

# homepage maršrutas
@app.route("/")
def homepage():
    return "Hello world!!!Čia mano Flask webappsas"

# įsivaizduojamo naujienų skyriaus maršrutas
@app.route("/news")
def news():
    return "<h1>Čia yra NAUJAS naujienų skyrius</h1>"

# gaunam iš browserio skaičiuką į web app maršruto dalį
@app.route("/news/<int:item_nr>")
def news_item(item_nr):
    return f"Jūs pasirinkote naujienų itemą {item_nr}"

# gaunam iš browserio bet kokią maršruto dalį po homepage
@app.route("/<text>")
def any_route(text):
    return f"Jūs bandote patekti adresu /{text} kuriame nieko nėra"

if __name__ == '__main__':
    app.run(port=5001)
