# Generated by Django 4.1.3 on 2022-11-17 11:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default=uuid.uuid4, max_length=40, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('published', 'published'), ('unpublished', 'unpublished'), ('postponed', 'postponed'), ('archived', 'archived')], default='published', max_length=12)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'db_category',
                'ordering': ('name',),
            },
        ),
    ]
