# Generated by Django 5.0.2 on 2025-04-10 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم الهاتف'),
        ),
    ]
