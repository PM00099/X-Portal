# Generated by Django 3.0.4 on 2020-04-05 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('um', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xuser',
            name='email',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xuser',
            name='fname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xuser',
            name='lname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
