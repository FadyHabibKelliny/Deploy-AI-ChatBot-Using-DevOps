import os
import logging
from flask import Flask, request, jsonify
from gemini_client import ask_gemini
from database import log_question

# Configure logging
logging.basicConfig(
    level=logging.ERROR,  # Changed from INFO to ERROR
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        #logging.FileHandler("app.log"),  # Keep this for debugging purposes        
        logging.StreamHandler()  # Removed FileHandler to stop writing to ap        p.log
    ]
)

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            logging.warning("Invalid request received: missing 'question' field")
            return jsonify({"error": "Invalid request. 'question' is required."}), 400

        question = data['question']
        logging.info(f"Received question: {question}")
        
        answer = ask_gemini(question)
        log_question(question, answer)
        
        logging.info("Successfully processed question and logged response")
        return jsonify({"answer": answer})

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}", exc_info=True)
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.getenv('PORT', 5000))
    
    # In production, disable debug mode and bind to all interfaces
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
