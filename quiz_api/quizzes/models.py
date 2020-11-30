from django.db import models
from jsonfield import JSONField


class Quiz(models.Model):
    title = models.CharField('Название', max_length=200)
    start_date = models.DateTimeField(
        'Начало',
        blank=True,
        null=True,
        db_index=True
    )
    end_date = models.DateTimeField(
        'Окончание',
        blank=True,
        null=True,
        db_index=True
    )
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Квиз'
        verbose_name_plural = 'Квизы'


class Question(models.Model):
    ANSWER_TYPE_CHOICES = [
        (1, 'Текстовое поле'),
        (2, 'Выбор одного варианта'),
        (3, 'Множественный выбор'),
    ]
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.SET_NULL,
        related_name='questions',
        blank=True,
        null=True,
        verbose_name='Квиз'
    )
    sort_order = models.IntegerField('Порядок сортировки', default=0)
    text = models.TextField('Текст вопроса')
    answer = JSONField('Ответ', default='')
    answer_type = models.IntegerField(
        'Тип ответа',
        choices=ANSWER_TYPE_CHOICES,
        default=1
    )

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['sort_order']


class Attempt(models.Model):
    user_id = models.IntegerField('Идентификатор пользователя', default=1)
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='attempts',
        default=1,
        verbose_name='Квиз'
    )
    pass_date = models.DateTimeField(
        'Дата прохождения',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return f'Прохождение {str(self.pk)}'
    
    class Meta:
        verbose_name = 'Прохождение'
        verbose_name_plural = 'Прохождения'
        

class Answer(models.Model):
    attempt = models.ForeignKey(
        Attempt,
        on_delete=models.CASCADE,
        related_name='answers',
        blank=True,
        null=True,
        verbose_name='Прохождение'
    )
    answer = JSONField('Ответ', default='')

    def __str__(self):
        return f'Ответ {str(self.pk)}'
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
