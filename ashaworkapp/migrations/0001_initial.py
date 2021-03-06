# Generated by Django 3.2.8 on 2021-11-01 11:45

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
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password2', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('adharno', models.CharField(max_length=100)),
                ('wardno', models.CharField(max_length=100)),
                ('panchayath', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=100)),
                ('fahusname', models.CharField(max_length=200)),
                ('fahusno', models.CharField(max_length=200)),
                ('noofchild', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
