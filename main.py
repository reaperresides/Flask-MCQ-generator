from flask import Flask,render_template,url_for,request,redirect,send_from_directory
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"]="Localhost"
app.config["MYSQL_USER"]="imran"
app.config["MYSQL_PASSWORD"]="imran123"
app.config["MYSQL_DB"]="mechanical"

mysql=MySQL(app)


@app.route('/')
def Home():
    return render_template("home.html")


@app.route('/contact')
def Contact():
    return render_template("contact.html")


@app.route('/about')
def About():
    return render_template("about.html")


@app.route('/mechanical',methods=["GET","POST"])
def mechanical():
    if request.method=="POST":
        if request.form["radiob"]!="option1":
            return redirect(url_for("dev"))
        return redirect(url_for("Modules"))
    return render_template("mech.html")


@app.route('/dev')
def dev():
    return render_template("dev.html")

@app.route('/modules',methods=["GET","POST"])
def Modules():
    global fetching_size,fetchdata
    if request.method=="POST":
        mylist=["option1","option2","option3","option4"]
        if request.form["exampleRadios"] not in mylist:
            return redirect(url_for("dev"))
        else:
            fetching_size=int(request.form["nquestions"])
            if fetching_size<2 or fetching_size>20:
                return "please select valid Number of Questions"
            else:
                if request.form["exampleRadios"]=="option1":
                        cur=mysql.connection.cursor()
                        cur.execute("SELECT * FROM `mechanical subjects` WHERE `module`=1 ORDER BY RAND()")
                        fetchdata=cur.fetchmany(size=fetching_size)
                        cur.close()
                        return render_template("MCQs.html",data=fetchdata)
                if request.form["exampleRadios"]=="option2":
                        cur=mysql.connection.cursor()
                        cur.execute("SELECT * FROM `mechanical subjects` WHERE `module`=2 ORDER BY RAND()")
                        fetchdata=cur.fetchmany(size=fetching_size)
                        cur.close()
                        return render_template("MCQs.html",data=fetchdata)
                if request.form["exampleRadios"]=="option3":
                        cur=mysql.connection.cursor()
                        cur.execute("SELECT * FROM `mechanical subjects` WHERE `module`=3 ORDER BY RAND()")
                        fetchdata=cur.fetchmany(size=fetching_size)
                        cur.close()
                        return render_template("MCQs.html",data=fetchdata)
                if request.form["exampleRadios"]=="option4":
                        cur=mysql.connection.cursor()
                        cur.execute("SELECT * FROM `mechanical subjects` WHERE `module`=4 ORDER BY RAND()")
                        fetchdata=cur.fetchmany(size=fetching_size)
                        cur.close()
                        return render_template("MCQs.html",data=fetchdata)
            


    return render_template("MCQs.html")


@app.route('/mcqs',methods=["GET","POST"])
def MCQs():
    if request.method=="POST":
        Answers=[]
        for i in range(fetching_size):
            Answers.append(request.form["exampleRadios"+str(i)])
        result_data=[]    
        for index,data in enumerate(fetchdata):
            result_data.append((data[3],data[4],data[5],data[6],data[7],data[8],data[int(Answers[index])+3]))
        return render_template("result.html",data=result_data)
    return render_template("result.html")
        
    




