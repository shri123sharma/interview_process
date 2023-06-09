# Generated by Django 4.0.5 on 2023-05-17 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interview_process', '0004_inteviewquestion_question_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('questions_result', models.JSONField()),
                ('final_score', models.FloatField(blank=True, default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InterviewQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('question_type', models.CharField(choices=[('python', 'PYTHON'), ('django', 'DJANGO'), ('react', 'REACT'), ('sql', 'SQL'), ('html', 'HTML'), ('css', 'CSS')], default='python', max_length=100)),
                ('question_difficulty_level', models.CharField(choices=[('easy', 'EASY'), ('medium', 'MEDIUM'), ('hard', 'HARD')], default='easy', max_length=50)),
                ('question_text', models.TextField(unique=True)),
                ('question_description', models.TextField(blank=True, null=True)),
                ('question_answer', models.TextField(blank=True, null=True)),
                ('question_time', models.DurationField(null=True)),
                ('pointer', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='interviewer',
            name='candidate_interview',
        ),
        migrations.DeleteModel(
            name='InteviewQuestion',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='candidate_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='InterViewer',
        ),
        migrations.AddField(
            model_name='interview',
            name='candidate_interview',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interview_candidate', to='interview_process.candidate'),
        ),
    ]
