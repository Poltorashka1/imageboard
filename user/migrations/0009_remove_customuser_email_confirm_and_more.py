# Generated by Django 4.1.3 on 2022-12-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_customuser_email_confirm_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='email_confirm',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='reset_password',
        ),
        migrations.AddField(
            model_name='customuser',
            name='account_url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]