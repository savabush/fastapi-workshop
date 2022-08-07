from fastapi import FastAPI
from api import router

tags_metadata = [
    {
        'name': 'auth',
        'descrpition': 'Авторизация и регистрация'
    },
    {
        'name': 'operations',
        'descrpition': 'Все об операциях по доходам и расходам'
    },
    {
        'name': 'reports',
        'descrpition': 'Импорт и экспорт CSV файлов'
    },
]

app = FastAPI(
    title='Workshop',
    description='Сервис для учета личных расходов и доходов',
    version='1.0'
)
app.include_router(router)
