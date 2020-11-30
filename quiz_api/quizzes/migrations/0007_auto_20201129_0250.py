# Generated by Django 2.2.1 on 2020-11-28 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0006_auto_20201129_0009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Квиз', 'verbose_name_plural': 'Квизы'},
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='quizzes.Quiz', verbose_name='Квиз'),
        ),
    ]
