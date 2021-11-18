# Generated by Django 3.2.8 on 2021-11-03 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ashaworkapp', '0005_auto_20211103_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='AskDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('assign', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=1000)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ashaworkapp.doctorentry')),
                ('patients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ashaworkapp.patiententry')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ashaworkapp.usertype')),
            ],
        ),
    ]
