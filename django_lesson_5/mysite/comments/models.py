from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from article.models import Article


class Comment(models.Model):

    author = models.CharField(max_length=30)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = RichTextUploadingField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    parent_id = models.PositiveIntegerField(blank=True, null=True, default=None)

    def __str__(self):
        return self.comment



