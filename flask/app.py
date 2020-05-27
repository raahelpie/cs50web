from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
	return "Ud kar char kar swedh bawan ko ooo..."