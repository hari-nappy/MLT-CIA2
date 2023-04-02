from flask import Flask, request
from flask import render_template
import pymysql as pms
app=Flask(__name__)#obj for flask class

import pickle
model=pickle.load(open('cmodel.pkl','rb'))#load the pkl obj created and open it, put it in a varibale called model
#rb: read in bytes
conn=pms.connect(host="localhost",user="root",password="Shri_Hari98!",db="logins")
cur=conn.cursor()
cur.execute("select * from details")
res=cur.fetchall()

@app.route("/",methods=['GET','POST'])
def start():
    if request.method=='GET':
        return render_template("login.html")
    if request.method=='POST':
        uname=request.form['username']
        pwd=request.form['password']
        '''conn=pms.connect(host="localhost",user="root",password="Shri_Hari98!",db="logins")
            cur=conn.cursor()
            cur.execute("select * from details")
            res=cur.fetchall()'''
        namelist=[]
        pwdlist=[]
        for i in res:
                #print(res)
            namelist.append(i[0])
            pwdlist.append(i[1])

        if uname not in namelist:
                return render_template("login.html",display="Invalid email!")
        elif pwd not in pwdlist:
                return render_template("login.html",display="Invalid password!")
        else:
                return render_template("success.html")

@app.route("/predict",methods=['POST'])
def predict():
    if request.method=='POST':
        age=request.form['age']
        Salary=request.form['sal']
        predn=model.predict([[int(age),int(Salary)]])[0]
        if predn==0:
            return render_template("success.html",text='Value of Purchased is 0')
        elif predn==1:
             return render_template("success.html",text='Value of Purchased is 1')
#or return render_template("index.html",data="Salary is {}".format(pred))
if __name__=='__main__':
    app.debug=True
    app.run()#runs on a certain host and port