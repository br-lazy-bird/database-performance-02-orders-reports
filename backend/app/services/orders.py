"""
Services related to orders.
"""

import time
from typing import Any

from sqlalchemy.orm import Session

from app.repositories.orders import OrdersRepository
from app.core.database import get_query_count, reset_query_count

class OrdersService:
    """
    Service for orders related API.
    """

    def __init__(self, db: Session):
        self.db = db
        self.orders_repository = OrdersRepository(db)
        
    def get_all_orders(self) -> dict[str, Any]:
        """Get all orders with customer information and totals.

        Returns:
            dict containing report data and metadata (execution time, query count)
        """
        reset_query_count()
        start_time = time.time()
        orders = self.orders_repository.get_all_orders()

        report = [
            {
                "order_id": order.id,
                "customer_name": order.customer.name,
                "item_count": len(order.items),
                "order_date": order.order_date,
                "status": order.status,
                "total": sum(
                    item.unit_price * item.quantity
                    for item in order.items
                )
            }
            for order in orders
        ]

        end_time = time.time()
        duration_ms = (end_time - start_time) * 1000

        return {
            "report": report,
            "metadata": {
                "total_orders": len(report),
                "execution_time_ms": round(duration_ms, 2),
                "query_count": get_query_count(),
            }
        }
        

