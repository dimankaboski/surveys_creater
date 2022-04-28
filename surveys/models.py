from django.db import models


class Survey(models.Model):
    """
    Шаблон опросника, имеет поля: название, описание, кем создан, когда создан, время обновления
    Связан один ко многим к Element
    """
    name = models.CharField('Название', max_length=100, blank=False)
    description = models.TextField('Описание', blank=True)
    created_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at', null=True)
    updated_at = models.DateTimeField(auto_now=True)


class Element(models.Model):
    """
    Элемент опросника, имеет несколько типов:
    1. Один из списка
    2. Несколько из списка
    3. Строка
    4. Текст с абзацами
    5. Шкала
    """
    class TYPE:
        """
        Класс с выбором вариантов типа элемента
        """
        ONE_IN_MANY = 'one_in_list'
        MANY_IN_MANY = 'many_in_list'
        STRING = 'string'
        TEXT = 'textarea'
        RANGE = 'range'

        LIST = (
            (ONE_IN_MANY, 'Один из списка'),
            (MANY_IN_MANY, 'Неколько из списка'),
            (STRING, 'Строка'),
            (TEXT, 'Текст с абзацами'),
            (RANGE, 'Шкала'),
        )
    
    type = models.CharField('Тип элемента', max_length=20, blank=False)
    text = models.TextField('Текст', blank=True, help_text='Если варианты спика, то разделение идет с новой строки')
    range_from = models.IntegerField(default=1, verbose_name='Шкала от')
    range_to = models.IntegerField(default=10, verbose_name='Шкала до')
    required = models.BooleanField(default=False, verbose_name='Обязательное поле')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Опрос')
    file = models.FileField(upload_to='survey_files', null=True, blank=True, verbose_name='Файл')


class FilledSurvey(models.Model):
    """
    Заполненный опросник
    Имеет поля: кем заполнен, к какому шаблону относится, время заполнения
    """
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at', null=True)


class ElementValue(models.Model):
    """
    Значение элемента в опроснике
    Связан с FilledSurvey, Element
    Имеет поле: значение
    """
    survey = models.ForeignKey(FilledSurvey, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    value = models.TextField()