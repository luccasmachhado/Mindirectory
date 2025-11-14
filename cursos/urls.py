from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('usuario/', views.usuario_view, name='usuario'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:id>/', views.pagina_cursos, name='pagina_cursos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)