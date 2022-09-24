from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''


# Create your views here.


def loginaction(request):
    global em,pwd
    if request.method=="POST":
        mydb =sql.connect(host="localhost",user="root",password="M@teen_29",database="crypto_currency")
        cursor=mydb.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Email_id":
                em=value
            if key=="password":
                pwd=value
           
        c="select * from users where Email_id ='{}' and password='{}' " .format(em,pwd,)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")
    return render(request,'login_page.html')
                