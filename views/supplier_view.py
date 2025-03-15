import click
from database import SessionLocal
from controllers.supplier_controller import SupplierController

@click.group()
def supplier_cli():
    """Commands for managing suppliers."""
    pass

@supplier_cli.command()
@click.option("--name", prompt="Supplier Name")
@click.option("--contact-info", prompt="Contact Info")
def add_supplier(name, contact_info):
    """Add a new supplier."""
    db = SessionLocal()
    supplier = SupplierController.create_supplier(db, name, contact_info)
    click.echo(f"Added supplier: {supplier}")

@supplier_cli.command()
def list_suppliers():
    """List all suppliers."""
    db = SessionLocal()
    suppliers = SupplierController.get_all_suppliers(db)
    for supplier in suppliers:
        click.echo(supplier)

@supplier_cli.command()
@click.option("--id", prompt="Supplier ID", type=int)
def delete_supplier(id):
    """Delete a supplier by ID."""
    db = SessionLocal()
    success = SupplierController.delete_supplier(db, id)
    if success:
        click.echo(f"Deleted supplier with ID {id}")
    else:
        click.echo("Supplier not found.")

@supplier_cli.command()
def generate_supplier_report():
    """Generate a supplier report."""
    db = SessionLocal()
    report = SupplierController.generate_supplier_report(db)
    if not report:
        click.echo("No suppliers found.")
        return

    click.echo("\n=== Supplier Report ===")
    for item in report:
        click.echo(f"ID: {item['id']}, Name: {item['name']}, Contact: {item['contact_info']}, "
                   f"Products Supplied: {item['product_count']}")
    click.echo("=======================\n")