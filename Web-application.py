from flask import Flask, redirect, url_for, render_template, request
import pyodbc
import mysql
import mysql.connector as c

User_Symptoms=""
conn = c.connect(host="localhost", database="symptodoc", user="root", passwd="amaatra")
cursor = conn.cursor()
cursor.execute('select * from disease_table')

app = Flask(__name__)
app.secret_key = "Hello"

@app.route("/login", methods=["POST", "GET"])
def homepage():
    return render_template("LoginPage.htm", content="Samarth Mishra")

@app.route("/Database")
def database():
    return render_template("HtmlDatabasepage.htm")

@app.route("/admin")
def admin():
    return redirect(url_for("homepage"))

@app.route("/test")
def test():
    return render_template("InheritenceTest.htm")


@app.route("/")
def home():
    return render_template("HomePage.htm", methods=["POST", "GET"])

@app.route("/Developers")
def Developers():
    return render_template("DevelopersPage.htm")

@app.route("/Malaria")
def thePy():
    return render_template("Malaria.htm")

@app.route("/Signup")
def signup():
    return render_template("SignupPage.htm")

@app.route("/Searcher", methods=["POST", "GET"])
def searcher():
    if request.method == "POST":
        Symptoms = request.form["nm"]
        from typing import Counter
        import pyodbc

        conn = c.connect(host="localhost", database="symptodoc", user="root", passwd="amaatra")
        cursor = conn.cursor()
        cursor.execute('select * from disease_table')
        Data_to_Webpage_Carrier = str()

        User_Input=str(Symptoms).lower().replace(",", "")
        Usable_User_Input=User_Input.split()
        Disease=""
        Search_Result=[]
        for row in cursor.fetchall():
            for r in range(0,len(Usable_User_Input)):
                Usable_Database_Disease=row[2]
                Usable_Database_Disease=str(Usable_Database_Disease).replace(",", "").split()
                for i in range(0,len(Usable_Database_Disease)):
                    if(Usable_Database_Disease[i]==Usable_User_Input[r]):
                        Search_Result.append(row[1])
        Record_Dictionary=dict()
        for i in range(0,len(Search_Result)):
            Comparer=Search_Result[i]
            Counter=int()
            for r in range(0,len(Search_Result)):
                if(Comparer==Search_Result[r]):
                    Counter=Counter+1
                    Record_Dictionary[Comparer]=Counter
        Sorted_Record_Dictionary=sorted(Record_Dictionary, key=Record_Dictionary.get, reverse=True)
        To_Use_HTML = '<!DOCTYPE html><html lang="en">    <head>        <meta name="viewport" content="initial-scale=1, width=device-width">        <meta charset="utf-8">        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">        <title>SymptoDoc - The Virtual Medical Consultant</title>        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">        <style>            .center            {                text-align: center;            }            .titledFont            {                font-family: Arial, Helvetica, sans-serif;            }            .topPageSize            {                font-size: xx-large;            }            .topPageColor            {                text-decoration-color: rgb(68, 68, 68);            }            .topSubColor            {                text-decoration-color: rgb(151, 151, 151);            }            .bodySize            {                font-size: large;            }            .bottonpadding            {                padding-right: 20px;            }            .bottoncolor            {                text-decoration-color: white;                text-decoration-style: dotted;            }            .To_HTML            {                padding-left: 20px;                font-size: large;            }        </style>    </head>    <body>        <div class="alert alert-warning" role="alert">            CAUTION!! Site currently under Development          </div>        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">            <a class="navbar-brand" href="http://127.0.0.1:5000/">SymptoDoc</a>            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">              <span class="navbar-toggler-icon"></span>            </button>                      <div class="collapse navbar-collapse" id="navbarSupportedContent">              <ul class="navbar-nav mr-auto">                <li class="nav-item active">                  <a class="nav-link" href="http://127.0.0.1:5000/">Home <span class="sr-only">(current)</span></a>                </li>                <li class="nav-item">                  <a class="nav-link" href="http://127.0.0.1:5000/Searcher">DataBase</a>                </li>                <li class="nav-item dropdown">                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">                    Options                  </a>                  <div class="dropdown-menu" aria-labelledby="navbarDropdown">                    <a class="dropdown-item" href="#">Help</a>                    <a class="dropdown-item" href="#">Feedback</a>                    <div class="dropdown-divider"></div>                    <a class="dropdown-item" href="http://127.0.0.1:5000/Developers">Developers</a>                  </div>                </li>                <li class="nav-item">                  <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Feel Well</a>                </li>              </ul>              <form action="http://127.0.0.1:5000/login" class="form-inline my-2 my-lg-0 bottonpadding bottoncolor">                  <button class="btn btn-outline-success my-2 my-sm-0" type="login">Login</a></button>                    </form>              <form class="form-inline my-2 my-lg-0">                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>              </form>            </div>          </nav>        <br><br>        '
        Filtered_Links=[]
        cursor.execute('select * from disease_table')
        Table_Dictionary = dict()
        for data in cursor.fetchall():
            Table_Dictionary[data[1]] = data[3]


        for d in Sorted_Record_Dictionary:
            a=Table_Dictionary[d]
            To_Use_HTML = To_Use_HTML+'<div class="To_HTML"><p><h5>'+d+'   -   </h5><h5><a href="'+Table_Dictionary[d]+'">'+Table_Dictionary[d]+'</a></h5></p>'

        To_Use_HTML = To_Use_HTML+"<p>"+'<br><br>        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>    </body></html></html>'




        HTML_LinkPage = open(r"C:\Users\Ullas\Desktop\SymptoDoc Code-20220326T063923Z-001\SymptoDoc Code\templates\HTML_ResultPage_Rudimentary.htm", 'w')
        HTML_LinkPage.write(To_Use_HTML)
        return redirect(url_for("Results"))
    else:
        return render_template("UserInputPage.htm")
   

@app.route("/Results", methods=["POST", "GET"])
def Results():
    return render_template("HTML_ResultPage_Rudimentary.htm")

@app.route("/Covid")
def covid():
    return render_template("covid.htm")

@app.route("/Pneumonia")
def pneumonia():
    return render_template("Pneumonia.htm")


@app.route("/Malaria")
def malaria():
    return render_template("Malaria.htm")

@app.route("/Scarlet_fever")
def scarlet_fever():
    return render_template("Scarlet_Fever.htm")

@app.route("/Diarrhea")
def diarrhea():
    return render_template("Diarrhoea.htm")

@app.route("/Dengue")
def dengue():
    return render_template("Dengue.htm")

@app.route("/Aids")
def aids():
    return render_template("AIDS.htm")

@app.route("/Schizophrenia")
def Schizophrenia():
    return render_template("Schizophrenia.htm")

@app.route("/Anal_cancer")
def Anal_cancer():
    return render_template("Anal_cancer.htm")

@app.route("/Alzheimer")
def Alzheimer():
    return render_template("Alzhemer's_Disease.htm")

@app.route("/Mouth_ulcer")
def Mouth_ulcer():
    return render_template("Mouth_ulcer.htm")

@app.route("/Chicken_pox")
def Chicken_pox():
    return render_template("Chicken_pox.htm")

@app.route("/Tonsillitis")
def Tonsillitis():
    return render_template("Tonsillitis.htm")

@app.route("/Tubercolosis")
def Tubercolosis():
    return render_template("Tubercolosis.htm")

@app.route("/Insomnia")
def Insomnia():
    return render_template("Insomnia.htm")

@app.route("/Arthritis")
def Arthritis():
    return render_template("Arthritis.htm")

@app.route("/Hypherhidrosis")
def Hypherhidrosis():
    return render_template("Hypherhidrosis.htm")

@app.route("/Conjunctivitis")
def Conjunctivitis():
    return render_template("conjunctivitis.htm")

@app.route("/Flu")
def Flu():
    return render_template("Flu.htm")

@app.route("/Epilepsy")
def Epilepsy():
    return render_template("Epilepsy.htm")

@app.route("/Hepatitis_C")
def Hepatitis_C():
    return render_template("Hepatitis_c.htm")

@app.route("/Diphtheria")
def Diphtheria():
    return render_template("diphtheria.htm")

@app.route("/Gonorrhoea")
def Gonorrhoea():
    return render_template("Gonorrhoea.htm")

@app.route("/Influenza")
def Influenza():
    return render_template("influenza.htm")

@app.route("/Hepatitis_B")
def Hepatitis_B():
    return render_template("Hepatitis_b.htm")

@app.route("/Diabetes")
def Diabetes():
    return render_template("diabetes.htm")

@app.route("/Hepatitis_A")
def Hepatitis_A():
    return render_template("Hepatitis_a.htm")

@app.route("/HIV")
def HIV():
    return render_template("HIV.htm")

@app.route("/Ebola")
def Ebola():
    return render_template("ebola.htm")

@app.route("/E_coli")
def E_coli():
    return render_template("E_coli.htm")


@app.route("/<usr>", methods=["POST", "GET"])
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
