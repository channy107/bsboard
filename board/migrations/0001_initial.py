# Generated by Django 2.1.2 on 2018-11-05 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='boardDb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('write_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
