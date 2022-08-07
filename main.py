import uvicorn
from settings.settings import settings


def main():
    uvicorn.run(
        'workshop.app:app',
        reload=True,
        host=settings.server_host,
        port=settings.server_port
    )


if __name__ == '__main__':
    main()
