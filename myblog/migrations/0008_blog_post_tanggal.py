# Generated by Django 4.1.4 on 2023-01-03 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_home_github_link_home_twitter_link_home_webname'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='tanggal',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]