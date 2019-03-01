from .article import (
    ArticleDetailView,
    ArticleListView,
    ArticleManageView,
    ArticleDeleteView
)
from .main import home_redirect
from .prof import ProfView
from .student import StudentView
from .user import RegistrationView

__all__ =  [
    'ArticleDetailView',
    'ArticleListView',
    'ArticleManageView',
    'ArticleDeleteView',
    'home_redirect',
    'ProfView',
    'StudentView',
    'RegistrationView'
]