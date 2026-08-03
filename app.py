from flask import Flask, render_template, request, jsonify
from chatbot import get_response


app = Flask(__name__)



@app.route("/")
def index():

    return render_template("index.html")



@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()


    message = data.get("message")


    if message:

        reply = get_response(message)


        return jsonify({

            "response":reply

        })


    return jsonify({

        "response":
        "Please enter a message."

    })



if __name__ == "__main__":

    app.run(debug=True)