from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Главная страница портфолио."""

    template_name = "portfolio/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "name": "Ваше Имя",
                "title": "Python / Django разработчик",
                "tagline": (
                    "Создаю надёжные веб-приложения и API на Python и Django: "
                    "от проектирования базы данных до деплоя в продакшен."
                ),
                "email": "you@example.com",
                "github_url": "https://github.com/username",
                "telegram": "@username",
                "telegram_url": "https://t.me/username",
            }
        )
        return context
