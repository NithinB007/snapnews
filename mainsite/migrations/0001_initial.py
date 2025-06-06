# Generated by Django 3.2.25 on 2025-05-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomePageSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Home Page Setting',
                'verbose_name_plural': 'Home Page Settings',
                'db_table': 'homepagesettings',
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Site Setting',
                'verbose_name_plural': 'Site Settings',
                'db_table': 'sitesettings',
            },
        ),
        migrations.CreateModel(
            name='SocialSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=20)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Social Setting',
                'verbose_name_plural': 'Social Settings',
                'db_table': 'socialsettings',
            },
        ),
    ]
