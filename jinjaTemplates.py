from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from model import db, saveDB

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html",
           cards = db
    )

@app.route("/card/<int:index>")
def cardView(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)


@app.route("/add_card/", methods=["GET", "POST"])
def addCard():
    if request.method == "POST":
        # form has been submitted process data
        card = {"question":request.form['question'], "answer":request.form["answer"]}
        db.append(card)
        saveDB()
        return redirect(url_for("cardView", index=len(db)-1))

    else:
        return render_template('addCard.html')


@app.route("/remove_card/<int:index>", methods=["GET", "POST"])
def removeCard(index):
    try:
        if request.method == "POST":
            del db[index]
            saveDB()
            return redirect( url_for("welcome"))
        else:
            return render_template('removeCard.html', card=db[index])
    except IndexError:
        abort(404)

@app.route("/api/card/")
def apiCardList():
    return jsonify(db)


@app.route("/api/card/<int:index>")
def apiCardDetail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)