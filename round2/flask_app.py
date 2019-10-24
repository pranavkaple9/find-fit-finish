from flask import Flask, render_template, request, session
import pyrebase
import random

config = {
    "apiKey": "AIzaSyB4yzIXobku5uXoUqC8rOf5ljmm0JOg0Uc",
    "authDomain": "f3-test-4723d.firebaseapp.com",
    "databaseURL": "https://f3-test-4723d.firebaseio.com/",
    "storageBucket": "gs://f3-test-4723d.appspot.com/",
    "messagingSenderId": "983165075832",
    "appId": "1:983165075832:web:4c2b31e43b1a978d"
}
firebase = pyrebase.initialize_app(config)
app = Flask(__name__)
app.secret_key = "tanstar4567"

@app.route('/register', methods=['POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        pin = request.form['pin']
        mobile = request.form['mobile']
        college = request.form['college']
        branch = request.form['branch']
        if pin!="x1z4f6y8" and pin!="f6y9r5i8" and pin!="g0u7s3v5" and pin!="i8a1s6x4":
            return render_template("startpage-1.html")
        if pin=="x1z4f6y8":
            session['set']=1
        if pin=="f6y9r5i8":
            session['set']=2
        if pin=="g0u7s3v5":
            session['set']=3
        if pin=="i8a1s6x4":
            session['set']=4

        details = {'name': name, 'mobile': mobile, 'college': college, 'branch': branch}
        db = firebase.database()
        db.child("round-2-register").push(details)
        session['username'] = name
        session['mobile'] = mobile
        session['qno'] =1
        qno=session['qno']
        session['totalScore']=0
        db=firebase.database()
        dict1 = {}
        for j in db.child("round-2"+str(session['set'])).child(str(qno)).get().each():
            dict1[j.key()] = j.val()
        val = qno
        result=dict1
        result['qno']=qno
        session['hintstatus']='empty'
        result['hintstatus']=session['hintstatus']
        result['totalScore'] = session['totalScore']
        result['scoreObtained']=dict1['score']
        print(result)
        det={'name':name,'mobile':mobile,'score':0,'time':'30:00'}
        db.child("round2-results").push(det)
        return render_template("exp.html",qdata=result);


@app.route('/submitAnswer', methods=['POST'])
def submitAnswer():
    if request.method=="POST":
        if "Finish Test" in request.form.values():
            db = firebase.database()
            dict1 = {}
            dict3={}
            for j in db.child("round-2"+str(session['set'])).child(str(session['qno'])).get().each():
                if j.key()=='answer':
                    dict1[j.key()] = j.val()
                if j.key()=='score':
                    dict3[j.key()]=j.val()
            userAns=request.form['hidden']
            time="0:00"
            if "hidden2" in request.form.values():
                time=request.form['hidden3']
            
            if str(userAns).lower()==str(dict1['answer']).lower():

                if session['hintstatus']=='hint1':
                    session['totalScore'] += dict3['score']*0.8
                elif session['hintstatus']=='hint2':
                    session['totalScore'] += dict3['score']*0.4
                else:
                    session['totalScore'] += dict3['score']
            for j in db.child("round2-results").get().each():
                scoreds=j.val()
                if scoreds['name']==session['username'] and scoreds['mobile']==session['mobile']:
                    db.child("round2-results").child(j.key()).update({'name':session['username'],'mobile':session['mobile'],'score':session['totalScore'],'time':time})
                    print("1")
                    break;

            return render_template("thankyou.html",score=session['totalScore']);
            
        qno = session['qno']
        db = firebase.database()
        dict1 = {}
        dict3={}
        for j in db.child("round-2"+str(session['set'])).child(str(qno)).get().each():
            if j.key()=='answer':
                dict1[j.key()] = j.val()
            if j.key()=='score':
                dict3[j.key()]=j.val()
        userAns=request.form['userAns']
        if str(userAns).lower()==str(dict1['answer']).lower():
            
            if session['hintstatus']=='hint1':
                session['totalScore'] += dict3['score']*0.8
            elif session['hintstatus']=='hint2':
                session['totalScore'] += dict3['score']*0.4
            else:
                session['totalScore'] += dict3['score']
            if qno<5:
                qno += 1
                dict2 = {}
                session['qno'] = int(qno)
                for j in db.child("round-2"+str(session['set'])).child(str(qno)).get().each():
                    dict2[j.key()] = j.val()
                dict2['qno'] = session['qno']
                dict2['totalScore']=session['totalScore']
                dict2['scoreObtained']=dict2['score']
                session['hintstatus'] = 'empty'
                dict2['hintstatus'] = session['hintstatus']
                
                for j in db.child("round2-results").get().each():
                    scoreds=j.val()
                    if scoreds['name']==session['username'] and scoreds['mobile']==session['mobile']:
                        db.child("round2-results").child(j.key()).update({'name':session['username'],'mobile':session['mobile'],'score':session['totalScore'],'time':request.form['finish']})
                        break;
                return render_template("exp.html", qdata=dict2);
            else:
                dict2 = {}
                session['qno'] = int(qno)
                for j in db.child("round-2"+str(session['set'])).child(str(qno)).get().each():
                    dict2[j.key()] = j.val()
                dict2['qno'] = session['qno']
                dict2['totalScore']=session['totalScore']
                dict2['scoreObtained']=dict2['score']
                session['hintstatus'] = 'empty'
                dict2['hintstatus'] = session['hintstatus']
                for j in db.child("round2-results").get().each():
                    scoreds=j.val()
                    if scoreds['name']==session['username'] and scoreds['mobile']==session['mobile']:
                        db.child("round2-results").child(j.key()).update({'name':session['username'],'mobile':session['mobile'],'score':session['totalScore'],'time':request.form['finish']})
                        break;
                return render_template("thankyou.html",score=session['totalScore']);


        else:
            dict2={}
            for j in db.child("round-2"+str(session['set'])).child(str(qno)).get().each():
                dict2[j.key()] = j.val()
            dict2['qno'] = session['qno']
            dict2['hintstatus']=session['hintstatus']
            dict2['totalScore'] = session['totalScore']
            if session['hintstatus']=='empty':
                dict2['scoreObtained'] = dict2['score']
            elif session['hintstatus']=='hint1':
                dict2['scoreObtained'] = 0.8*dict2['score']
            elif session['hintstatus']=='hint2':
                dict2['scoreObtained'] = 0.4*dict2['score']
            return render_template("exp.html", qdata=dict2);

@app.route('/obtainHint',methods=['POST'])
def takenhint1():
    if request.method=="POST":

        hint_taken=request.form['Hint']
        if session['hintstatus']=="empty":
            session['hintstatus']='hint1'

            qno = session['qno']
            db = firebase.database()
            dict2 = {}
            for j in db.child("round-2"+str(session['set'])).child(str(qno)).get().each():
                dict2[j.key()] = j.val()
            dict2['qno'] = session['qno']
            dict2['hintstatus'] = session['hintstatus']
            dict2['scoreObtained'] = 0.8*dict2['score']
            dict2['totalScore'] = session['totalScore']
            return render_template("exp.html", qdata=dict2);
        elif session['hintstatus']=="hint1":
            session['hintstatus'] = 'hint2'
            qno = session['qno']
            db = firebase.database()
            dict2 = {}
            for j in db.child("round-2"+str(session['set'])).child(str(qno)).get().each():
                dict2[j.key()] = j.val()
            dict2['qno'] = session['qno']
            dict2['hintstatus'] = session['hintstatus']
            dict2['scoreObtained'] = 0.4 * dict2['score']
            dict2['totalScore'] = session['totalScore']
            return render_template("exp.html", qdata=dict2);


    return render_template("exp.html")

@app.route('/')
def home():
    return render_template("startpage-1.html")

@app.route('/leaderboard')
def leaderboard():
    db=firebase.database()
    list1=[]
    for j in db.child("round2-results").get().each():
        list1.append(j.val())
    list2=sorted(list1,key=lambda i:(i['score'],i['time']),reverse=True)
    for i in range(0,len(list2)):
        list2[i]['sno']=i+1;
    return render_template("leaderboard.html",data=list2)
if __name__ == "__main__":
    app.run(debug=True)