from decimal import Decimal
from typing import Optional, Annotated, AnyStr

from pydantic import BaseModel, AfterValidator


def validate_tax(value: AnyStr):
    """Validate the tax value."""
    if value is None or value == "" or value == "None":
        return Decimal("0.0")
    return Decimal(value)


Tax = Annotated[Decimal, AfterValidator(validate_tax)]


class SmallBoxRecordSchema(BaseModel):
    """Small box record schema."""

    code: Optional[str] = None
    national_id: Optional[str] = None
    verification_digit: Optional[str] = None
    name: str
    invoice: Optional[str] = None
    date: str
    amount: Decimal
    tax: Optional[Tax] = Decimal("0.0")
    total: Decimal
    description: str
    source_file: Optional[str] = None
    source_sheet: Optional[str] = None
