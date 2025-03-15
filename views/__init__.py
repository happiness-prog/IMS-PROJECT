from .main_menu import cli
from .product_view import product_cli
from .supplier_view import supplier_cli
from .user_view import user_cli
from .order_view import order_cli

__all__ = ["cli", "product_cli", "supplier_cli", "user_cli", "order_cli"]