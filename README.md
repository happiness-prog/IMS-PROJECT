# Inventory Management System

A command-line application for managing inventory, suppliers, orders, and users.

## Features

- **Product Management:** Add, edit, delete, and view products
- **Supplier Management:** Add, edit, delete, and view suppliers

- **Stock Management:** Track stock levels and get restock alerts
- **Reporting:** Generate reports on sales, inventory, and suppliers

## Setup Instructions

1. Create a virtual environment:
   ``` bash 
   pipenv shell
   ```


2. Run the application:
   ```
   python main.py
   ```

## Usage

Follow the interactive menu prompts to navigate through the different features of the system:

1. **Products:** Manage your product inventory
2. **Suppliers:** Manage your suppliers
3. **Orders:** Create and manage customer orders
4. **Users:** Manage system users
5. **Reports:** Generate various reports
6. **Exit:** Quit the application

## Models

- **Product:** Represents inventory items with name, description, price, quantity, and related supplier
- **Supplier:** Represents vendors who supply products
- **Order:** Represents customer purchases
- **OrderItem:** Individual items within an order
- **User:** System users with different roles

## Dependencies

- click: Command line interface creation
- SQLAlchemy: ORM for database management
- tabulate: Formatted table output



python main.py product-cli generate-stock-report
