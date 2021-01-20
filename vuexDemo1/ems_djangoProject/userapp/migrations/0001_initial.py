# Generated by Django 2.0.6 on 2021-01-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=80)),
                ('img', models.ImageField(default='img/1.jpg', upload_to='img')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
                'db_table': 'emps',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_password', models.CharField(max_length=20)),
                ('real_name', models.CharField(max_length=20)),
                ('gender', models.SmallIntegerField(choices=[(0, 'man'), (1, 'woman')], default=0)),
                ('status', models.BooleanField(default=True)),
                ('register_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
            },
        ),
    ]
