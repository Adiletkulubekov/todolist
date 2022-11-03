from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


# Create your models here.
class Todolist(models.Model):
    describe = models.CharField(max_length=50, null=False, blank=False, verbose_name='describe')
    status = models.CharField(max_length=3000, blank=False, verbose_name='status', choices=status_choices,
                              default=status_choices[0][0])
    schedule_at = models.DateTimeField(verbose_name='schedule_at', auto_now_add=False)

    def __str__(self):
        return f'{self.describe} / {self.status} / {self.schedule_at}'
