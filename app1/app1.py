from flask import Flask, jsonify
import tensorflow as tf

app = Flask(__name__)

@app.route('/api1')
def api1():
    # Check if GPU is available
    gpu_available = tf.config.list_physical_devices('GPU')

    # Create a random tensor
    tensor = tf.random.uniform([3, 3])

    # Run the tensor on GPU if available
    if gpu_available:
        tensor = tensor.gpu()

    return jsonify({
        'gpu_available': bool(gpu_available),
        'tensor': tensor.numpy().tolist()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
