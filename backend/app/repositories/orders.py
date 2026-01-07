"""
Repository to handle orders table.
"""
from sqlalchemy.orm import Session

from app.models.orders import Orders


class OrdersRepository:
    """
    Repository for Orders database operations.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all_orders(self) -> list[Orders]:
        """
        Get all orders in the database.

        Returns:
            list[Orders]: All orders from the database.
        """
        return self.db.query(Orders).all()


