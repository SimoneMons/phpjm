from flask import Flask
from board import pages
import test

app = Flask(__name__)
app.register_blueprint(pages.bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)