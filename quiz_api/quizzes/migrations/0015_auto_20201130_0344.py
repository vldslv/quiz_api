# Generated by Django 2.2.1 on 2020-11-30 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0014_question_answer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_type',
            field=models.IntegerField(choices=[(1, 'Текстовое поле'), (2, 'Выбор одного варианта'), (3, 'Множественный выбор')], default=1, verbose_name='Тип ответа'),
        ),
    ]
