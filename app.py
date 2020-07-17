from flask import Flask, render_template, abort, request, redirect
from flask.helpers import url_for

app = Flask(__name__)

products = [
    {
        "id":1,
        "description":"Playstation 4",
        "price":18000.00,
        "imageUrl":'ps4.jpeg'

    },
    {
        "id":2,
        "description":"Xbox One Controller",
        "price":2800.00,
        "imageUrl":'xbox.jpeg'


    },
    {
        "id":3,
        "description":"God of War Ps4",
        "price":2350.00,
        "imageUrl":'gow.jpeg'

    }
]

filteredProducts = products

@app.route("/")
def home():
    return render_template("home.html",products = filteredProducts, pageTitle="Game Store")

@app.route("/product/<int:id>")
def getProductById(id):
    global products
    for product in products:
        if (product["id"] == id):
            return render_template("productdetail.html", product = product)
    return abort(404)

@app.route("/findProducts", methods=['POST'])
def findProducts():
    global filteredProducts
    filteredProducts = []
    dato = request.form["filtertext"]
    for p in products:
        if (p["description"] == dato):
        # if (p["description"].startswith(dato)):
            filteredProducts.append(p)
    return redirect("/")


@app.route("/form/", methods=["GET","POST"], defaults={"id":0})
@app.route("/form/<int:id>", methods=["GET","POST"])
def createOrEditProduct(id):
    if id == 0:
        return render_template("productForm.html", product={"id":len(products)+1})
    else:
        try:
            return render_template("productForm.html",product =filteredProducts[id -1])
        except:
            return abort(404)


if __name__ == "__main__":
    app.run(debug=True)