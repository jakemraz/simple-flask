from flask import Flask
import sys

app = Flask(__name__) 
signiture = 0

@app.route("/", methods=['GET', 'POST']) 
def main():
	ans = f'hello flask {signiture}'
	return ans

if __name__ == "__main__": 
	port = int(sys.argv[1])
	signiture = sys.argv[2]
	
	app.run(debug=True, host="0.0.0.0", port=port)
