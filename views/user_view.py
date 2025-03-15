import click
from database import SessionLocal
from controllers.user_controller import UserController

@click.group()
def user_cli():
    """Commands for managing users."""
    pass

@user_cli.command()
@click.option("--username", prompt="Username")
@click.option("--email", prompt="Email")
def add_user(username, email):
    """Add a new user."""
    db = SessionLocal()
    user = UserController.create_user(db, username, email)
    click.echo(f"Added user: {user}")

@user_cli.command()
def list_users():
    """List all users."""
    db = SessionLocal()
    users = UserController.get_all_users(db)
    for user in users:
        click.echo(user)

@user_cli.command()
@click.option("--id", prompt="User ID", type=int)
def delete_user(id):
    """Delete a user by ID."""
    db = SessionLocal()
    success = UserController.delete_user(db, id)
    if success:
        click.echo(f"Deleted user with ID {id}")
    else:
        click.echo("User not found.")