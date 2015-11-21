#! /usr/bin/env python27
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask.ext.moment import Moment
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

from datetime import datetime

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What item would you like to add?', validators=[Required()])
    submit = SubmitField('Submit')
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'BigSeekritNoboddyNoze'
moment = Moment(app)
bootstrap = Bootstrap(app)

shoppingList = ['Milk', 'Eggs']

@app.route('/', methods=['GET', 'POST'])
def index():
    global shoppingList
    item = None
    form = NameForm()
    if form.validate_on_submit():
    	shoppingList.append(form.name.data)
    	form.name.data=''
    return render_template("index.html", items = shoppingList, current_time=datetime.utcnow(), form = form)

@app.route('/remove/<name>')
def remove_item(name):
	global shoppingList
	if name in shoppingList: 
		shoppingList.remove(name)
	else:
		#flash message item not in shoppingList
		pass
	return redirect(url_for('index'))
	
@app.route('/api/items')
def get_items():
	global shoppingList
	return jsonify({'items': shoppingList})
	
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
	 
if __name__ == '__main__':
    app.run(debug=True)