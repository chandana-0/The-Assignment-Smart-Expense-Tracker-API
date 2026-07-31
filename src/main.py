
from fastapi import FastAPI, HTTPException, Query

from src.models import Expense, ExpenseCreate, TotalsResponse, CategoryTotal
from src.storage import ExpenseStore

app = FastAPI(
    title="Smart Expense Tracker API",
    description="A simple REST API for tracking personal expenses.",
    version="1.0.0",
)

store = ExpenseStore()


@app.post("/expenses", response_model=Expense, status_code=201)
def create_expense(expense: ExpenseCreate):
    """Add a new expense."""
    return store.add(expense)


@app.get("/expenses", response_model=list[Expense])
def list_expenses(category: str | None = Query(default=None, description="Filter by category")):
    """View all expenses, optionally filtered by category."""
    return store.get_all(category=category)


@app.get("/expenses/total", response_model=TotalsResponse)
def get_totals():
    """Overall total and totals broken down by category."""
    overall, by_category = store.totals()
    return TotalsResponse(
        overall_total=overall,
        by_category=[CategoryTotal(category=k, total=v) for k, v in by_category.items()],
    )


@app.delete("/expenses/{expense_id}", status_code=204)
def delete_expense(expense_id: int):
    """Delete an expense by id."""
    deleted = store.delete(expense_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Expense with id {expense_id} not found")
    return None
