# IMS 
This is a Python CLI application that uses SQLAlchemy for ORM to manage an inventory system. Users can interact with the database through commands to create, delete, view, and search products, suppliers, users, and orders. The system also includes reporting features.
## Features
- Add,delete and view products ,suppliers an users
- cerate and manage orders
- generate reports 
## setup
1. clone the repo
```bash
git clone https://github.com/happiness-prog/IMS-PROJECT
cd inventory_managment_system
```
2. install dependancies 
```bash
pip install
pipenv shell
```
3. run the application 
```bash 
python main.py menu 
```

## usage 
1. add user 
```bash 
python main.py supplier add-supplier --name=''
```
2. add product 
```bash 
python main.py product add-product --name''
```
3. create an order 
```bash 
python main.py order create-order --user-id= ....
```
4. generate reports
```bash 
python main.py supplier generate-supplier-report
```

## dependancies
- CLICK
- SQLALCHEMY
- ALEMBIC

## LICENSE 
 MIT license.
 