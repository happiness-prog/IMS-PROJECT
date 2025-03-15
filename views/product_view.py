import click
from database import SessionLocal
from controllers.product_controller import ProductController

@click.group()
def product_cli():
    """Commands for managing products."""
    pass

@product_cli.command()
@click.option("--name", prompt="Product Name")
@click.option("--quantity", prompt="Quantity", type=int)
@click.option("--supplier-id", prompt="Supplier ID", type=int)
def add_product(name, quantity, supplier_id):
    """Add a new product."""
    db = SessionLocal()
    product = ProductController.create_product(db, name, quantity, supplier_id)
    click.echo(f"Added product: {product}")

@product_cli.command()
def list_products():
    """List all products."""
    db = SessionLocal()
    products = ProductController.get_all_products(db)
    for product in products:
        click.echo(product)

@product_cli.command()
@click.option("--id", prompt="Product ID", type=int)
def delete_product(id):
    """Delete a product by ID."""
    db = SessionLocal()
    success = ProductController.delete_product(db, id)
    if success:
        click.echo(f"Deleted product with ID {id}")
    else:
        click.echo("Product not found.")

@product_cli.command()
def generate_stock_report():
    """Generate a stock summary report."""
    db = SessionLocal()
    report = ProductController.generate_stock_summary(db)
    if not report:
        click.echo("No products found.")
        return

    click.echo("\n=== Stock Summary Report ===")
    for item in report:
        click.echo(f"ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}, "
                   f"Status: {item['status']}, Supplier: {item['supplier']}")
    click.echo("============================\n")