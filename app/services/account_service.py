from app.models.account import Account
from app.repository.account_repository import AccountRepository


class AccountService(object):
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def get_account_by_id(self, account_id: int) -> Account | None:
        """
        Get account by ID
        """
        return self.account_repository.get_by_id(account_id)

    def transfer_money(self, from_account_id: int, to_account_id: int, amount: int) -> None:
        """
        Transfer money from one account to another within a single transaction
        """
        with self.account_repository.session.begin():
            self.account_repository.withdraw_money(from_account_id, amount)
            self.account_repository.deposit_money(to_account_id, amount)

    def withdraw_money(self, account_id: int, amount: int) -> None:
        """
        Withdraw money from an account
        """
        with self.account_repository.session.begin():
            self.account_repository.withdraw_money(account_id, amount)

    def deposit_money(self, account_id: int, amount: int) -> None:
        """
        Deposit money into an account
        """
        with self.account_repository.session.begin():
            self.account_repository.deposit_money(account_id, amount)
