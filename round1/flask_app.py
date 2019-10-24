from flask import Flask,render_template,request,session
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
app=Flask(__name__)
app.secret_key="tanstar4567"
@app.route('/register',methods=['POST'])
def register():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        mobile=request.form['mobile']
        college=request.form['college']
        year=request.form['year']
        branch=request.form['branch']
        details={'name':name,'email':email,'mobile':mobile,'college':college,'year':year,'branch':branch}
        db=firebase.database()
        db.child("student").push(details)
        session['username']=name
        session['mobile']=mobile
        val=random.randint(1,4)
        exam_questions=''
    
        #print("welcome")
        #print(val)

        if val==1:
            exam_questions=db.child("exam").get()
        else:
            exam_questions=db.child("exam"+'-'+str(val)).get()
        session['set']=val
        
        dict1={}
        for i in exam_questions.each():
            dict1[i.key()]=i.val()
        del dict1[0]
        print(dict1)
    return render_template("test.html",val1=dict1)
@app.route('/')
def homepage():
    return render_template("registration.html")
@app.route('/submitTest',methods=['POST'])
def submitAnswer():
    original_ans=[]
    db=firebase.database()
    val=session['set']
    exam=''
    
    #print("welcome")
    #print(val)

    if val==1:
        exam=db.child("exam").get()
    else:
        exam=db.child("exam"+'-'+str(val)).get()
    for i in exam.each():
        if i.val() is not None:
            print(i.val())
            temp=i.val()
            original_ans.append(str(i.key())+temp['answer'])
    print(original_ans)
    if request.method=="POST":
        answered=request.form.values()
        c=0
        for v in answered:
            if v in original_ans:
                c+=1
        print(c)
        print(session['username'])
        score_det={"name":session['username'],"mobile":session['mobile'],"score":c}
        db.child("results").push(score_det)
        return render_template("thankyou.html")
if  __name__=="__main__":
    app.run()
