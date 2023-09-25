from django.db import models

# Create your models here.

class Db(models.Model):
    title  = models.CharField(max_length=50, verbose_name = "Title")
    content = models.TextField(null=True, blank=True, verbose_name = "Description")
    price = models.FloatField(null=True, blank=True, verbose_name = "Price")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name = "Published")
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name = "Rubric")
    
class Rubric(models.Model):
        name = models.CharField(max_length=20, verbose_name = "Title")
        
        def __str__(self):
            return self.name
        
        class Meta:
            verbose_name_plural = 'Rubric'
            verbose_name = 'Rubric'
            ordering = ['name']