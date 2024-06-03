from flask import *
from uuid import uuid4
import os

app = Flask(__name__)
cache_id = uuid4()

@app.route("/", strict_slashes=False)
def index():
    return render_template("index.html", cache_id=cache_id)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
