from flask import Flask, request, render_template
import os


api= Flask(__name__)

@api.route('/',methods=['GET'])
def index():
    return render_template('sendfile.html')


api.run(host="0.0.0", port=8080) 

