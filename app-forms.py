from flask import Flask, render_template, redirect, url_for, request

import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField, TextAreaField, FieldList, PasswordField
from wtforms.validators import InputRequired, URL
from wtforms.widgets import ColorInput, Input

app = Flask(__name__)
app.secret_key = ':)'
# Main
@app.route('/')
def index():
		return render_template("index.html")

# Forms class
class yt_form(FlaskForm):
	yt_input = StringField('YT url:', validators=[URL(require_tld=True, message='Podaj poprawny link do video na YouTube')])
	text = "Możesz dodać opis do linku:"
	yt_textarea =  TextAreaField(text)
	password = PasswordField('Wpisz hasło -> :)xD;)', validators=[InputRequired('Hasło jest wymagane')])
	button = SubmitField(' Wyslij ')
# Forms
@app.route('/yt_urls', methods=["GET", "POST"])
def yt_urls():
	form = yt_form()
	if not form.yt_input.data:
		form.yt_input.data = 'https://www.youtube.com/watch?v=jR2aFKuaOBs'
	if request.method == 'POST':
		zapisz()
		
	if form.validate_on_submit():
		yt_input = form.yt_input.data
		yt_textarea = form.yt_textarea.data
		password = form.password.data
		output_data = '{}\n{}\n\n'.format(yt_input, yt_textarea)
		
		if password == 'aassaa':
			save_data(output_data)
			#return yt_urls(yt_input)
			#thankyou_message = "<h1>Dzieki za dodanie url: "+yt_input+"</h1>"
			#thankyou_message+= '<iframe width="560" height="315" src="'+yt_input+'" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
			#return thankyou_message 
			return redirect( url_for("yt_url_save", url=yt_input) )
	return render_template("yt_urls.html", form=form)

#@app.route("/<string:url>")
@app.route("/yt_url_save")
def yt_url_save(url):
	zapisz()
	re
	return "<h1>Dzieki za dodanie url: "+url+"</h1>"

# Helpers
def save_data(string):
		with open('data/data.txt', "a") as f:
				f.write(string)
def check_yt_url():
	pass
# Errors
@app.errorhandler(404)
def handle_404(e):
		return render_template('404.html'), 404
@app.errorhandler(500)
def handle_500(e):
		return render_template('500.html'), 500

if __name__=="__main__":
		app.run(debug=True)