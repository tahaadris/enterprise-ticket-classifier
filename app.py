from flask import Flask, request, jsonify
from chains import extract_ticket_data

app = Flask(__name__)

@app.route('/api/resolve', methods=['POST'])
def resolve_ticket():
    """
    Endpoint to process the final conversation and generate a structured JSON ticket.
    Expects a JSON payload: {"chat_history": "User: ... \\nAgent: ..."}
    """
    try:
        data = request.get_json()
        
        if not data or "chat_history" not in data:
            return jsonify({"error": "Missing 'chat_history' in payload."}), 400
            
        chat_history = data["chat_history"]
        
        # Invoke the LangChain pipeline to extract the structured data
        structured_ticket = extract_ticket_data(chat_history)
        
        return jsonify({
            "status": "success",
            "ticket": structured_ticket
        }), 200
        
    except Exception as e:
        # Catch extraction errors or LLM API failures
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask server locally
    app.run(debug=True, host='0.0.0.0', port=5000)
