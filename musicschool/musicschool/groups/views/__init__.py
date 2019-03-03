from .article import (
    ArticleDetailView,
    ArticleListView,
    ArticleManageView,
    ArticleDeleteView
)
from .user import (
    UserListView,
    UserManageView,
    UserDeleteView
)
from .media import (
    MediaListView,
    MediaManageView,
    MediaDeleteView
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
    'MediaListView',
    'MediaManageView',
    'MediaDeleteView',
    'ProfView',
    'StudentView',
    'RegistrationView',
    'UserListView',
    'UserManageView',
    'UserDeleteView',

]