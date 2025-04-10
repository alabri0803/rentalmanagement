# Generated by Django 5.0.2 on 2025-04-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_address_alter_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='الصورة الشخصية'),
        ),
        migrations.AddField(
            model_name='profile',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم المؤسسة / الشركة'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='تم التحقق'),
        ),
        migrations.AddField(
            model_name='profile',
            name='language',
            field=models.CharField(choices=[('ar', 'العربية'), ('en', 'English')], default='ar', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_seen',
            field=models.DateTimeField(auto_now=True, verbose_name='آخر نشاط'),
        ),
    ]
