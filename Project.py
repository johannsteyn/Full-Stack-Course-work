with open('a', 'w' ) as f: f.write('#!/bin/sh\nexit 0')
from flask import Flask
app = Flask(__name__)


from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurnt).first()
	items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
	output = ''
	for i in items:
		output += i.name
		output += '</br>'
		output += i.price
		output += '</br>'
		output += i.description
		output += '</br>'
		output += '</br>'
	return output
@app.route('/restaurant/<int:restaurant_id>/new/')	
def newMenuItem(restaurant_id):
	return "page to create a new menu item. Task 1 complete!"
@app.route('/restaurant_id/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
	return "page to edit a menu item. Task 2 complete!"
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_it):
	return "page to delete a menu item. Task 3 complete!"		

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)