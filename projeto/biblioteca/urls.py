# biblioteca/urls.py
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, LivroViewSet, EmprestimoViewSet

router = DefaultRouter()
router.register(r'users', UsuarioViewSet, basename='usuario')
router.register(r'livros', LivroViewSet, basename='livro')
router.register(r'emprestimos', EmprestimoViewSet, basename='emprestimo')

urlpatterns = router.urls
