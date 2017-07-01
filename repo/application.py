import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)
database = 'mydb.db'


def connect():
    return sqlite3.connect(database)


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/addnew' ,methods=['GET'] )
def add():
    return render_template("addnew.html")


@app.route('/fetch', methods=['POST'])
def fetch():
        name = request.form['ename']
        add = request.form['addr']
        pin = request.form['pin']
        mob = request.form['pin']
        sal = request.form['sal']

        query = "INSERT INTO employee(name,address,pin,mob,salary) VALUES ('{}','{}','{}','{}','{}')"
        print(query)
        cur = connect().cursor()
        cur.executescript(query.format(name, add, pin, mob, sal))
        connect().commit()
        connect().close()
        cur.close()
        return render_template("result.html")


@app.route('/read' , methods=['GET'])
def read():
    connect()
    cur = connect().cursor()
    cur.execute("SELECT name,address,pin,mob,salary FROM employee;")
    items=[dict(name=row[0],address=row[1],pin=row[2],mob=row[3],salary=row[4]) for row in cur.fetchall()]
    return render_template("read1.html", items=items)


@app.route('/update' , methods=['GET'])
def update():
    return render_template('Update.html')

@app.route('/updating' , methods=['POST'])
def updating():
    name = request.form['ename']
    add = request.form['addr']
    pin = request.form['pin']
    mob = request.form['pin']
    sal = request.form['sal']
    connect()
    cur = connect().cursor()
    query = "UPDATE employee SET name='{}'  , address='{}' , pin = '{}', mob = '{}' , salary = '{}' WHERE name == '{}' "
    cur.executescript(query.format(name, add, pin, mob, sal,name))
    connect().commit()
    connect().close()
    return render_template('result.html')

@app.route('/delete',methods=['GET'])
def delete():
    return render_template("delete.html")

@app.route('/deleteing' , methods=['POST'])
def deleting():
    name = request.form['ename']
    connect()
    cur = connect().cursor()
    query = "delete from employee where name='{}'"
    cur.executescript(query.format(name))
    connect().commit()
    connect().close()
    return render_template("result.html")




if __name__ == ("__main__"):
    app.run(debug=True)