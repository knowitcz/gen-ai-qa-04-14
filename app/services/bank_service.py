import abc

from app.services.account_service import AccountService
from app.validator.amount_validator import AmountValidator


class BankService(abc.ABC):
    @abc.abstractmethod
    def deposit_money_at_atm(self, account_id: int, amount: int) -> None:
        """
        Deposit money at the ATM
        """
        ...

    @abc.abstractmethod
    def deposit_money_at_branch(self, account_id: int, amount: int) -> None:
        """
        Deposit money at the bank branch
        """
        ...

    @abc.abstractmethod
    def make_transfer_at_branch(self, from_account_id: int, to_account_id: int, amount: int) -> None:
        """
        Make a transfer at the bank branch
        """
        ...

    @abc.abstractmethod
    def withdraw_money_at_atm(self, account_id: int, amount: int) -> None:
        """
        Withdraw money at the ATM
        """
        ...

    @abc.abstractmethod
    def withdraw_money_at_branch(self, account_id: int, amount: int) -> None:
        """
        Withdraw money at the bank branch
        """
        ...

class BranchBankService(BankService):
    def __init__(self, account_service: AccountService):
        self.account_service = account_service

    def deposit_money_at_atm(self, account_id: int, amount: int) -> None:
        """
        Deposit money at the ATM
        """
        raise NotImplementedError("ATM deposits are not supported by BranchBankService.")

    def deposit_money_at_branch(self, account_id: int, amount: int) -> None:
        """
        Deposit money at the bank branch
        """
        self.account_service.deposit_money(account_id, amount)

    def make_transfer_at_branch(self, from_account_id: int, to_account_id: int, amount: int) -> None:
        """
        Make a transfer at the bank branch
        """
        self.account_service.transfer_money(from_account_id, to_account_id, amount)

    def withdraw_money_at_atm(self, account_id: int, amount: int) -> None:
        """
        Withdraw money at the ATM
        """
        raise NotImplementedError("ATM withdrawals are not supported by BranchBankService.")

    def withdraw_money_at_branch(self, account_id: int, amount: int) -> None:
        """
        Withdraw money at the bank branch
        """
        self.account_service.withdraw_money(account_id, amount)

class AtmBankService(BankService):
    def __init__(self, account_service: AccountService, amount_validator: AmountValidator):
        self.account_service = account_service
        self.amount_validator = amount_validator

    def deposit_money_at_atm(self, account_id: int, amount: int) -> None:
        """
        Deposit money at the ATM
        """
        self.amount_validator(amount).raise_if_error()
        self.account_service.deposit_money(account_id, amount)

    def deposit_money_at_branch(self, account_id: int, amount: int) -> None:
        """
        Deposit money at the bank branch
        """
        raise NotImplementedError("Branch deposits are not supported by AtmBankBankService.")

    def make_transfer_at_branch(self, from_account_id: int, to_account_id: int, amount: int) -> None:
        """
        Make a transfer at the bank branch
        """
        raise NotImplementedError("Branch transfers are not supported by AtmBankBankService.")

    def withdraw_money_at_atm(self, account_id: int, amount: int) -> None:
        """
        Withdraw money at the ATM
        """
        self.amount_validator(amount).raise_if_error()
        self.account_service.withdraw_money(account_id, amount)

    def withdraw_money_at_branch(self, account_id: int, amount: int) -> None:
        """
        Withdraw money at the bank branch
        """
        raise NotImplementedError("Branch withdrawals are not supported by AtmBankBankService.")