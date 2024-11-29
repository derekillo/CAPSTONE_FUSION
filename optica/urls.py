from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from optica import views
# from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static
from django.conf import settings
from .views import CrearAbonoView, CrearCertificadoView

from django.views.generic import TemplateView
router = routers.DefaultRouter()
#router.register(r'cliente', views.ClienteView, 'Cliente')
# router.register(r'atendedor', views.AtendedorView, 'Atendedor')
# router.register(r'tecnico', views.TecnicoView, 'Tecnico')
# router.register(r'receta', views.RecetaView, 'Receta')
# router.register(r'abono', views.AbonoView, 'Abono')
# router.register(r'ordentrabajo', views.OrdenTrabajoView, 'Orden de Trabajo')
# router.register(r'certificado', views.CertificadoView, 'Certificado')
# router.register(r'administrador', views.AdministradorView, 'Administrador')



urlpatterns = [
    #path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='Optica API')),
    
    path('', views.index, name='index'),
    path('cliente_list/', views.ListarClienteView.as_view(), name='cliente_list'),
    path('cliente_new/', views.CrearClienteView.as_view(), name='cliente_new'),    
    path('<int:pk>/cliente_edit/', views.EditarClienteView.as_view(), name='cliente_edit'),
    path('<int:pk>/cliente_delete/', views.EliminarClienteView.as_view(), name='cliente_delete'),
    
    
    path('receta_list', views.ListarRecetaView.as_view(), name='receta_list'),
    path('receta_new/', views.CrearRecetaView.as_view(), name='receta_new'),    
    path('<int:pk>/receta_edit/', views.EditarRecetaView.as_view(), name='receta_edit'),
    path('<int:pk>/receta_delete/', views.EliminarRecetaView.as_view(), name='receta_delete'),
    
    path('ordenTrabajo_list', views.ListarOrdenTrabajoView.as_view(), name='ordenTrabajo_list'),
    path('ordenTrabajo_new/', views.CrearOrdenTrabajoView.as_view(), name='ordenTrabajo_new'),    
    path('<int:pk>/ordenTrabajo_edit/', views.EditarOrdenTrabajoView.as_view(), name='ordenTrabajo_edit'),
    path('<int:pk>/ordenTrabajo_delete/', views.EliminarOrdenTrabajoView.as_view(), name='ordenTrabajo_delete'),
    
    path('abono/new/', CrearAbonoView.as_view(), name='abono_new'),
    
    path('abono_list', views.ListarAbonoView.as_view(), name='abono_list'),
    path('abono_new/', views.CrearAbonoView.as_view(), name='abono_new'),    
    path('<int:pk>/abono_edit/', views.EditarAbonoView.as_view(), name='abono_edit'),
    path('<int:pk>/abono_delete/', views.EliminarAbonoView.as_view(), name='abono_delete'),


    path('certificado_list', views.ListarCertificadoView.as_view(), name='certificado_list'),
    path('certificado_new/', views.CrearCertificadoView.as_view(), name='certificado_new'),    
    # path('<int:pk>/certificado_edit/', views.EditarCertificadoView.as_view(), name='certificado_edit'),
    path('<int:pk>/certificado_delete/', views.EliminarCertificadoView.as_view(), name='certificado_delete'),
    path('certificado/new/', CrearCertificadoView.as_view(), name='certificado_new'),
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)