from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='authors/', blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class FeaturedPost(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='featured_posts/')
    post_url = models.URLField()
    categories = models.ManyToManyField(Category, blank=True)
    authors = models.ManyToManyField(Author, related_name='posts')

    def __str__(self):
        return self.title
    
class Writer(models.Model):
    full_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='writers/', blank=True, null=True)

    def __str__(self):
        return self.full_name

class Topic(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    headline = models.CharField(max_length=500)
    identifier = models.SlugField(blank=True)
    writers = models.ManyToManyField(Writer, related_name='articles')
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='articles/', blank=True, null=True)
    topics = models.ManyToManyField(Topic, related_name='articles')
    source_link = models.URLField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline
    
class Expert(models.Model):
    full_name = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='experts/', blank=True, null=True)

    def __str__(self):
        return self.full_name

class RecommendedArticle(models.Model):
    title = models.CharField(max_length=500)
    experts = models.ManyToManyField(Expert, related_name='recommended_articles')
    description = models.TextField(blank=True)
    article_image = models.ImageField(upload_to='recommended_articles/', blank=True, null=True)
    article_link = models.URLField()
    published_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
