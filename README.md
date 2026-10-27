# Макет шаблонов для портфолио программиста

Шаблон главной страницы портфолио Python / Django разработчика (чистый HTML + CSS, без внешних зависимостей, светлая/тёмная тема, адаптивная вёрстка).

## Структура

```
templates/portfolio/index.html   # Django-шаблон главной страницы
static/css/style.css             # стили
```

## Как подключить к Django-проекту

1. Скопируйте `templates/portfolio/index.html` в папку шаблонов вашего приложения (например, `portfolio/templates/portfolio/index.html`), а `static/css/style.css` — в папку статики (`portfolio/static/css/style.css`).
2. Убедитесь, что `django.contrib.staticfiles` есть в `INSTALLED_APPS`.
3. Добавьте представление:

```python
# portfolio/views.py
from django.shortcuts import render

def index(request):
    context = {
        "name": "Ваше Имя",
        "title": "Python / Django разработчик",
        "email": "you@example.com",
        "github_url": "https://github.com/username",
        "telegram": "@username",
        "telegram_url": "https://t.me/username",
    }
    return render(request, "portfolio/index.html", context)
```

```python
# urls.py
from django.urls import path
from portfolio.views import index

urlpatterns = [path("", index, name="index")]
```

Все переменные необязательны — если их не передать, используются значения по умолчанию (`|default`). Тексты-заполнители в разделах «Обо мне», «Проекты» и «Опыт» замените своими.
