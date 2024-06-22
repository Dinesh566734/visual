from flask import Flask
app=Flask(__name__)
@app.route("/")
@app.route("/base")
def base():
    return "hello world"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)