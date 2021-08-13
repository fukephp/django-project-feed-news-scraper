from django.db import models

# Create your models here.
class Symbol(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    link = models.CharField(max_length=300)
    published = models.DateTimeField()
    symbol = models.CharField(max_length=100,null=True)
    # symbol = models.ForeignKey(Symbol, related_name="articles", on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']


