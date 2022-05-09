from secrets import choice
from django.db import models
import uuid

class Survey(models.Model):
    """
    Шаблон опросника, имеет поля: название, описание, кем создан, когда создан, время обновления
    Связан один ко многим к Element
    """
    class ACCESS:
        """
        Разрешение на прохождение опроса
        """
        LINK = 'link'
        OPENED = 'opened'

        LIST = (
            (LINK, 'Только по ссылке'),
            (OPENED, 'Открыт всем')
        )
    
    name = models.CharField('Название', max_length=100, blank=False)
    description = models.TextField('Описание', blank=True)
    access = models.CharField('Разрешение', max_length=20, choices=ACCESS.LIST, default=ACCESS.LINK)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at', null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_chosen_elements(self):
        return self.element_set.filter(type__in=[Element.TYPE.MANY_IN_MANY, Element.TYPE.ONE_IN_MANY])

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

    type = models.CharField('Тип элемента', choices=TYPE.LIST, max_length=20, blank=False)
    name = models.CharField('Вопрос', max_length=150, blank=False)
    text = models.TextField('Текст', blank=True, help_text='Если варианты спика, то разделение идет с новой строки')
    range_from = models.IntegerField(default=1, verbose_name='Шкала от')
    range_to = models.IntegerField(default=10, verbose_name='Шкала до')
    required = models.BooleanField(default=False, verbose_name='Обязательное поле')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Опрос')
    file = models.FileField(upload_to='survey_files', null=True, blank=True, verbose_name='Файл')

    def get_text_values(self):
        return self.text.split('\n')

    def get_range_iter(self):
        return [i for i in range(self.range_from, self.range_to)]

class FilledSurvey(models.Model):
    """
    Заполненный опросник
    Имеет поля: кем заполнен, к какому шаблону относится, время заполнения
    """
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at', null=True)

    def get_user(self):
        if self.user:
            return self.user
        else:
            return 'Аноним'

class ElementValue(models.Model):
    """
    Значение элемента в опроснике
    Связан с FilledSurvey, Element
    Имеет поле: значение
    """
    survey = models.ForeignKey(FilledSurvey, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    value = models.TextField()