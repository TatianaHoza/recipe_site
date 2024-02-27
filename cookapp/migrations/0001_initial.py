# Generated by Django 5.0.2 on 2024-02-27 10:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CathegoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('steps', models.TextField()),
                ('time', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cathegories', models.ManyToManyField(default='new', to='cookapp.cathegorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeToCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('cathegory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookapp.cathegorymodel')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookapp.recipemodel')),
            ],
        ),
    ]
