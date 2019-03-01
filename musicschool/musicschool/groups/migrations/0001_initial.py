# Generated by Django 2.1.1 on 2019-02-21 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=300)),
                ('miniature', models.FileField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ERPUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=50)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_information', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos')),
                ('image', models.FileField(blank=True, null=True, upload_to='images')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('audio', models.FileField(blank=True, null=True, upload_to='audio')),
                ('guitarpro', models.FileField(blank=True, null=True, upload_to='gp')),
                ('youtubeurl', models.CharField(blank=True, max_length=50, null=True)),
                ('text', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('articles', models.ManyToManyField(related_name='articles_group', to='groups.Article')),
                ('members', models.ManyToManyField(related_name='members_group', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='categories', to='groups.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='media',
            field=models.ManyToManyField(blank=True, related_name='media', to='groups.Media'),
        ),
    ]
