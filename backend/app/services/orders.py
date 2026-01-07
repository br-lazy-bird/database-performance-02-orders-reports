"""
Services related to orders.
"""

import time
from sqlalchemy.orm import Session
from decimal import Decimal

from app.repositories.orders import OrdersRepository
from app.core.database import get_query_count, reset_query_count

class OrdersService:
    """
    Service for orders related API.
    """

    def __init__(self, db: Session):
        self.db = db
        self.orders_repository = OrdersRepository(db)
        
    def get_all_orders(self):
        reset_query_count()
        start_time = time.time()
        all_orders = self.orders_repository.get_all_orders()
        response = {}
        response["report"] = []
        for order in all_orders:
            single_order = {}
            single_order["order_id"] = order.id
            single_order["customer_name"] = order.customer.name
            single_order["item_count"] = len(order.items)
            single_order["order_date"] = order.order_date
            single_order["status"] = order.status
            total = Decimal("0.0")
            for item in order.items:
                total += item.unit_price * item.quantity
            single_order["total"] = total
            response["report"].append(single_order)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        response["metadata"] = {
            "total_orders" : len(response["report"]),
            "execution_time_ms": round(duration, 2),
            "query_count" : get_query_count(),
        }
        return response
        

