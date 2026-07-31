

from src.models import Expense, ExpenseCreate


class ExpenseStore:
    def __init__(self):
        self._expenses: dict[int, Expense] = {}
        self._next_id = 1

    def add(self, data: ExpenseCreate) -> Expense:
        expense = Expense(id=self._next_id, **data.model_dump())
        self._expenses[expense.id] = expense
        self._next_id += 1
        return expense

    def get_all(self, category: str | None = None) -> list[Expense]:
        items = list(self._expenses.values())
        if category:
            items = [e for e in items if e.category.lower() == category.lower()]
        return items

    def delete(self, expense_id: int) -> bool:
        """Returns True if something was deleted, False if id didn't exist."""
        if expense_id in self._expenses:
            del self._expenses[expense_id]
            return True
        return False

    def totals(self) -> tuple[float, dict[str, float]]:
        overall = 0.0
        by_category: dict[str, float] = {}
        for e in self._expenses.values():
            overall += e.amount
            by_category[e.category] = by_category.get(e.category, 0.0) + e.amount
        return round(overall, 2), {k: round(v, 2) for k, v in by_category.items()}