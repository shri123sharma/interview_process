# Generated by Django 4.2.1 on 2023-05-22 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview_process', '0008_questiontype_alter_question_question_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionType',
        ),
    ]
