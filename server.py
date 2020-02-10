from flask import Flask, redirect, render_template, request, url_for 

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == "GET":
		return render_template("index.html")


@app.route("/web", methods=['GET', 'POST'])
def web1():
	if request.method == "GET":
		return render_template("web.html")
	elif request.method == "POST":
		print(request.form['usn'])
		print(request.form['metod1']+"\n"+request.form['metod2']+"\n"+request.form['metod3']+"\n"+request.form['metod4']+"\n"+request.form['metod5']+"\n"+request.form['metod6']+"\n"+request.form['metod7']+"\n"+request.form['metod8']+"\n"+request.form['metod9']+"\n"+request.form['metod10'])
		f = open("resultsweb.txt", "a")
		scr=0
		l1 = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]
		for i in range(0,10):
			if l1[i]==request.form['metod'+str(i+1)]:
				scr=scr+1
		f.write(request.form['usn']+"\t"+str(scr)+"\n")
		f.close()

		return render_template("success.html",score=str(scr),usn=request.form['usn'])

@app.route("/ml", methods=['GET', 'POST'])
def ml1():
	if request.method == "GET":
		return render_template("ml.html")
	elif request.method == "POST":
		print(request.form['usn'])
		print(request.form['metod1'] + "\n" + request.form['metod2'] + "\n" + request.form['metod3'] + "\n" +
			  request.form['metod4'] + "\n" + request.form['metod5'] + "\n" + request.form['metod6'] + "\n" +
			  request.form['metod7'] + "\n" + request.form['metod8'] + "\n" + request.form['metod9'] + "\n" +
			  request.form['metod10'])
		f = open("resultsml.txt", "a")
		scr = 0
		l1 = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]
		for i in range(0, 10):
			if l1[i] == request.form['metod' + str(i + 1)]:
				scr = scr + 1
		f.write(request.form['usn'] + "\t" + str(scr) + "\n")
		f.close()

		return render_template("success.html", score=str(scr), usn=request.form['usn'])

@app.route("/mobile", methods=['GET', 'POST'])
def mobile1():
	if request.method == "GET":
		return render_template("mobile.html")
	elif request.method == "POST":
		print(request.form['usn'])
		print(request.form['metod1'] + "\n" + request.form['metod2'] + "\n" + request.form['metod3'] + "\n" +
			  request.form['metod4'] + "\n" + request.form['metod5'] + "\n" + request.form['metod6'] + "\n" +
			  request.form['metod7'] + "\n" + request.form['metod8'] + "\n" + request.form['metod9'] + "\n" +
			  request.form['metod10'])
		f = open("resultsmobile.txt", "a")
		scr = 0
		l1 = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]
		for i in range(0, 10):
			if l1[i] == request.form['metod' + str(i + 1)]:
				scr = scr + 1
		f.write(request.form['usn'] + "\t" + str(scr) + "\n")
		f.close()
		return render_template("success.html", score=str(scr), usn=request.form['usn'])

if __name__ == '__main__':
	app.run(debug=True)
