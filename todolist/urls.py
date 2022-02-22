from django.urls import path, include

from . import views

app_name = 'todolist'

urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
        path('<int:pk>/delete/', views.ItemDeleteView.as_view(), name='delete'),
        path('finished/', views.FinishedItemView.as_view(), name='finished'),
        path('create/', views.ItemCreateView.as_view(), name='create'),
        path('signup/', views.SignUpView.as_view(), name='signup'),
        path('profile/', views.profile, name='profile'),
        path('change_password/', views.ChangePassword.as_view(),
            name='pass_change'),
    ]
