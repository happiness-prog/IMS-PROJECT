from sqlalchemy.orm import Session
from database import engine
from models import User, Supplier, Product, Order, OrderDetail

# Create a session
session = Session(bind=engine)

# Insert Users
users = [
    User(username="Happiness", email="happiness@example.com"),
    User(username="Maina", email="maina@example.com"),
    User(username="Ness", email="ness@example.com"),
    User(username="Nick", email="nick@example.com"),
]
session.add_all(users)

# Insert Suppliers
suppliers = [
    Supplier(name="BookHaven Distributors", contact_info="support@bookhaven.com"),
    Supplier(name="CozyNest Essentials", contact_info="contact@cozynest.com"),
    Supplier(name="TechNest Supplies", contact_info="sales@technest.com"),
    Supplier(name="Vintage Cellars", contact_info="info@vintagecellars.com"),
]
session.add_all(suppliers)

# Insert Products
products = [
    Product(name="Twisted Love - Ana Huang", quantity=12, supplier_id=1),
    Product(name="Haunting Adeline - H.D. Carlton", quantity=8, supplier_id=1),
    Product(name="Corrupt - Penelope Douglas", quantity=10, supplier_id=1),
    Product(name="Kindle Paperwhite", quantity=7, supplier_id=3),
    Product(name="Luxury Duvet Cover", quantity=6, supplier_id=2),
    Product(name="Bean Bag Chair", quantity=4, supplier_id=2),
    Product(name="House Slippers", quantity=15, supplier_id=2),
    Product(name="Chateau Margaux 2015", quantity=2, supplier_id=4),
    Product(name="MacBook Pro 16-inch", quantity=3, supplier_id=3),
]
session.add_all(products)
session.commit()  # Commit products so we can reference them in orders

# Insert Orders
orders = [
    Order(user_id=1),  # Happiness
    Order(user_id=2),  # Maina
    Order(user_id=3),  # Ness
    Order(user_id=4),  # Nick
]
session.add_all(orders)
session.commit()  # Commit orders so we can reference them in order details

# Insert Order Details (Product Orders)
order_details = [
    OrderDetail(order_id=1, product_id=1, quantity=2),  # Happiness buys Twisted Love
    OrderDetail(order_id=1, product_id=4, quantity=1),  # Happiness buys a Kindle
    OrderDetail(order_id=2, product_id=2, quantity=1),  # Maina buys Haunting Adeline
    OrderDetail(order_id=2, product_id=5, quantity=2),  # Maina buys Luxury Duvet Cover
    OrderDetail(order_id=3, product_id=3, quantity=1),  # Ness buys Corrupt
    OrderDetail(order_id=3, product_id=7, quantity=3),  # Ness buys House Slippers
    OrderDetail(order_id=4, product_id=8, quantity=1),  # Nick buys Chateau Margaux
    OrderDetail(order_id=4, product_id=9, quantity=1),  # Nick buys MacBook Pro
]
session.add_all(order_details)

# Commit all changes
session.commit()
session.close()
