from flask import Flask, jsonify, abort, request, make_response, url_for
from flask import render_template, redirect
import json, time, os
import serial


app = Flask(__name__)




# ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']



image = [
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.239216,0.011765,0.164706,0.462745,0.756863,0.462745,0.462745,0.239216,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.054902,0.701961,0.960784,0.925490,0.949020,0.996078,0.996078,0.996078,0.996078,0.960784,0.921569,0.329412,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.592157,0.996078,0.996078,0.996078,0.835294,0.752941,0.698039,0.698039,0.705882,0.996078,0.996078,0.945098,0.180392,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.168627,0.921569,0.996078,0.886275,0.250980,0.109804,0.047059,0.000000,0.000000,0.007843,0.501961,0.988235,1.000000,0.678431,0.066667,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.219608,0.996078,0.992157,0.419608,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.525490,0.980392,0.996078,0.294118,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.247059,0.996078,0.619608,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.866667,0.996078,0.615686,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.760784,0.996078,0.403922,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.588235,0.996078,0.835294,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.133333,0.862745,0.937255,0.227451,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.329412,0.996078,0.835294,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.494118,0.996078,0.670588,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.329412,0.996078,0.835294,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.839216,0.937255,0.235294,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.329412,0.996078,0.835294,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.839216,0.780392,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.329412,0.996078,0.835294,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.043137,0.858824,0.780392,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.329412,0.996078,0.835294,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.384314,0.996078,0.780392,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.635294,0.996078,0.819608,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.384314,0.996078,0.780392,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.200000,0.933333,0.996078,0.294118,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.384314,0.996078,0.780392,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.200000,0.647059,0.996078,0.764706,0.015686,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.258824,0.945098,0.780392,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.011765,0.654902,0.996078,0.890196,0.215686,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.839216,0.835294,0.078431,0.000000,0.000000,0.000000,0.000000,0.000000,0.180392,0.596078,0.792157,0.996078,0.996078,0.247059,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.839216,0.996078,0.800000,0.705882,0.705882,0.705882,0.705882,0.705882,0.921569,0.996078,0.996078,0.917647,0.611765,0.039216,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.317647,0.803922,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.988235,0.917647,0.470588,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.101961,0.823529,0.996078,0.996078,0.996078,0.996078,0.996078,0.600000,0.407843,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,
            0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000
        ]


predict_image_tag = 0
measured_voltage = ['<0 V>', '<0 V>', '<0 V>']
probability = ['<Digit 0: 0 %>', '<Digit 1: 0 %>', '<Digit 2: 0 %>']

@app.route('/get_current_image')
def get_current_image():
  return json.dumps(image)

@app.route('/get_current_image_tag')
def get_current_image_tag():
  return json.dumps(image_tag)

@app.route('/upload_image', methods=['POST'])
def upload_image():
  img_data = request.form.get("img_data")
  img_data = json.loads(img_data)
  for i in range(0, len(image)):
      image[i] = round((img_data[i] - 0.1307) / 0.3081, 6)
      # image[i] = img_data[i]
  print(image)
  return "SUCCESS"

@app.route('/transmit_img_H2D')
def transmit_image_h2d():
  ser = serial.Serial()
  if ser.isOpen():
    ser.close()
  ser = serial.Serial('/dev/ttyS5', 921600)

  for i in range(0, len(image)):
      ser.write(str(round(image[i], 3)).encode())
      ser.write(' '.encode())

  ser.write('A'.encode())

  mbed_data = ""

  while(1):
      curr = ser.read().decode()
      if (curr == 'F'):
        print("Input Image: ")
        print(mbed_data)
        break
      mbed_data += curr

  result = ""

  while(1):
      curr = ser.read().decode()
      if (curr == 'I'):
        print("Result: ")
        print(result)
        break
      result += curr

  prob = ""

  while(1):
      curr = ser.read().decode()
      if (curr == 'P'):
        print("Probability: ")
        print(prob)
        break
      prob += curr

  exec_time_mcu = ""

  while(1):
      curr = ser.read().decode()
      if (curr == 'T'):
        print("Exec Time on MCU: ")
        print(exec_time_mcu + " us")
        break
      exec_time_mcu += curr

  prob_arr = json.loads(prob)
  sum = prob_arr[0] + prob_arr[1] + prob_arr[2]
  prob_arr[0] /= sum
  prob_arr[1] /= sum
  prob_arr[2] /= sum

  result_arr = json.loads(result)

  global measured_voltage
  measured_voltage[0] = '<  ' + str(round(result_arr[0]*3.3, 4))+' V  >'
  measured_voltage[1] = '<  ' + str(round(result_arr[1]*3.3, 4))+' V  >'
  measured_voltage[2] = '<  ' + str(round(result_arr[2]*3.3, 4))+' V  >'

  # print(result_arr)

  global predict_image_tag

  predict_image_tag = result_arr.index(max(result_arr))

  global probability
  probability[0] = '<  Digit 0: ' + str(round(prob_arr[0]*100, 2))+' %  >'
  probability[1] = '<  Digit 1: ' + str(round(prob_arr[1]*100, 2))+' %  >'
  probability[2] = '<  Digit 2: ' + str(round(prob_arr[2]*100, 2))+' %  >'

  # print(predict_image_tag)

  return result + "|" + prob



@app.route('/')
def index():
  return render_template('index.html', predict_image_tag=predict_image_tag, probability=str(probability), measured_voltage=str(measured_voltage))

@app.route('/draw')
def draw():
  return render_template('draw.html')



if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0')
