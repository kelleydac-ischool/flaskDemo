#! /usr/bin/env python27
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

shoppingList = ['Milk', 'Eggs']

@app.route('/', methods=['GET', 'POST'])
def index():
    global shoppingList
    if request.method == 'POST':
        shoppingList.append(request.form['item'])
    return render_template("index.html", items = shoppingList)

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
	 
if __name__ == '__main__':
    app.run(debug=True)