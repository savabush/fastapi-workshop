from fastapi import FastAPI
from api import router

tags_metadata = [
    {
        'name': 'auth',
        'description': 'Авторизация и регистрация'
    },
    {
        'name': 'operations',
        'description': 'Все об операциях по доходам и расходам'
    },
    {
        'name': 'reports',
        'description': 'Импорт и экспорт CSV файлов'
    },
]

app = FastAPI(
    title='Workshop',
    description='Сервис для учета личных расходов и доходов',
    version='1.0',
    openapi_tags=tags_metadata
)
app.include_router(router)
