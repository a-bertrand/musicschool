# Generated by Django 2.1.1 on 2018-11-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20180920_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.FileField(upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='media',
            name='text',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='video',
            field=models.FileField(upload_to='static/videos'),
        ),
    ]
