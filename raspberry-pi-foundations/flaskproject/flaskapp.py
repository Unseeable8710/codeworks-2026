from flask import Flask, render_template, request
from gpiozero import LED

app = Flask(__name__)

led1 = LED(4)
led2 = LED(27)
led3 = LED(22)
led4 = LED(4)
led5 = LED(23)
led6 = LED(25)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    led = request.form.get('led')
    action = request.form.get('action')

    if led == '1':
        target = led1
    elif led == '2':
        target = led2
    elif led == '3':
        target = led3
    else:
        return "Invalid LED"

    if action == 'on':
        target.on()
    elif action == 'off':
        target.off()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
