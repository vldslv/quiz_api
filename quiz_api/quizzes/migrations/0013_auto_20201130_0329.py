# Generated by Django 2.2.1 on 2020-11-30 00:29

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0012_auto_20201130_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=jsonfield.fields.JSONField(default='', verbose_name='Ответ'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
