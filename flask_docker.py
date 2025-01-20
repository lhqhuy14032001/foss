from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello world, Hello CI/CD using Jenkins by LHQH-M3724006"

if __name__ == '__main__':
	app.run(debug="True", host="0.0.0.0")
