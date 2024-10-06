from flask import Flask, jsonify, Response
import random
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/random-numbers', methods=['GET'])
def get_random_numbers():
    # Generate 10 random numbers
    random_numbers = random.sample(range(1, 101), 10)
    
    # Create a bar chart using matplotlib
    plt.figure(figsize=(8, 6))
    plt.bar(range(1, 11), random_numbers, color='skyblue')
    plt.xlabel('Index')
    plt.ylabel('Random Number')
    plt.title('Random Numbers Bar Chart')
    
    # Save the plot to a bytes buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # Return the image as a response
    return Response(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5122)
