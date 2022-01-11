from django.urls import include, path

import rsps_conf.views as rsps_conf

app_name = "rsps_conf"

urlpatterns = [
    path("", rsps_conf.index, name="index"),
    # path("register/", rsps_conf.index, name="index"),
    # path("register/", rsps_conf.register_participant, name="register"),
]
