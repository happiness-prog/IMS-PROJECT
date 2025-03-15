import click
from views import cli, product_cli, supplier_cli, user_cli, order_cli
from database import init_db

if __name__ == "__main__":
    init_db()  # Initialize the database
    cli.add_command(product_cli)  # Register product commands
    cli.add_command(supplier_cli)  # Register supplier commands
    cli.add_command(user_cli)      # Register user commands
    cli.add_command(order_cli)     # Register order commands
    cli()