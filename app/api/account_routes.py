from typing_extensions import Annotated
from app.db import get_session
from app.repository.account_repository import AccountRepository
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.models.account import Account
from app.services.account_service import AccountService

router = APIRouter()

def get_account_service(session: Annotated[Session, Depends(get_session)]) -> AccountService:
    repo = AccountRepository(session)
    return AccountService(repo)


@router.get("/account/{id}", response_model=Account)
def get_account(id: int,
                account_service: Annotated[AccountService, Depends(get_account_service)]):
    if account := account_service.get_account_by_id(id):
        return account
    raise HTTPException(status_code=404, detail="Account not found")

@router.post("/account/withdraw")
def withdraw_money(account_id: int, amount: int,
                   account_service: Annotated[AccountService, Depends(get_account_service)]):
    """
    Withdraw money from an account
    """
    try:
        account_service.withdraw_money(account_id, amount)
        return {"message": "Withdrawal successful"}
    except ValueError as e:
        raise HTTPException(status_code=400) from e
