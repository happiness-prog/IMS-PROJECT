from sqlalchemy.orm import Session
from models import Order, OrderDetail, Product, User
from datetime import datetime

class OrderController:
    @staticmethod
    def create_order(db: Session, user_id: int, product_quantities: dict):
        """Create a new order."""
        # Validate user exists
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError(f"User with ID {user_id} does not exist.")

        # Fetch all products and validate stock
        total_amount = 0.0
        order_details = []
        product_ids = list(product_quantities.keys())
        products = db.query(Product).filter(Product.id.in_(product_ids)).all()

        for product in products:
            quantity = product_quantities.get(product.id, 0)
            if product.quantity < quantity:
                raise ValueError(f"Insufficient stock for product ID {product.id}")
            total_amount += product.price * quantity
            order_details.append({"product_id": product.id, "quantity": quantity, "price": product.price})

        # Ensure all requested products were found
        if len(products) != len(product_ids):
            missing_ids = set(product_ids) - {p.id for p in products}
            raise ValueError(f"Invalid product IDs: {missing_ids}")

        try:
            # Create the order
            order = Order(user_id=user_id, order_date=datetime.utcnow(), total_amount=total_amount)
            db.add(order)
            db.commit()

            # Add order details and update product quantities
            for detail in order_details:
                order_detail = OrderDetail(
                    order_id=order.id,
                    product_id=detail["product_id"],
                    quantity=detail["quantity"],
                    price=detail["price"]
                )
                db.add(order_detail)

                # Update product stock
                product = db.query(Product).filter(Product.id == detail["product_id"]).first()
                product.quantity -= detail["quantity"]

            db.commit()
            db.refresh(order)
            return order

        except Exception as e:
            # Rollback in case of error
            db.rollback()
            raise ValueError(f"Failed to create order: {str(e)}")

    @staticmethod
    def get_all_orders(db: Session):
        """Retrieve all orders."""
        return db.query(Order).all()

    @staticmethod
    def get_order_by_id(db: Session, order_id: int):
        """Retrieve an order by its ID."""
        return db.query(Order).filter(Order.id == order_id).first()

    @staticmethod
    def delete_order(db: Session, order_id: int):
        """Delete an order by its ID."""
        order = db.query(Order).filter(Order.id == order_id).first()
        if order:
            db.delete(order)
            db.commit()
            return True
        return False