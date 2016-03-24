from django.conf.urls import patterns, include, url
from django.contrib import admin

from last_app.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'final_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',render_index_page),                    	  #index page
    url(r'^index1/$',checkuser),                              #username and password are sent by this url by using ajax
    url(r'^signup/$',signup_function),
    url(r'^homepage/$',render_homepage),                      #main homepage
    url(r'^home/$',receive_ajax),							  #url by which list of all components is sent
    url(r'^homepage/(.*)',render_generated_form),			  #all generated forms will be shown b this url and handled by render_generated_form
    url(r'^checkform/',checkfo),							  #checks whether url exists in database as url should be unique
)
