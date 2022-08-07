import uvicorn


def main():
    uvicorn.run(
        'workshop.app:app',
        reload=True
    )


if __name__ == '__main__':
    main()
