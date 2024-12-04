from flask import Flask, request, render_template
import os


api= Flask(__name__)

@api.route('/',methods=['GET'])
def index():
    return render_template('sendfile.html',answer = "ciao")


@api.route('/mansendfile', methods=['POST'])
def ricevidati():
    sDomanda = request.form.get("question")
    image = request.files.get("image")
    if image :
        image.save("./pippo,jpg")
    lunghezza = len(image)
    mio_answer = "ciao a tutti, MA PER ORA NON RISPONDO alla domanda " + sDomanda + "con file " + str(lunghezza)
    return render_template('send.html',answer=mio_answer)


api.run(host="0.0.0", port=8080) 

