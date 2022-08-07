from fastapi import APIRouter, Depends
from models.operations import Operation
from typing import List, Optional
from services.operations import OperationService
from models.operations import OperationKind


router = APIRouter(
    prefix='/operations'
)


@router.get('/', response_model=List[Operation])
def get_operations(
        kind: Optional[OperationKind] = None,
        service: OperationService = Depends()
        ):
    return service.get_list(kind=kind)

