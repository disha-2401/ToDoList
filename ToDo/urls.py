from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.addToDo, name='add'),
    path('complete/<todo_id>', views.completeToDo, name='complete'),
    path('deleteCompleted', views.deleteCompleted, name='deleteCompleted'),
    path('deleteAll', views.deleteAll, name='deleteAll'),
    path('update', views.update, name='update'),
    path('updatetodo/<todo_id>', views.updatetodo, name='updatetodo'),
    path('homeRedirect/<todo_id>', views.homeRedirect, name='homeRedirect'),
]