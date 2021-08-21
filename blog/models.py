from django.db import models

# Create your models here.

"""

## Models

- Text
    - ID
    - Type: (Poem, Short Story)
    - Published Date
    - Title
    - Content
    - Comments
    - (?) Category
    - (?) Author(s) / Contributors
    - (?) Likes
- Comment
    - Text
    - Author
    - (?) Likes
    - (?) Response

## Notes

- Using Markdown in Django: https://learndjango.com/tutorials/django-markdown-tutorial
"""


class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    pub_date = models.DateTimeField("date published")

    class PostType(models.TextChoices):
        POEM = "PM"
        SHORT_STORY = "SS"

    post_type = models.CharField(
        choices=PostType.choices, default=PostType.SHORT_STORY, max_length=2)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
