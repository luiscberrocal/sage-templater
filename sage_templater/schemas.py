from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class SmallBoxRecordSchema(BaseModel):
    """Small box record schema."""
    code: str
    national_id: Optional[str] = None
    verification_digit: Optional[str] = None
    name: str
    invoice: str
    date: date
    amount: Decimal
    tax: Decimal
    total: Decimal
    description: str
