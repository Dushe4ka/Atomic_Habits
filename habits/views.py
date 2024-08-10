from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitsCreateAPIView(CreateAPIView):
    """Эндпоинт создания привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Привязываем текущего пользователя к создаваемому объекту"""
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitsRetrieveAPIView(RetrieveAPIView):
    """Эндпоинт отображения одной привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsUpdateAPIView(UpdateAPIView):
    """Эндпоинт редактирования привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsDestroyAPIView(DestroyAPIView):
    """Эндпоинт удаления привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsListAPIView(ListAPIView):
    """Эндпоинт вывода списка привычек c признаком публичности"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [AllowAny]

    def get_queryset(self):
        """Отфильтруем привычки по признаку публикации"""
        return Habit.objects.filter(is_public=True)


class UserHabitsListAPIView(ListAPIView):
    """Эндпоинт вывода списка привычек конкретного пользователя"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPaginator

    def get_queryset(self):
        """Отфильтруем привычки текущего пользователя"""
        return Habit.objects.filter(owner=self.request.user)
