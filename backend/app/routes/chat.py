from flask import Blueprint, request, jsonify
from ..services.chat_service import ChatService

# Change the blueprint registration without url_prefix
chat_bp = Blueprint('chat', __name__)

# Add this route explicitly
@chat_bp.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        if not data or 'message' not in data:
            return jsonify({"error": "No message provided"}), 400

        chat_service = ChatService()
        response = chat_service.get_completion(
            message=data['message'],
            conversation_history=data.get('history', [])
        )

        return jsonify({"content": response})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500