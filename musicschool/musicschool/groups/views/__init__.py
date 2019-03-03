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
from .category import (
    CategoryListView,
    CategoryManageView,
    CategoryDeleteView
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
    'CategoryListView',
    'CategoryManageView',
    'CategoryDeleteView',
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