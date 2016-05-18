"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
       
        self.load_model('Product')
        self.db = self._app.db

   
    def index(self):
        products = self.models['Product'].get_products()
        return self.load_view('index.html', products =products)
    
    def new(self):
        return self.load_view('add.html')
    
    def create(self):
        name =request.form['name']
        description = request.form['description']
        price = request.form['price']
        if self.models['Product'].add_product(name, description, price)== True:
            return redirect('/')
        else :
            flash("price must be a numerical")
            return redirect('/products/new')
            
    
    def show(self, product_id):
        products = self.models['Product'].get_product_by_id(product_id)
        return self.load_view('show.html', product = products[0])

    def edit(self, product_id):
        products = self.models['Product'].get_product_by_id(product_id)
        return self.load_view('update.html', product = products[0])
    
    def update(self, product_id):
        name =request.form['name']
        description = request.form['description']
        price = request.form['price']
        self.models['Product'].update_product(name, description, price, product_id)
        return redirect('/')
    
    def destroy(self, product_id):
        self.models['Product'].delete_product(product_id)
        return redirect('/')
        