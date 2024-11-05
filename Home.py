from flask import Flask, render_template, jsonify
import requests
import json  # Add this import for JSON dumping


@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/page2')
def Page2():
    return render_template('Page 2.html')
    

        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
