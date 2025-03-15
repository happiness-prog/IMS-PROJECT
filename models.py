from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

    products = relationship("Product", back_populates="supplier")

    def __repr__(self):
        return f"<Supplier(id={self.id}, name={self.name})>"

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, default=0)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

    supplier = relationship("Supplier", back_populates="products")
    order_details = relationship("OrderDetail", back_populates="product")

    @property
    def is_in_stock(self):
        return self.quantity > 0

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, quantity={self.quantity})>"

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    order_date = Column(DateTime, default=datetime.utcnow)
    total_amount = Column(Float, default=0.0)

    user = relationship("User", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")

    def __repr__(self):
        return f"<Order(id={self.id}, user_id={self.user_id}, total_amount={self.total_amount})>"

class OrderDetail(Base):
    __tablename__ = 'order_details'
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, default=1)
    price = Column(Float, default=0.0)

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product", back_populates="order_details")

    def __repr__(self):
        return f"<OrderDetail(id={self.id}, order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity})>"