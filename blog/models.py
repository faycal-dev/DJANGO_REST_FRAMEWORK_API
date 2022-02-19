from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return f'posts/{filename}'


class Categorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")
        # to only get the published posts

    options = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    categorie = models.ForeignKey(
        Categorie, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    image = models.ImageField(
        _("image"), upload_to=upload_to, default='posts/default.jpg')
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=options, default="published")

    # define the model managers
    objects = models.Manager()
    postobjects = PostObjects()

    # ordering by the date
    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
