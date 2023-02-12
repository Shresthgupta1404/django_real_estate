# Generated by Django 2.2.2 on 2019-11-25 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='desc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('bedrooms', models.CharField(max_length=100)),
                ('garages', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('avatar', models.ImageField(default='../default_avatar.png', null=True, upload_to='../img')),
            ],
        ),
    ]