#!/usr/bin/env python3
"""
This is the main file of the flask application.
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    This is the main page of the flask application.

    Returns:
        str: The rendered template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
