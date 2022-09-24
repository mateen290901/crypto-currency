from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
em=''
pwd=''
cp=''


# Create your views here.


def signupaction(request):
    global fn,ln,em,pwd,cp
    if request.method=="POST":
        mydb =sql.connect(host="localhost",user="root",password="M@teen_29",database="crypto_currency")
        cursor=mydb.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="First_Name":
                fn=value
            if key=="Last_Name":
                ln=value
            if key=="Email_id":
                em=value
            if key=="password":
                pwd=value
            if key=="confirm_password":
                cp=value
        c="insert into users values ('{}','{}','{}','{}','{}')".format(fn,ln,em,pwd,cp)
        cursor.execute(c)
        mydb.commit()
    return render(request,'signup_page.html',{})
                