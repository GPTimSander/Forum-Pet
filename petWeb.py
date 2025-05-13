import sys
import os
sys.path.append(os.path.dirname(__file__))
from flask import Flask, render_template, request, redirect
from services.message_service import save_message, get_all_messages

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["complaint"]
        save_message(text)
        return redirect("/")
    #python petWeb.py
    messages = get_all_messages()
    return render_template("index.html", messages=messages)

@app.route("/delete/<int:message_id>", methods=["POST"])
def delete(message_id):
    from services.message_service import delete_message
    delete_message(message_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port = 5000)


