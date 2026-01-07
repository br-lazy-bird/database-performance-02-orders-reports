"""
Order related APIs
"""
import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.core.database import get_db
from app.services.orders import OrdersService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/orders", tags = ["orders"])

@router.get("/report")
def get_all_orders(db: Session = Depends(get_db)):
    """
    Returns: 
        List of all orders in the database along with some metadata related to the 
        queries fetching. 

    Raises: 
        HTTPException: 500 if database error occurs
    """
    try:
        orders_service = OrdersService(db)
        all_orders = orders_service.get_all_orders()
        return all_orders
    except SQLAlchemyError as e:
        logger.error("Database error in GET orders/report: %s}", str(e))
        raise HTTPException(
            status_code=500,
            detail="Database error occurred during all orders report fetching",
        ) from e
    except Exception as e:
        logger.error("Unexpected error in GET orders/report : %s", str(e))
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred during all orders report fetching",
        ) from e



    