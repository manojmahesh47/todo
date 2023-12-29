from django.urls import path
from . import views

app_name='todo_app'
urlpatterns = [

   path('',views.add,name='add'),

   path('delete/<int:taskid>/',views.delete,name='delete'),
   path('update/<int:taskid>/',views.update,name='update'),
   path('hom/',views.TaskKistview.as_view(),name='hom'),
   path('details/<int:pk>/',views.Detailview.as_view(),name='details'),
   path('edit/<int:pk>/',views.Updateview.as_view(),name='edit'),
   path('del/<int:pk>/',views.Deleteview.as_view(),name='del'),
]
