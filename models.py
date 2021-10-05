from django.db import models

class Main(models.Model):

    rows = models.IntegerField(verbose_name ="количество строк")
    columns = models.IntegerField(verbose_name ="количество столбцов")

    class Meta:
        verbose_name_plural = "Документ"
        verbose_name = "Документы"

    def __str__(self):
        return  "Документ номер " + str(self.id)