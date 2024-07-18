from flask import Flask, request, jsonify, render_template
import os
import sys

##Add the AI_service path in backend for AI integration
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI_Service')))



##Importing AI logic 
from gemini_response import get_gemini_response, reset_chat_session


##Creating flask app instance
app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')


##Frontend integration
@app.route('/')
def home():
    return render_template('index.html')

##This part is request handling by python and sending the message to chat display by javascript
@app.route('/generate-response', methods=['POST'])
def generate_response():
    data = request.get_json()
    user_message = data.get('message')
    language = data.get('language')
    print(language)
    print("User said:",user_message)
    bot_response = get_gemini_response(user_message,language)  ##AI logic usage
    print("Bot said:",bot_response)
    return jsonify({'bot_response': bot_response})   ##Returning bot respone to chat (frontend)

reset_chat_session()
##Running the flask app
if __name__ == '__main__':
    app.run(debug=True)