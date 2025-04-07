# Generated by Django 5.0.2 on 2025-04-07 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_alter_property_options_alter_propertyimage_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم الوحدة')),
                ('type', models.CharField(choices=[('شقة', 'شقة'), ('محل', 'محل'), ('مكتب', 'مكتب'), ('مخزن', 'مخزن'), ('موقف', 'موقف')], max_length=50, verbose_name='نوع الوحدة')),
                ('floor_number', models.PositiveIntegerField(verbose_name='رقم الطابق')),
                ('area', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='المساحة')),
                ('is_occupied', models.BooleanField(default=False, verbose_name='مشغولة؟')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='properties.property', verbose_name='العقار')),
            ],
            options={
                'verbose_name': 'وحدة',
                'verbose_name_plural': 'الوحدات',
            },
        ),
    ]
