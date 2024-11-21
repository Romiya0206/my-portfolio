from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5

class ReviewForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = StringField('Message')


class Info():
    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

app = Flask(__name__)
Bootstrap5(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/", methods=["POST", "GET"])
def homepage():
    form = ReviewForm()
    if form.validate_on_submit():
        print("yes")
        print(form.name.data)
        info = Info(form.name.data, form.email.data, form.subject.data, form.message.data)
        print(info.message)
    return render_template("index.html", form=form)


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio-details.html")


if __name__ == "__main__":
    app.run(debug=True)
