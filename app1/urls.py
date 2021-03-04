from django.urls import path
from .import views


urlpatterns = [
	path('',views.home,name='homepg'),
	path('donerpg',views.donerpg),
	path('recieverpg',views.recieverpg),
	path('doner',views.doneradd),
	path('recieverreg',views.recieveradd),
	path('recieverlog',views.recieverlog),
	path('loginpg',views.log),
	path('display',views.display),
	path('removednr',views.remdoner),
	path('rempage',views.remdnr),
]