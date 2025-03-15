import click

@click.group()
def cli():
    pass

@cli.command()
def menu():
    """Display the main menu."""
    click.echo("=== Inventory Management System ===")
    click.echo("1. Manage Products")
    click.echo("2. Manage Suppliers")
    click.echo("3. Manage Users")
    click.echo("4. Exit")