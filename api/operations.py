from fastapi import APIRouter, Depends
from models.operations import Operation
from typing import List
from services.operations import OperationService


router = APIRouter(
    prefix='/operations'
)


@router.get('/', response_model=List[Operation])
def get_operations(service: OperationService = Depends()):
    return service.get_list()
