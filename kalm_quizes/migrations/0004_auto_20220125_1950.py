# Generated by Django 3.2.9 on 2022-01-25 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kalm_quizes', '0003_auto_20220125_0005'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionWithMultipleChoice',
            new_name='MultipleChoice',
        ),
        migrations.RenameModel(
            old_name='ChooseRightOrder',
            new_name='PutInOrder',
        ),
        migrations.RenameModel(
            old_name='QuestionWithOneAnswer',
            new_name='SingleChoice',
        ),
    ]
