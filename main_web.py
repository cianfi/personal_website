from flask import Flask, request, render_template
from flask_restful import Resource, Api
import scripts
import datetime
from functools import wraps

app = Flask(__name__)
# api = Api(app)

# class api_test(Resource):
#     def get(self) -> dict:
#         return {"TEST": "TEST"}
# api.add_resource(api_test, '/test/')

# @app.route("/add", methods=["GET", "POST"])
# def add():
#     if request.method == "POST":
#         num1 = request.form.get("num1")
#         num2 = request.form.get("num2")
#         result = scripts.add(num1, num2)
#         return result
#     return render_template("add.html")

# @app.route("/user", methods=["GET", "POST"])
# def user():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         result = scripts.user(username, password)
#         return result
#     return render_template("user.html")


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port="80")
    app.run(debug="True")