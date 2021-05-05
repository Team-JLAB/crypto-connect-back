# Generated by Django 3.2.1 on 2021-05-04 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crypto', '0005_auto_20210504_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='wallet_id',
        ),
        migrations.AlterField(
            model_name='wallet',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]