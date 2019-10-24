from flask import Flask, render_template, request, session
import random
app = Flask(__name__)
@app.route('/submitAnswer', methods=['POST'])
def submitAnswer():
    if request.method == "POST":
        ans1 = request.form['ans1']
        ans2 = request.form['ans2']
        ans3 = request.form['ans3']
        ans4 = request.form['ans4']
        if ans1=="17.3921°N" and ans2=="78.3145°E" and str(ans3).upper()=="TI SPA" and str(ans4)=="54720":
            return render_template("youwon.html")
        else:
            return render_template("qpage.html")
@app.route('/')
def home():
    return render_template("qpage.html")
if __name__ == "__main__":
    app.run(debug=True)
