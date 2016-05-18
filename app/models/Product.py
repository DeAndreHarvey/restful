""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()
        
    def get_products(self):
        query = "SELECT * from Products"
        return self.db.query_db(query)
    
    def add_product(self, name, description, price):
        if not price.isdigit():
            return False
        else:
            sql = "INSERT INTO Products (name, description, price, created_at) Values(:name, :description, :price, NOW())"
            data ={
                'name':name,
                'description':description,
                'price':price
            }
            self.db.query_db(sql, data)
            return True
        
        
    def update_product(self, name, description, price, product_id):
        sql = "UPDATE Products SET name=:name, description = :description, price =:price, updated_at =NOW() where id = :id"
        data ={
            'name':name,
            'description':description,
            'price':price,
            'id':product_id
        }
        self.db.query_db(sql, data)
        return True    
        
    def delete_product(self, product_id):
        query = "DELETE FROM products WHERE id = :product_id"
        data = { "product_id": product_id }
        self.db.query_db(query, data)
        return True
    
    def get_product_by_id(self, product_id):
        query = "SELECT * FROM products WHERE id = :product_id"
        data = { 'product_id': product_id}
        return self.db.query_db(query, data)