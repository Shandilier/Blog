from django.conf.urls import url
from . import views
urlpatterns=[
url(r'^$',views.Home,name='First'),
url(r'^Blog/$',views.BlogListView.as_view(),name='blog'),
url(r'^Blog/(?P<pk>\d+)$',views.BlogDetailView.as_view(),name='blog-detail'),
url(r'^Userlist/$',views.UserListView.as_view(),name='user'),
url(r'^user/(?P<pk>\d+)$',views.UserDetailView.as_view(),name='user-detail'),
url(r'^signup/$', views.signup, name='signup'),

url(r'^profile/$', views.profile, name='profile'),
url(r'^profile/edit/$', views.edit_profile, name='userchange'),
# url(r'^profile/edituser/$', views.edit_user_profile, name='userprofilechange'),
url(r'^Blog/create$', views.BlogCreate.as_view(), name='create'),
url(r'^Blog/(?P<pk>\d+)/update/$', views.BlogUpdateView.as_view(), name='update'),
url(r'^Blog/(?P<pk>\d+)/delete/$', views.BlogDeleteView.as_view(), name='delete'),
url(r'^Blog/(?P<pk>\d+)/comment/$', views.BlogCommentCreate.as_view(), name='blog-comment'), 
]