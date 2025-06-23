from flask import Flask, request, jsonify
from text_controller import summarize_using_llama 
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Flask app
app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract language, summary type, and texts from the request
        language = data.get("languages", "EN")
        summary_type = data.get("summary", "one_by_one")
        texts = data.get("texts")

        if not texts or not isinstance(texts, list):
            return jsonify({"error": "'texts' must be a non-empty list"}), 400

        # Summarize the texts
        summaries = []
        for text in texts:
            summary = summarize_using_llama(text)  
            summaries.append({
                "original_text": text,
                "summary": summary
            })

        # Return the summarized response in JSON format
        return jsonify({
            "languages": language,
            "summary": summary_type,
            "results": summaries
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app on localhost
if __name__ == '__main__':
    app.run(debug=True)
