from django.db import models

# Create your models here.
class Word(models.Model):
    search_word = models.CharField(max_length=100)

    def __str__(self):
        return self.search_word

class Document(models.Model): 
    title = models.CharField(max_length=300)
    year = models.IntegerField(max_length=4)
    author = models.CharField(max_length=300)
    words = models.ManyToManyField(Word, related_name='documents')
    file = models.FileField()
    def __str__(self):
        return self.title


class WordCount(models.Model):
    transcript = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='word_counts')
    word = models.ForeignKey(Word,on_delete=models.CASCADE, related_name='word_counts')
    count = models.IntegerField(default=1)
    
    pass

