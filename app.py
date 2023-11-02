import os
from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
#api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = "CHANGE_ME" #your API key here

@app.route('/')
def chat():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask_gpt3():
    user_message = request.form['user_message']

    # You can customize the prompt or conversation as needed.
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message},
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            max_tokens=100,
        )

        assistant_response = response['choices'][0]['message']['content']

        return jsonify({"assistant_response": assistant_response})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
