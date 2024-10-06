from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/random-numbers', methods=['GET'])
def get_random_numbers():
    # Generate 10 random numbers
    random_numbers = random.sample(range(1, 101), 10)  # Numbers between 1 and 100
    return jsonify(random_numbers)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5123)

