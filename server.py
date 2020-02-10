from flask import Flask, redirect, render_template, request, url_for 

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == "GET":
		return '<h1>DSC RIT recruitment process</h1>'

@app.route("/web", methods=['GET', 'POST'])
def web1():
	if request.method == "GET":
		return render_template("web.html")
	elif request.method == "POST":
		print(request.form['usn'])
		print(request.form['metod7']+"\n"+request.form['metod1']+"\n"+request.form['metod2']+"\n"+request.form['metod3']+"\n"+request.form['metod4']+"\n"+request.form['metod5']+"\n"+request.form['metod6'])
		f = open("results.txt", "a")
		f.write(request.form['usn']+"\t"+"8.0")
		f.close()

		return render_template("web.html")

@app.route("/ml", methods=['GET', 'POST'])
def ml1():
	if request.method == "GET":
		return render_template("ml.html")
	elif request.method == "POST":
		print(request)
		return render_template("ml.html")

@app.route("/mobile", methods=['GET', 'POST'])
def mobile1():
	if request.method == "GET":
		return render_template("mobile.html")
	elif request.method == "POST":
		print(request)
		return render_template("mobile.html")


if __name__ == '__main__':
	app.run(debug=True,host= '0.0.0.0')
