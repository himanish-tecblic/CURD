# Generated by Django 2.2.12 on 2022-09-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tasktitle', models.CharField(max_length=70)),
                ('Taskdesc', models.CharField(max_length=70)),
            ],
        ),
    ]
