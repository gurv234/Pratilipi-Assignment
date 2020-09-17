
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from apps.core.views import signup
from apps.story.views import frontpage, submit, newest, vote, story
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', frontpage, name='frontpage'),
    # path('u/', include('apps.userprofile.urls')),
    path('submit/', submit, name='submit'),
    path('newest/', newest, name='newest'),
    path('s/<int:story_id>/vote', vote, name='vote'),
    path('s/<int:story_id>', story, name='story'),
    path('admin/', admin.site.urls),
]
