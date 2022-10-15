# Generated by Django 3.2.4 on 2022-10-08 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0006_auto_20221007_1655'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('order_title', models.CharField(max_length=150, verbose_name='订单标题')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='订单总价')),
                ('real_price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='实付金额')),
                ('order_number', models.CharField(max_length=64, verbose_name='订单号')),
                ('order_status', models.SmallIntegerField(choices=[(0, '未支付'), (1, '已支付'), (2, '已取消'), (3, '超时取消')], default=0, verbose_name='订单状态')),
                ('pay_type', models.SmallIntegerField(choices=[(1, '支付宝'), (2, '微信支付')], default=1, verbose_name='支付方式')),
                ('credit', models.IntegerField(default=0, verbose_name='使用的积分数量')),
                ('coupon', models.IntegerField(null=True, verbose_name='用户优惠券ID')),
                ('order_desc', models.TextField(max_length=500, verbose_name='订单描述')),
                ('pay_time', models.DateTimeField(null=True, verbose_name='支付时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_orders', to=settings.AUTH_USER_MODEL, verbose_name='下单用户')),
            ],
            options={
                'verbose_name': '订单记录',
                'verbose_name_plural': '订单记录',
                'db_table': 'ly_order',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('expire', models.IntegerField(default='0', help_text='0表示永久有效', verbose_name='有效期周期')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='课程原价')),
                ('real_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='课程实价')),
                ('discount_name', models.CharField(default='', max_length=120, verbose_name='优惠类型')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_orders', to='course.course', verbose_name='课程ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_courses', to='order.order', verbose_name='订单ID')),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情',
                'db_table': 'ly_order_detail',
            },
        ),
    ]
