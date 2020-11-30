# Generated by Django 2.2.1 on 2020-11-29 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0008_auto_20201129_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='end_date',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Окончание'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='start_date',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Начало'),
        ),
    ]