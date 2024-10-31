SECRET_KEY="key",
ROOT_URLCONF="",
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "demo_app"
]
MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "sql-inspector-tool.middleware.sql_middleware",
)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}
USE_TZ = False