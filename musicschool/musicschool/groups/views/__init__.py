from .article import ArticleView
from .main import home_redirect
from .prof import ProfView
from .student import StudentView
from .user import RegistrationView

__all__ =  [
    'ArticleView',
    'home_redirect',
    'ProfView',
    'StudentView',
    'RegistrationView'
]