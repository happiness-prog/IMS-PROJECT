from sqlalchemy.orm import Session
from models import Supplier

class SupplierController:
    @staticmethod
    def create_supplier(db: Session, name: str, contact_info: str):
        supplier = Supplier(name=name, contact_info=contact_info)
        db.add(supplier)
        db.commit()
        db.refresh(supplier)
        return supplier

    @staticmethod
    def get_all_suppliers(db: Session):
        return db.query(Supplier).all()

    @staticmethod
    def get_supplier_by_id(db: Session, supplier_id: int):
        return db.query(Supplier).filter(Supplier.id == supplier_id).first()

    @staticmethod
    def delete_supplier(db: Session, supplier_id: int):
        supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
        if supplier:
            db.delete(supplier)
            db.commit()
            return True
        return False

    @staticmethod
    def generate_supplier_report(db: Session):
        """Generate a report of suppliers and their products."""
        suppliers = db.query(Supplier).all()
        report = []
        for supplier in suppliers:
            report.append({
                "id": supplier.id,
                "name": supplier.name,
                "contact_info": supplier.contact_info,
                "product_count": len(supplier.products)
            })
        return report