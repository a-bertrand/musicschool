# Generated by Django 2.1.1 on 2019-01-19 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='categories', to='groups.Category'),
        ),
    ]