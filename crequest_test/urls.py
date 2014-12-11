from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from crequest.middleware import CrequestMiddleware

def function_without_request():
    cr = CrequestMiddleware.get_request()
    print type(cr)

def home(request):
    html = "<html><body>ok</body></html>"
    function_without_request()
    return HttpResponse(html)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    # url(r'^crequest_test/', include('crequest_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
