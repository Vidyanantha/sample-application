from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def Homepage():
    return render_template("loginpage.html")

@app.route("/profile" , methods=["GET","POST"])
def edit():
    username=request.form["User_Name"]
    email=request.form["Email"]
    date=request.form["date"]
    number=request.form["number"]
    return render_template("site1.html", name=username,email=email,date=date,number=number)

if __name__=="__main__" :
    app.run(debug=True)