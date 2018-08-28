from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import python_2_unicode_compatible, force_text
from django.utils.functional import cached_property
try:
    from django.contrib.contenttypes.fields import GenericForeignKey
except ImportError:
    from django.contrib.contenttypes.generic import GenericForeignKey
#import markdown
import json
from django.utils.html import escape	

# Create your models here.
TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)
class ModelPost(models.Model):
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    published_date = models.DateTimeField()
    text = models.CharField(max_length=300)

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
    def get_title(self):
        return self.title
		
class Article(models.Model):
    pub_date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=100)
    headline = models.CharField(max_length=100)
    content = models.CharField(max_length=1300)
    reporter = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
class Review(models.Model):
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=1300)
class Book(models.Model):
    name = models.CharField(max_length=300)
    authors = models.ManyToManyField(Author)
    publisher = models.ManyToManyField(Publisher)
    article = models.ManyToManyField(Article)
    review = models.ManyToManyField(Review)
    image = models.CharField(max_length=300)
    def __str__(self):
        return self.name


def has_int_pk(model):
    """Tests whether the given model has an integer primary key."""
    pk = model._meta.pk
    return (
        (
            isinstance(pk, (models.IntegerField, models.AutoField)) and
            not isinstance(pk, models.BigIntegerField)
        ) or (
            isinstance(pk, models.ForeignKey) and has_int_pk(pk.rel.to)
        )
    )


def get_str_pk(obj, connection):
    return obj.pk.hex if isinstance(obj.pk, uuid.UUID) and connection.vendor != "postgresql" else force_text(obj.pk)


META_CACHE_KEY = "_meta_cache"

@python_2_unicode_compatible
class SearchEntry(models.Model):
    """An entry in the search index."""

    engine_slug = models.CharField(
        max_length=200,
        db_index=True,
        default="default",
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )

    object_id = models.TextField()

    object_id_int = models.IntegerField(
        blank=True,
        null=True,
        db_index=True,
    )

    object = GenericForeignKey()

    title = models.CharField(
        max_length=1000,
    )

    description = models.TextField(
        blank=True,
    )

    content = models.TextField(
        blank=True,
    )

    url = models.CharField(
        max_length=1000,
        blank=True,
    )

    meta_encoded = models.TextField()

    def _deserialize_meta(self):
        from watson.search import SearchEngine
        engine = SearchEngine._created_engines[self.engine_slug]
        model = ContentType.objects.get_for_id(self.content_type_id).model_class()
        adapter = engine.get_adapter(model)
        return adapter.deserialize_meta(self.meta_encoded)

    @cached_property
    def meta(self):
        """Returns the meta information stored with the search entry."""
        # Attempt to use the cached value.
        if hasattr(self, META_CACHE_KEY):
            return getattr(self, META_CACHE_KEY)
        # Decode the meta.
        meta_value = self._deserialize_meta()
        setattr(self, META_CACHE_KEY, meta_value)
        return meta_value

    def get_absolute_url(self):
        """Returns the URL of the referenced object."""
        return self.url

    def __str__(self):
        """Returns a string representation."""
        return self.title

    class Meta:
        verbose_name_plural = "search entries"
        app_label = 'watson'
