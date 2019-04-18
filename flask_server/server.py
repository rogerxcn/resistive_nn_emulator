from flask import Flask, jsonify, abort, request, make_response, url_for
from flask import render_template, redirect
import json, time, os

app = Flask(__name__)




# ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']



image = [
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.329412,0.725490,0.623529,0.592157,0.235294,0.141176,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.870588,0.996078,0.996078,0.996078,0.996078,0.945098,0.776471,0.776471,0.776471,0.776471,0.776471,0.776471,0.776471,0.776471,0.666667,0.203922,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.262745,0.447059,0.282353,0.447059,0.639216,0.890196,0.996078,0.882353,0.996078,0.996078,0.996078,0.980392,0.898039,0.996078,0.996078,0.549020,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.066667,0.258824,0.054902,0.262745,0.262745,0.262745,0.231373,0.082353,0.925490,0.996078,0.415686,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.325490,0.992157,0.819608,0.070588,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.086275,0.913725,1.000000,0.325490,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.505882,0.996078,0.933333,0.172549,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.231373,0.976471,0.996078,0.243137,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.521569,0.996078,0.733333,0.019608,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.035294,0.803922,0.972549,0.227451,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.494118,0.996078,0.713726,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.294118,0.984314,0.941176,0.223529,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.074510,0.866667,0.996078,0.650980,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.011765,0.796078,0.996078,0.858824,0.137255,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.149020,0.996078,0.996078,0.301961,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.121569,0.878431,0.996078,0.450980,0.003922,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.521569,0.996078,0.996078,0.203922,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.239216,0.949020,0.996078,0.996078,0.203922,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.474510,0.996078,0.996078,0.858824,0.156863,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.474510,0.996078,0.811765,0.070588,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
        0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000
        ]


image_tag = 7
predict_image_tag = 7

@app.route('/get_current_image')
def get_current_image():
  return json.dumps(image)

@app.route('/get_current_image_tag')
def get_current_image_tag():
  return json.dumps(image_tag)

@app.route('/get_predict_image_tag')
def get_predict_image_tag():
  return json.dumps(predict_image_tag)

@app.route('/get_result')
def get_result():
  return json.dumps(image_tag == predict_image_tag)

@app.route('/upload_image', methods=['POST'])
def upload_image():
  img_data = request.form.get("img_data")
  img_data = json.loads(img_data)
  print(img_data)
  return "SUCCESS"

@app.route('/transmit_img_H2D'):
def transmit_image_h2d:
  ser = serial.Serial()
  if ser.isOpen():
    ser.close()
  ser = serial.Serial('/dev/ttyS7', 9600)

  for i in range(0, len(image)):
      ser.write(str(image[i]))
      ser.write(' ')

  ser.write('A')

  mbed_data = ""

  while(1):
      curr = ser.read()
      if (curr == 'F'):
        print(mbed_data)
        break
      mbed_data += curr

  result = ""

  while(1):
      curr = ser.read()
      if (curr == 'F'):
        print(result)
        break
      result += curr



@app.route('/')
def index():
  return render_template('index.html', image_tag=str(image_tag), predict_image_tag=predict_image_tag, result=bool(image_tag == predict_image_tag))



if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
