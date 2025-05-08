from django.contrib import admin
from Blogs_Data.models import FeaturedPost, Author, Category
admin.site.register(FeaturedPost)
admin.site.register(Author)
admin.site.register(Category)
from Blogs_Data.models import Writer, Topic, BlogPost
admin.site.register(Writer)
admin.site.register(Topic)
admin.site.register(BlogPost)
from Blogs_Data.models import Expert, RecommendedArticle
admin.site.register(Expert)
admin.site.register(RecommendedArticle)
# Register your models here.
