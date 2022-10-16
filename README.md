# django_model_cached_property

Django model cached property is useful for caching of property results for more time than lifetime of object during the request

This package use redis like a caching backend, because redis allow to delete keys by template. It is usefull for caching different keys for different users.

## Install

```pip install -U django-model-cached-property```

## Install and configure requirements

Install redis for caching.

```sudo apt install redis-server```

Configure **setup.py** of your django project.

```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

## Using

Package contains two functions:

* **model_cached_property** - it is decorator for class methods, which will cache results of property call for separate records.
* **invalidate_model_cached_property** - it is function for invalidation of method on the model record property.

### model_cached_property

You can use this decorator by following way.

```
from django_model_cached_property import model_cached_property

class Article(models.Model):
 
    @model_cached_property
    def comments_count(self):
        return self.comments.count()
```

It means you cache comments count for each record of article in your Django project.

You can set up cache timeout 3000 second by following way.

```
class Article(models.Model):
 
    @model_cached_property(timeout=3000)
    def comments_count(self):
        return self.comments.count()
```

By default, caching timeout is 60 second, by you can set up it globally in **settings.py**.

```
MODEL_CACHED_PROPERTY_TIMEOUT = 300000
```

Additionally, you can use caching of model property with input arguments. 
And in this case caching will be evaluated for all input sets of arguments.

For example caching by authenticated user.

```
class Article(models.Model):
 
    @model_cached_property
    def __user_in_bookmarks(self, user):
        return self.bookmarks.filter(user=user).exists()
 
    def user_in_bookmarks(self, user):
        return self.__user_in_bookmarks(user) if user.is_authenticated else False
```

### invalidate_model_cached_property

This function invalidate all cache keys on the property for one model record in database.

For example

```
article = get_object_or_404(Article, pk=12)
invalidate_model_cached_property(article, article.comments_count)
```

In this case you invalidate all cached keys for article with primary key 2.

## WARNING - Limitation

Limitation of this caching functionality consists in the fact that you can use it with unique input arguments only.
It means, that will not work with AnonymousUser object, because of in each request information about AnonymousUser object will be different, although it will be called by same user.
Therefore, use it on unique information only.
