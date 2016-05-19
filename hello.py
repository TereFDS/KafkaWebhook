from flask import Flask
from flask import request
from flask import Response
from flask import abort

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/facebook/93', methods=['GET', 'POST'])
def facebook_data():
  if request.method == 'GET':
  	if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.verify_token') == 'token':
  	  resp = Response(request.args.get('hub.challenge'), status=200)
  	  with open("test.txt", "a") as myfile:
  		myfile.write('get_facebook_93'+'\n')
  	else:
  	  abort(400)
  	return resp
  elif request.method == 'POST':
  	with open("test.txt", "a") as myfile:
  		myfile.write('post_facebook_93'+'\n')
  		myfile.write(str(request.get_data())+'\n')
  	return '200'
 


if __name__ == '__main__':
  app.debug = True
  app.run()
