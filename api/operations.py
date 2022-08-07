from fastapi import APIRouter, Depends, Response, status
from typing import List, Optional
from services.operations import OperationService
from services.auth import get_current_user
from models.operations import OperationKind, OperationCreate, OperationUpdate, Operation
from models.auth import User


router = APIRouter(
    prefix='/operations',
    tags=['operations']
)


@router.get('/', response_model=List[Operation])
def get_operations(
        user: User = Depends(get_current_user),
        kind: Optional[OperationKind] = None,
        page: int = 1,
        service: OperationService = Depends()
        ):
    return service.get_list(kind=kind, user_id=user.id, page=page)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(
        operation_id: int,
        user: User = Depends(get_current_user),
        service: OperationService = Depends()
        ):
    return service.get_by_id(user.id, operation_id)


@router.post('/', response_model=Operation)
def create_operation(
        operation_data: OperationCreate,
        user: User = Depends(get_current_user),
        service: OperationService = Depends(),
):
    return service.create(user.id, operation_data)


@router.put('/{operation_id}', response_model=Operation)
def update_operation(
        operation_id: int,
        operation_data: OperationUpdate,
        user: User = Depends(get_current_user),
        service: OperationService = Depends(),
):
    return service.update(operation_id=operation_id, operation_data=operation_data, user_id=user.id)


@router.delete('/{operation_id}', response_model=Operation)
def update_operation(
        operation_id: int,
        user: User = Depends(get_current_user),
        service: OperationService = Depends(),
):
    service.delete(operation_id=operation_id, user_id=user.id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

