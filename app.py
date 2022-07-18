import requests
import numpy as np
from flask import Flask, render_template, jsonify, send_file, request, redirect, url_for,  Response, session
from flask_restful import Api, Resource, reqparse
import os
import time
import json
import glob
import sqlite3
import json
import requests
import cv2
from range_key_dict import RangeKeyDict
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

app = Flask(__name__)
api = Api(app)
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
basedir = os.path.abspath(os.path.dirname(__file__))



@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = '0'
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/board')
def board():
	return render_template('board.html')



@app.route('/survey')
def survey():
    if request.args.get("filename") is None:
        filename=  "https://play-lh.googleusercontent.com/aFWiT2lTa9CYBpyPjfgfNHd0r5puwKRGj2rHpdPTNrz2N9LXgN_MbLjePd1OTc0E8Rl1"
        conid = None
    else:
        filename= request.args['filename']
        conid = "myModal"
    return render_template('survey.html', filename= filename, conid=conid, job=filename[:-4])
    

class calculateScore(Resource):
        def get(self):
                return {"debug": "the resource is working with get method"}
        def post(self):
                parse = reqparse.RequestParser()
                parse.add_argument('Question1-1', type=str)
                parse.add_argument('Question1-2', type=str)
                parse.add_argument('Question1-3', type=str)

                parse.add_argument('Question2-1', type=str)
                parse.add_argument('Question2-2', type=str)
                parse.add_argument('Question2-3', type=str)
                
                parse.add_argument('Question3-1', type=str)
                parse.add_argument('Question3-2', type=str)
                parse.add_argument('Question3-3', type=str)
                
                parse.add_argument('Question4-1', type=str)
                parse.add_argument('Question4-2', type=str)
                parse.add_argument('Question4-3', type=str)
                
                parse.add_argument('Question5-1', type=str)
                parse.add_argument('Question5-2', type=str)
                parse.add_argument('Question5-3', type=str)
                
               




                args = parse.parse_args()
        
                a = [args['Question1-1'],args['Question2-1'],args['Question3-1'],args['Question4-1'],args['Question5-1']]
                
                a = [int(x) for x in a]
                b = [args['Question1-2'],args['Question2-2'],args['Question3-2'],args['Question4-2'],args['Question5-2']]
                             
                b = [int(x) for x in b]
                c = [args['Question1-3'],args['Question2-3'],args['Question3-3'],args['Question4-3'],args['Question5-3']]
                               
                c = [int(x) for x in c]

                suma = sum(a)
                sumb = sum(b)
                sumc = sum(c)
              
                dic = {'a': suma,'b': sumb, 'c':sumc}
                chosen = max(dic, key=dic.get)
                field = {'a':'energy','b':'material','c':'emissions'}
                degree = RangeKeyDict({
                        (5,11): 'Detective',
                        (11,16): 'Scientist',
                        (16,21): 'Hero',
                    })
                
                
                print(field[chosen]+' '+degree[dic[chosen]])
                
                
                return redirect(url_for(".survey", filename=field[chosen]+degree[dic[chosen]]+".JPG"))
                

class getimage(Resource):
	def get(self):
                return {"debug": "the resource is working with get method"}
	def post(self):

		d={
  			"type": "get_image",

			}
		string_dictionary = json.dumps(d)
		list = requests.get(f'https://mz9hzt4ia5.execute-api.us-east-2.amazonaws.com/norhanWebsite?event='+string_dictionary).json()
		image=np.reshape(np.array(list['image']),list['shape'])
		cv2.imwrite('static/image_path.jpg',image)
		print(os.listdir())
		print(list["shape"])


		
		

class sendm(Resource):
	def get(self):
                return {"debug": "the resource is working with get method"}
	def post(self):
		parse = reqparse.RequestParser()
		parse.add_argument('Popup1-1', type=str)
		args = parse.parse_args()
		print(args["Popup1-1"])
		d={"type":"update_user","name":args["Popup1-1"]}
		print(d)
		string_dictionary = json.dumps(d)
		list = requests.get(f'https://mz9hzt4ia5.execute-api.us-east-2.amazonaws.com/norhanWebsite?event='+string_dictionary).json()
		return redirect(url_for(".survey"))


def call_five():
	url = "http://ec2-3-90-162-76.compute-1.amazonaws.com:8080/getimage"

	payload = json.dumps({})
	headers = {
  	'Content-Type': 'application/json'
	}

	response = requests.request("POST", url, headers=headers, data=payload)


scheduler = BackgroundScheduler()
scheduler.add_job(func=call_five, trigger="interval", seconds=5)
scheduler.start()


api.add_resource(sendm, "/sendm")
api.add_resource(getimage, "/getimage")
api.add_resource(calculateScore, "/calculateScore")
if __name__ == "__main__":
        app.secret_key = 'super secret key'
        app.run(host='0.0.0.0', port=8080)
        #app.run(debug=True)
        atexit.register(lambda: scheduler.shutdown())
