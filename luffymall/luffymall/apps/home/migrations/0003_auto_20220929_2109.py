# Generated by Django 3.2.4 on 2022-09-29 13:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_banner_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('title', models.CharField(max_length=500, verbose_name='导航标题')),
                ('link', models.CharField(max_length=500, verbose_name='导航链接')),
                ('position', models.IntegerField(choices=[(1, '顶部导航'), (2, '脚部导航')], default=1, verbose_name='导航位置')),
                ('is_site', models.BooleanField(default=False, verbose_name='是否是站外地址')),
            ],
            options={
                'verbose_name': '导航菜单',
                'verbose_name_plural': '导航菜单',
                'db_table': 'ly_nav',
            },
        ),
        migrations.AddField(
            model_name='banner',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='添加时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banner',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image_url',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='banner', verbose_name='广告图片'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=500, verbose_name='广告标题'),
        ),
    ]