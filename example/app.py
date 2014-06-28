from flask import Flask
from paginate_wrapper import paginate
app = Flask()


@app.route("/")
def index():
    return "AAA"

if __name__ == '__main__':
    app.run(debug=True)


