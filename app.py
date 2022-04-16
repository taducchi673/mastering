# from django.template import Engine
from flask import Flask, Response, redirect, render_template, render_template_string, url_for, request
from config import DevConfig
from wtforms import IntegerField, RadioField, SubmitField, Form, StringField, SubmitField;
from flask_wtf import Form
from sqlalchemy import create_engine, MetaData, Table, Column, Text, insert
import pandas as pd
import cv2 as cv
import cv2
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'
app.config.from_object(DevConfig)

engine = create_engine('sqlite:///questions.db')
connection = engine.connect()
metadata = MetaData()
test1 = Table('question', metadata, 
    Column('question', Text),
    Column('a', Text),
    Column('b', Text),
    Column('c', Text),
    Column('d', Text),
)

metadata.create_all(engine) 
 
test = pd.read_sql_table('question', connection)
class Answer(Form):
    ques1 = RadioField(label = test['question'][1], choices = (test['a'][1], test['b'][1], test['c'][1], test['d'][1]))

class CTForm(Form):
    question = StringField(label = "question")
    a = StringField(label = "a")
    b = StringField(label = "b")
    c = StringField(label = "c")
    d = StringField(label = "d")
    submit = SubmitField(label ="submit")


camera = cv2.VideoCapture(0)  # use 0 for web camera
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera
# for local webcam use cv2.VideoCapture(0)

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/test", methods=['GET', 'POST'])
def test():
    form = Answer()
    return render_template('test.html', form = form)


posts = [
    {
        'author': 'ABC',
        'title': 'Blog 1',
        'content': 'First post content',
        'date_posted': 'Today'
    },
        {
        'author': 'Chi Ta Duc',
        'tit/le': 'Blog 2',
        'content': 'Second post content',
        'date_posted': 'Last night'
    }
]


@app.route('/admin')
def hello_admin():
    return "Hello admin Ta Duc Chi"

@app.route("/")
def home():
    return render_template('index.html', posts = posts)


@app.route('/about_me')
def about():
    return render_template('about.html')

@app.route('/ml')
def ml():
    return render_template('ML.html')

@app.route('/contact_me')
def contact():
    return render_template('contact_me.html')

@app.route('/about/<name>')
def hello(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    return f'<h1>Hello {name}<h1>'

@app.route('/create_test', methods = ['GET','POST'])
def create_test():
    form = CTForm()
    if request.method == 'POST':
        question = request.form['question']
        a = request.form['a'] 
        b = request.form['b']
        c = request.form['c']
        d = request.form['d']
        engine = create_engine('sqlite:///questions.db')
        connection = engine.connect()   
        stmt  = insert(test1).values(question = question , a = a, b=b, c=c, d=d)
        connection.execute(stmt)
    return render_template('create_test.html', form = form)


if __name__ == "__app__":
    app.run(debug = True)