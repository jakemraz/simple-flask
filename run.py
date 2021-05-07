from flask import Flask
import sys
import uuid

app = Flask(__name__) 

id = str(uuid.uuid4())
@app.route("/", methods=['GET', 'POST']) 
def main():
	ans = f'hello flask {id}'
	return ans

if __name__ == "__main__": 
	app.run(debug=True, host="0.0.0.0", port=80)
