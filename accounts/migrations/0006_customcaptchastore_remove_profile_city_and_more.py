# Generated by Django 5.0.4 on 2024-07-02 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_connection_profile_info_profile_notification_and_more'),
        ('captcha', '0002_alter_captchastore_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomCaptchaStore',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('captcha.captchastore',),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='street_address',
        ),
    ]
