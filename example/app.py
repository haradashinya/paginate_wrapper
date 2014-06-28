from flask import Flask,render_template,request
from paginate_wrapper import paginate
app = Flask(__name__)

# Each page has 10 items.
PER_PAGE = 10

@app.route('/')
def index():
    _page = request.args.get("page",1)
    page = int(_page)
    all_items = ['item-'+str(item) for item in range(1,1000)]
    items = all_items[PER_PAGE * (page- 1):PER_PAGE * page]

    obj = paginate(offset=7,
                   objects=all_items,
                   page = page,
                   per_page = PER_PAGE)

    return render_template('index.html',
                           items = items,
                           obj =obj
                           )

if __name__ == '__main__':
    app.run(debug=True)


