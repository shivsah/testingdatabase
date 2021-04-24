from flask import Flask, render_template, request

from flask_mysqldb import MySQL

app =  Flask(__name__)

app.config['MYSQL_HOST'] = '192.168.1.128'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']= 'Admin@123'
app.config['MYSQL_DB']='cannabis'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'



mysql = MySQL(app)

app.static_folder = 'static'

@app.route('/strains', methods=["GET","POST"])
def strains():
    render_template("strains.html")
    if request.method=="POST":
        search = request.form.get("search")
        cur = mysql.connection.cursor()
        sqlquery = ("SELECT * from cannabis WHERE Rating = {}".format(search))
        cur.execute(sqlquery)
        results= cur.fetchall()
        print(results)
    #return render_template("strains.html", data= results , ss =search)
    return render_template("strains.html",data = results)
@app.route('/')
def age_confirmation():
    return render_template("ageconfirmation.html")

if __name__ =="__main__":
    app.run(debug=True)
