# Макет шаблонов для портфолио программиста

Шаблон главной страницы портфолио Python / Django разработчика (чистый HTML + CSS, без внешних зависимостей, светлая/тёмная тема, адаптивная вёрстка).

## Структура

```
manage.py                        # управляющий скрипт Django
requirements.txt                 # зависимости (Django)
config/                          # пакет проекта: settings.py, urls.py, wsgi.py, asgi.py
portfolio/                       # приложение: views.py (IndexView), urls.py, apps.py
templates/portfolio/index.html   # Django-шаблон главной страницы
static/css/style.css             # стили (общие для Django и GitHub Pages)
index.html, .nojekyll            # статическая копия страницы для GitHub Pages
```

## Запуск Django-проекта локально

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Откройте http://127.0.0.1:8000/ — главная страница рендерится из `templates/portfolio/index.html`, стили отдаются из `static/css/style.css`.

Данные на странице (имя, должность, контакты) задаются в `portfolio/views.py` (`IndexView.get_context_data`). Все переменные шаблона необязательны — если их не передать, используются значения по умолчанию (`|default`). Тексты-заполнители в разделах «Обо мне», «Проекты» и «Опыт» замените своими в шаблоне.

### Переменные окружения

| Переменная             | Назначение                                   | По умолчанию                 |
|------------------------|----------------------------------------------|------------------------------|
| `DJANGO_SECRET_KEY`    | секретный ключ                               | небезопасный ключ для разработки |
| `DJANGO_DEBUG`         | режим отладки (`True`/`False`)               | `True`                       |
| `DJANGO_ALLOWED_HOSTS` | список хостов через запятую                  | `localhost,127.0.0.1`        |

Для продакшена обязательно задайте свой `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False` и `DJANGO_ALLOWED_HOSTS`, затем выполните `python manage.py collectstatic`.

## GitHub Pages

Статическая версия страницы для GitHub Pages — файл `index.html` в корне репозитория (копия шаблона, где Django-теги заменены значениями по умолчанию; стили подключаются из `static/css/style.css`). Она не зависит от Django и публикуется как есть. Если меняете `templates/portfolio/index.html`, при необходимости перенесите правки и в корневой `index.html`.

Живая версия: https://leshashirokov.github.io/-/
