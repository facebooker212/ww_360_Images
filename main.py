from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/car1/image_<int:image_number>.png')
def serve_car1(image_number):
    return send_from_directory('./car1', f'image_{image_number}.png')

@app.route('/car2/image_<int:image_number>.png')
def serve_car2(image_number):
    return send_from_directory('./car2', f'image_{image_number}.png')

@app.route('/car3/image_<int:image_number>.png')
def serve_car3(image_number):
    return send_from_directory('./car3', f'image_{image_number}.png')

if __name__ == '__main__':
    app.run(port=8001)
