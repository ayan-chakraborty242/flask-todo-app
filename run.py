#main file
from flask import Flask,render_template,redirect,url_for
from app.form import TodoApp
import mysql.connector

app=Flask(__name__)
app.secret_key= "secret"
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="7434",
        database="todo"
    )

@app.route("/",methods=["POST","GET"])
def todo():
    form= TodoApp()
    conn=get_db_connection()
    cursor=conn.cursor()
    
    if form.validate_on_submit():
        task=form.task.data
        cursor.execute("INSERT INTO tasks (task) values(%s)",(task,))
        conn.commit()
        
        return redirect(url_for('todo'))
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()

    
    return render_template("app.html",form=form,tasks=tasks)

@app.route("/delete/<int:id>")
def delete_task(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('todo'))

    

if __name__=="__main__":
    app.run(debug=True)