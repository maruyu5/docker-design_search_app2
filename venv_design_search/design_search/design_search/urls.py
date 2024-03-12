from django.urls import path
from . import views
# from .views import email_form
from .views import inquiry_list

from django.conf import settings
from django.conf.urls.static import static
from .views import EditInquiryView
from .views import DetailInquiryView


app_name = 'design_search'
urlpatterns = [
    path('diary/', views.DiaryView.as_view(), name="diary"),
    path('hello/', views.HelloView.as_view(), name="hello"),
    path('tashizan/', views.TashizanView.as_view(), name="tashizan"),
    path('kajiki/', views.KajikiView.as_view(), name="kajiki"),
    path('tenki/', views.TenkiView.as_view(), name="tenki"),
    path('tashizan_form/', views.TashizanFormView, name="tashizan_form"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('inquiry_list/', inquiry_list, name='inquiry_list'),
    path('edit_inquiry/<int:inquiry_id>/', EditInquiryView.as_view(), name='edit_inquiry'),
    path('detail_inquiry/<int:inquiry_id>/', DetailInquiryView.as_view(), name='detail_inquiry'),
    # path('email/', views.email_form, name='email_form'),
]

# 開発環境でのみメディアファイルを提供する設定を追加
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    