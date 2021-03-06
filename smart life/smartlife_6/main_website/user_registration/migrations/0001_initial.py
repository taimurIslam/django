# Generated by Django 2.0.1 on 2018-02-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.ImageField(upload_to='')),
                ('email_address', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=50)),
                ('user_address', models.CharField(max_length=200)),
            ],
        ),
    ]
