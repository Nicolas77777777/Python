from flask import Flask, request, render_template
import os


api= Flask(__name__)

@api.route('/',methods=['GET'])
def index():
    return render_template('sendfile.html',answer = "ciao")


@api.route('/mansendfile',methods=['POST'])
def ricevidati():
    sDomanda= request.form.get("question")
    mio_answer = " ciao a tutti, ma per ora non risposno alla domanda " + sDomanda
    return render_template('sendfile.html',answer = mio_answer)


api.run(host="0.0.0", port=8080) 

