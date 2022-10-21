from flask import Flask, render_template, request, redirect
app=Flask(__name__)

edit_1=None

@app.route("/")
def Homepage():
    return render_template("loginpage.html")

@app.route("/profile" , methods=["GET","POST"])
def edit():
    print(edit_1)
    # username=request.form["User_Name"]
    # email=request.form["Email"]
    # date=request.form["date"]
    # number=request.form["number"]
    username="Sakthi"
    email="Sakthi@gmail.com"
    date="12-07-2022"
    number="2312341243"
    return render_template("site1.html", name=username,email=email,date=date,number=number ,edit=edit_1)

@app.route("/editProfile")
def edit_profile():
    global edit_1
    edit_1=True
    print(edit_1)
    return redirect("/profile")

@app.route("/update")
def update_profile():
    global edit_1
    edit_1=None
    print(edit_1)
    return redirect("/profile")


if __name__=="__main__" :
    app.run(debug=True)