"""Module that provides endpoints."""
from django.urls import include, path
from garden_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'floras', views.FloraViewSet)
router.register(r'collect_places', views.CollectPlaceViewSet)
router.register(r'labels', views.LabelViewSet)
router.register(r'coords', views.CoordsViewSet)
router.register(r'taxons', views.TaxonViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'herbariums', views.HerbariumViewSet)

urlpatterns = [
    path('', views.home_page, name='homepage'),

    path('floras/', views.FloraListView.as_view(), name='floras'),
    path('flora/', views.flora_view, name='flora'),
    path('collect_places/', views.CollectPlaceListView.as_view(), name='collect_places'),
    path('collect_place/', views.collect_place_view, name='collect_place'),
    path('labels/', views.LabelListView.as_view(), name='labels'),
    path('label/', views.label_view, name='label'),
    path('coords/', views.CoordsListView.as_view(), name='coords'),
    path('coord/', views.coords_view, name='coord'),
    path('taxons/', views.TaxonListView.as_view(), name='taxons'),
    path('taxon/', views.taxon_view, name='taxon'),
    path('comments/', views.CommentListView.as_view(), name='comments'),
    path('comment/', views.comment_view, name='comment'),
    path('herbariums/', views.HerbariumListView.as_view(), name='herbariums'),
    path('herbarium/', views.herbarium_view, name='herbarium'),

    path('api/', include(router.urls), name='api'),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
]
