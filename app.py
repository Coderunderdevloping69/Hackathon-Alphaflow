from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import stock_engine

app = Flask(__name__)
CORS(app)

# --- PAGES ---
@app.route('/')
def home(): return render_template('index.html')

@app.route('/learn')
def learn(): return render_template('learn.html')

@app.route('/dashboard')
def dashboard(): return render_template('dashboard.html')

# --- APIs ---
@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    ticker = data.get('ticker', 'TCS')
    result = stock_engine.analyze_ticker(ticker)
    return jsonify(result) if result else (jsonify({"error": "Ticker not found"}), 404)

@app.route('/api/market_status', methods=['GET'])
def market_status():
    result = stock_engine.analyze_ticker('^NSEI')
    if result: result['ticker'] = "NIFTY 50"
    return jsonify(result) if result else (jsonify({"error": "Error"}), 500)

@app.route('/api/chat', methods=['POST'])
def chat():
    return jsonify({"response": stock_engine.get_chat_response(request.json.get('message', ''))})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
