# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import User
from rest_framework_jwt.settings import api_settings

class UserModelSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(label='确认密码', required=True, allow_null=False, allow_blank=False, write_only=True)
    token = serializers.CharField(max_length=1024, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'id', 'token')
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate(self, data):
        # 验证密码
        password = data.get("password")
        password2 = data.get("password2")
        username = data.get('username')
        if len(password) < 6:
            raise serializers.ValidationError('密码太短不安全~')

        if password != password2:
            raise serializers.ValidationError('密码和确认必须一致~')

        if len(username) < 4:
            raise serializers.ValidationError('用户名太短8行哦！')

        return data

    def create(self, validated_data):
        # 删除一些不需要保存到数据库里面的字段
        del validated_data['password2']

        # 因为数据库中默认用户名是唯一的,所以我们把用户手机号码作为用户名

        # 继续调用ModelSerializer内置的添加数据功能
        user = super().create(validated_data)

        # 针对密码要加密
        user.set_password(user.password)
        # 修改密码等用于更新了密码,所以需要保存

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        user.token = jwt_encode_handler(payload)
        user.save()

        return user
from order.models import Order

class UserOrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id","order_number","order_status","created_time","course_list"]