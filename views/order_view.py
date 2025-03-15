import click
from database import SessionLocal
from controllers.order_controller import OrderController

@click.group()
def order_cli():
    """Commands for managing orders."""
    pass

@order_cli.command()
@click.option("--user-id", prompt="User ID", type=int)
@click.option("--product-quantities", prompt="Product Quantities (e.g., 1:2,2:3)", type=str)
def create_order(user_id, product_quantities):
    """Create a new order."""
    try:
        # Parse product quantities
        product_quantities_dict = {}
        for item in product_quantities.split(","):
            product_id, quantity = item.split(":")
            product_quantities_dict[int(product_id)] = int(quantity)

        # Create the order
        db = SessionLocal()
        order = OrderController.create_order(db, user_id, product_quantities_dict)
        click.echo(f"Created order: {order}")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

@order_cli.command()
def list_orders():
    """List all orders."""
    db = SessionLocal()
    orders = OrderController.get_all_orders(db)
    if not orders:
        click.echo("No orders found.")
        return

    for order in orders:
        click.echo(order)

@order_cli.command()
@click.option("--id", prompt="Order ID", type=int)
def delete_order(id):
    """Delete an order by ID."""
    db = SessionLocal()
    success = OrderController.delete_order(db, id)
    if success:
        click.echo(f"Deleted order with ID {id}")
    else:
        click.echo("Order not found.")