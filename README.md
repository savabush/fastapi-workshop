# fastapi-workshop
Сервис для учета личных расходов и доходов 

Основной фреймворк для бэкенда - FastAPI. Присутствует авторизация и аутентификация через JWT. Также доабвлена пагинация во избежание долгой подгрузки данных.
Возможность импортировать и экспортировать CSV файлы по операциям доходов и расходов.
Для работы необходима база данных на Ваш выбор, я использовал PostgreSQL.


Замените <b>.env.example</b> на <b>.env</b>. В нем необходимо добавить данные по айпи сервера, порту, URL на базу данных и ключ JWT.

Для запуска можно использовать Docker:

<p><code>docker build -t fastapi .</code></p>
<p><code>docker run --name fastapi -p 8008:80 fastapi</code></p>

Или командой:

<p><code>python main.py</code></p>
