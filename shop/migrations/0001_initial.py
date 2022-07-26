# Generated by Django 4.0.1 on 2022-07-24 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pin', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('pic', models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to='images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pin', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('pic', models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to='images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
