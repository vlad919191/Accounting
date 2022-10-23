from src.__Parents.Repository import Repository
from .IExpenseRepo import IExpenseRepo
from .ExpenseModel import Expense
from flask import g


class ExpenseRepository(Repository, IExpenseRepo):
    expense: Expense = Expense

    def create(self, body: dict, client_id: int):
        expense = self.expense()
        expense.title = body['title']
        expense.description = body['description']
        expense.price = body['price']
        expense.colleague_id = body['colleague_id']
        expense.expense_type_id = body['expense_type_id']
        expense.firm_id = g.firm_id
        expense.paid = body['paid']
        expense.product_id = body['product_id']
        expense.client_id = client_id
        expense.save_db()

    def update(self, expense: Expense, body: dict):
        expense.title = body['title']
        expense.description = body['description']
        expense.price = body['price']
        expense.colleague_id = body['colleague_id']
        expense.expense_type_id = body['expense_type_id']
        expense.paid = body['paid']
        expense.update_db()

    def delete(self, expense: Expense):
        expense.delete_db()

    def get_by_id(self, expense_id: int) -> Expense:
        expense = self.expense.query.filter_by(id=expense_id, client_id=g.client_id)\
            .filter(self.expense.firm_id.in_(g.allowed_firm_ids)).first()

        if expense:
            expense.price = float(expense.price or "0.00")
            # expense.count = float(expense.count)

        return expense

    def get_by_product_id(self, product_id: int) -> Expense:
        expense = self.expense.query.filter_by(product_id=product_id).first()
        return expense

    def get_all(self, page: int, per_page: int, firm_id: int or None, paid: bool or None) -> dict:
        expenses = self.expense.query.filter_by(client_id=g.client_id)\
            .filter(self.expense.firm_id.in_(g.allowed_firm_ids))\
            .filter(self.expense.firm_id == firm_id if firm_id else self.expense.firm_id.isnot(None))\
            .filter(self.expense.paid == True if paid == True else self.expense.id.isnot(None),
                    self.expense.paid == False if paid == False else self.expense.id.isnot(None))\
            .order_by(-self.expense.creation_date)\
            .paginate(page=page, per_page=per_page)
        #
        # for expense in expenses.items:
        #     expense.price = float(expense.price)
        #     # expense.count = float(expense.count)

        return self.get_page_items(expenses)
