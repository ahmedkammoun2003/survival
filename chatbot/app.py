from flask import Flask, request, render_template, jsonify
from chatbot import respond_to_question
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_answer', methods=['POST'])
def get_answer_route():
    data = request.get_json()
    question = data.get('question')
    answer = respond_to_question(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True,port=3000)
