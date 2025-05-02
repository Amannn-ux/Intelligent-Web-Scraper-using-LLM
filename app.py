import os
from flask import Flask, request, render_template, jsonify
from scraper import scrape_website
from llm_processor import process_text

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    raw_content = scrape_website(url)
    processed_content = process_text(raw_content)

    return jsonify({'raw': raw_content, 'processed': processed_content})

if __name__ == '__main__':
    app.run(debug=True)
