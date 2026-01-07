"""
Repository to handle orders table.
"""
from typing import List
from sqlalchemy.orm import Session, joinedload, selectinload
from app.models.orders import Orders


class OrdersRepository:
    """
    Repository for Orders database operations.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all_orders(self) -> List[Orders]:
        """
        Get all orders in the database.
        """
        return self.db.query(Orders).all()


