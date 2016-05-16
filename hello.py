from flask import Flask
from flask import request
from flask import Response
from flask import abort

app = Flask(__name__)
updates = ['1','2','3']

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/facebook/93', methods=['GET', 'POST'])
def facebook_data():
  if request.method == 'GET':
  	if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.verify_token') == 'token':
  	  resp = Response(request.args.get('hub.challenge'), status=200)
  	else:
  	  abort(400)
  	return resp
  elif request.method == 'POST':
  	updates= updates + request.get_data()
  	with open("test.txt", "a") as myfile:
  		myfile.write(str(request.get_data())+'\n')
  	return 200

@app.route('/facebook/list', methods=['GET'])
def facebook_list():
  #str1 = " ".join(str(x) for x in updates)
  str1 = " "
  with open("test.txt", "a") as myfile:  
    for ups in updates:
  	  myfile.write(str(ups)+'\n')
  return str1
 


if __name__ == '__main__':
  app.debug = True
  app.run()
