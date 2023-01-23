# Generated by Django 4.1.3 on 2022-12-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_customuser_email_confirm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email_confirm',
            field=models.BooleanField(default=False, verbose_name='Пользователь подтвердил почту'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='account_url',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ссылка'),
        ),
    ]