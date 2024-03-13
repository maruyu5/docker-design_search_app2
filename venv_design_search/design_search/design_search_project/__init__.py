from .settings import *                  # settings.py(本番環境用)をimport

try:
    from .settings_dev import *      # settings_dev.pyが存在しないか、その他のエラーが発生した場合は、settings_dev.py(開発環境用)をimport
except:
    pass
