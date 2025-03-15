from sqlalchemy.orm import Session
from models import Product

class ProductController:
    @staticmethod
    def create_product(db: Session, name: str, quantity: int, supplier_id: int):
        product = Product(name=name, quantity=quantity, supplier_id=supplier_id)
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def get_all_products(db: Session):
        return db.query(Product).all()

    @staticmethod
    def get_product_by_id(db: Session, product_id: int):
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def delete_product(db: Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            db.delete(product)
            db.commit()
            return True
        return False

    @staticmethod
    def generate_stock_summary(db: Session):
        """Generate a summary of product stock levels."""
        products = db.query(Product).all()
        report = []
        for product in products:
            status = "In Stock" if product.is_in_stock else "Out of Stock"
            report.append({
                "id": product.id,
                "name": product.name,
                "quantity": product.quantity,
                "status": status,
                "supplier": product.supplier.name if product.supplier else "No Supplier"
            })
        return report