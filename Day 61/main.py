from flask import Flask, render_template, session, request, url_for
from wtforms import Form, StringField, PasswordField, validators, SubmitField
from flask_bootstrap import Bootstrap


class RegForm(Form):
    email = StringField('Email Address',
                        [validators.Email(check_deliverability=True, allow_empty_local=True, granular_message=True),
                         validators.DataRequired()])
    password = PasswordField('New Password', [validators.DataRequired(), validators.Length(min=8, max=16)])
    ok = SubmitField('Login')


DEBUG = True
app = Flask(__name__)
app.config['SECRET_KEY'] = "b_5#y2LF4Q8z\n\xec]/"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = RegForm(request.form)
    if request.method == 'POST' and form.validate():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
