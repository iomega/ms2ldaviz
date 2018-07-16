from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^people/', views.people, name='people'),
    url(r'^api/', views.api, name='people'),
    url(r'^user_guide/', views.user_guide, name='user_guide'),
    url(r'^disclaimer/', views.disclaimer, name='disclaimer'),
    url(r'^confidence/', views.confidence, name='confidence'),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^basicviz/', include('basicviz.urls')),
    url(r'^annotation/', include('annotation.urls')),
    url(r'^massbank/', include('massbank.urls')),
    url(r'^options/', include('options.urls')),
    url(r'^registration/', include('registration.urls')),
    url(r'^uploads/', include('uploads.urls')),
    url(r'^decomposition/',include('decomposition.urls')),
    url(r'^ms1analysis/', include('ms1analysis.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
       url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
