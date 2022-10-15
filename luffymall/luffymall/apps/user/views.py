from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from .models import User
from order.models import Order
from .serializers import UserModelSerializers,UserOrderModelSerializer
from rest_framework.permissions import IsAuthenticated
class RegisterView(CreateAPIView):
    queryset = User.objects
    serializer_class = UserModelSerializers
class UserOrderAPIView(ListAPIView):
    serializer_class = UserOrderModelSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user.id)