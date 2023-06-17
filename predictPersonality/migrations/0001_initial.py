# Generated by Django 4.1.7 on 2023-03-02 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryId', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qId', models.CharField(max_length=20)),
                ('question', models.CharField(max_length=100)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='predictPersonality.category')),
            ],
        ),
    ]