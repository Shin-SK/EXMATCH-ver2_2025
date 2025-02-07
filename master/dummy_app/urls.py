# master/dummy_app/urls.py
from django.urls import path
from . import views  # 相対インポートに注意

urlpatterns = [
    # ex_member_update用のダミールート
    path('ex_member_update/', views.dummy_view, name='ex_member_update'),
    # ほかにも同様に <path('xxx', views.dummy_view, name='xxx')> など追加可
]
