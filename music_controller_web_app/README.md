PS F:\DEV\React-Django> django-admin startproject music_controller_web_app
PS F:\DEV\React-Django> cd .\music_controller_web_app\
PS F:\DEV\React-Django\music_controller_web_app> django-admin startapp api   

Recommended Configuration for Django + Ruff + Pylance
Add this to your settings.json (Workspace or User):

{
    // 1. Use Ruff as formatter
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll.ruff": "explicit",
            "source.organizeImports.ruff": "explicit"
        }
    },

    // 2. Keep Pylance for intelligent features (especially auto-imports)
    "python.analysis.autoImportCompletions": true,
    "python.analysis.indexing": true,
    "python.analysis.autoImportUserSymbols": true,

    // 3. Disable Pylance linting to avoid duplicate warnings
    "python.analysis.diagnosticMode": "workspace",
    "python.analysis.ignore": ["**/*"],   // or just specific folders if needed

    // 4. Django-specific improvements for Pylance
    "python.analysis.packageIndexDepths": [
        {
            "name": "django",
            "depth": 10,
            "includeAllSymbols": true
        },
        {
            "name": "rest_framework",
            "depth": 10,
            "includeAllSymbols": true
        }
    ]
}

python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py runserver