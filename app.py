from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
gpt_api_endpoint = "https://your-gpt-api-endpoint.com/complete"  # Replace with your GPT API endpoint

@app.route('/ask', methods=['POST'])
def ask_gpt():
    user_input = request.json['user_input']
    payload = {'prompt': user_input}
    response = requests.post(gpt_api_endpoint, json=payload)
    model_response = response.json()['model_output']
    return jsonify({'model_response': model_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
