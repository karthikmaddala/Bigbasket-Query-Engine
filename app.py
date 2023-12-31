from flask import Flask, request, jsonify, render_template
from query_engine import QueryEngine
import os

app = Flask(__name__)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', ' ')
engine = QueryEngine(OPENAI_API_KEY)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        product_info = engine.query(question)
        gpt_response = engine.get_gpt_response(question, product_info.to_json())
        return jsonify({"answer": gpt_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

