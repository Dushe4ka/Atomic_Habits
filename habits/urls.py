from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitsCreateAPIView, HabitsDestroyAPIView,
                          HabitsListAPIView, HabitsRetrieveAPIView,
                          HabitsUpdateAPIView, UserHabitsListAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path("", HabitsListAPIView.as_view(), name="habits-list"),
    path("user_habits/", UserHabitsListAPIView.as_view(), name="user-habits"),
    path("create/", HabitsCreateAPIView.as_view(), name="habits-create"),
    path("<int:pk>/retrieve/", HabitsRetrieveAPIView.as_view(), name="habits-retrieve"),
    path("<int:pk>/update/", HabitsUpdateAPIView.as_view(), name="habits-update"),
    path("<int:pk>/habits-delete/", HabitsDestroyAPIView.as_view(), name="delete"),
]