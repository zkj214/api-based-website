from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap5 #pip install bootstrap-flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
import requests
import os
from datetime import date
import time


app=Flask(__name__)
app.config["SECRET_KEY"]=os.environ.get("FLASK_KEY")

bootstrap=Bootstrap5(app)


class AskChatbotForm(FlaskForm):
    query=StringField("",validators=[DataRequired()])
    submit=SubmitField("Chat")


@app.route('/',methods=["GET","POST"])
def home():
    current_year=date.today().year
    #form=AskChatbotForm()
    if request.method=="POST":
        user_query=request.form.get("query")
        return render_template("index.html", user=True, year=current_year, user_txt=user_query)
        
        if user_query:
            time.sleep(3)
            url = "https://robomatic-ai.p.rapidapi.com/api"
    
            payload = {
                "in": f"{user_query}",
                "op": "in",
                "cbot": "1",
                "SessionID": "RapidAPI1",
                "cbid": "1",
                "key": os.environ.get("BOT_KEY"),
                "ChatSource": "RapidAPI",
                "duration": "1"
            }
            headers = {
                "content-type": "application/x-www-form-urlencoded",
                "X-RapidAPI-Key": os.environ.get("API_KEY"),
                "X-RapidAPI-Host": "robomatic-ai.p.rapidapi.com"
            }
    
            response = requests.post(url, data=payload, headers=headers)
    
            data=response.json()["out"]
            return render_template("index.html",response=data,user=True,bot=True,year=current_year,user_txt=user_query)
    return render_template("index.html",year=current_year)


if __name__=="__main__":
    app.run(debug=False)