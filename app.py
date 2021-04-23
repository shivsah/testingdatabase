from flask import Flask, render_template, request

from flask_mysqldb import MySQL

app =  Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']='cannabis' 
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'



mysql = MySQL(app)

app.static_folder = 'static'

@app.route('/strains', methods=["GET","POST"])
def strains():
    if request.method=="POST":
        search = request.form.get("search")
        print(search)
    cur = mysql.connection.cursor()
    results= cur.execute("SELECT * FROM cannabisreco WHERE Rating = :search", {"search":search}).fetchall()

    #cur = mysql.connection.cursor()
    #cur.execute("SELECT * FROM cannabisreco")
    #results = cur.fetchall()   
    #print(results)
    #print(type(results))
    #global user_search 
    #user_search = search
    #results= cur.execute("SELECT * FROM cannabisreco WHERE Rating = :user_search", {"user_search":user_search}).fetchall()
        #results=cur.fetchall()
        
    #print(search)
    #
    #return render_template("strains.html", data= results , ss =search)
    return render_template("strains.html",data = results)
@app.route('/')
def age_confirmation():
    return render_template("ageconfirmation.html")

if __name__ =="__main__":
    app.run(debug=True)

