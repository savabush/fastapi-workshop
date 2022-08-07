from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
from settings import tables
from settings.database import get_session
from models.operations import OperationKind, OperationCreate


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, kind: Optional[OperationKind] = None) -> List[tables.Operation]:
        query = self.session.query(tables.Operation)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()
        return operations

    def create(self, operation_data: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation
