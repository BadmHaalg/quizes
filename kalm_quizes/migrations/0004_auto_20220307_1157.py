# Generated by Django 3.2.9 on 2022-03-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalm_quizes', '0003_usercourseanswers_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourseanswers',
            name='quiz',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='usercourseanswers',
            name='user',
            field=models.IntegerField(),
        ),
    ]
