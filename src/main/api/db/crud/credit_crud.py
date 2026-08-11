from src.main.api.db.models.credit_table import Credit
from sqlalchemy.orm import Session

class CreditCrudDb:
    @staticmethod
    def get_credit_account_by_id(db: Session, account_id: int) -> Credit | None:
        return db.query(Credit).filter_by(id=account_id).first()

    @staticmethod
    def delete_account(db: Session, account_id: int) -> None:
         account =  db.query(Credit).filter_by(id=id).first()
         if account:
             db.delete(account)
             db.commit()