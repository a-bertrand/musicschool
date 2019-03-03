# Generated by Django 2.1.1 on 2019-03-03 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_auto_20190227_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.ManyToManyField(blank=True, to='groups.LessonDate')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='groups.ERPUser')),
            ],
        ),
    ]
