
from datetime import date as date_type
from pydantic import BaseModel, Field


class ExpenseCreate(BaseModel):
    """What the client sends us when creating a new expense.

    Notice there's no 'id' here — the server assigns that, not the client.
    """
    title: str = Field(..., min_length=1, description="Short description, e.g. 'Groceries'")
    amount: float = Field(..., gt=0, description="Must be a positive number")
    category: str = Field(..., min_length=1, description="e.g. 'food', 'travel'")
    date: date_type = Field(..., description="Format: YYYY-MM-DD")


class Expense(ExpenseCreate):
    """What we store and return: same fields as ExpenseCreate, plus an id."""
    id: int


class CategoryTotal(BaseModel):
    category: str
    total: float


class TotalsResponse(BaseModel):
    overall_total: float
    by_category: list[CategoryTotal]
