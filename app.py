# !/usr/bin/env python

'''
websocket
'''

# 使用Flask-Socketio进行WebSocket通信
# https://jiayi.space/post/shi-yong-flask-socketiojin-xing-websockettong-xin



from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)


# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/charts')
def index():
    return render_template('chartshow.html')


@socketio.on('client_event')
def client_msg(msg):
    print('client_msg')

    file = r"api.log"
    with open(file, "r") as f:
        while True:
            socketio.sleep(1)
            for line in f.readlines():
                newline = (line.replace("\n", "").split(","))
                data = []
                data.append(int(newline[0]))
                data.append(float(newline[1]))
                emit('server_response', {'data': data})


@socketio.on('connect_event')
def connected_msg(msg):
    print('connect_event')
    emit('server_response', {'data': msg['data']})



if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0',port=9999)
