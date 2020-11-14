from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [


    # Nuevo Agregar
    path('',views.menu),

    # path('add_usuario', views.UsuarioCreate.as_view(), name="add_usuario"),

    path('list_usuarios/', views.UsuarioList.as_view(), name='list_usuarios'),

    path('edit_usuarios/<int:pk>', views.UsuarioUpdate.as_view(), name='edit_usuario'),

    path('del_usuarios/<int:pk>', views.UsuarioDelete.as_view(), name='del_usuarios'),

    #path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('registrar', views.RegistroUsuario.as_view(), name="registrar"),
]
