from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    film_time = models.IntegerField(help_text="Tempo em minutos")
    resume = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:

        verbose_name_plural = "Recipes"