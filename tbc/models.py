from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='profile_images', blank=True)
    skills = models.TextField()
    education = models.TextField()
    aboutme = models.TextField()
    slug = models.SlugField(unique=True)
    portfolio = models.ImageField(upload_to='portfolio_images', blank=True)
    activities = models.ImageField(upload_to='activities_images', blank=True)
    views = models.IntegerField(default=0)
    reviews = models.TextField()
    # location
    # password = models.CharField(max_length=20)
    # email = models.CharField(max_length=128)
    # username = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

class Inbox(models.Model):
    profile = models.ForeignKey(Profile)
    messages = models.TextField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Inbox, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class LendAndSell(models.Model):
    profile = models.ForeignKey(Profile)
    title = models.CharField(max_length=128)
    description = models.TextField()
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='LendAndSell_images', blank=True)
    price = models.CharField(max_length=128)
    availability = models.CharField(max_length=128)
    keywords = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(LendAndSell, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Service(models.Model):
    profile = models.ForeignKey(Profile)
    title = models.CharField(max_length=128)
    description = models.TextField()
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='Service_images', blank=True)
    price = models.CharField(max_length=128)
    availability = models.CharField(max_length=128)
    keywords = models.TextField()
    location = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Projects(models.Model):
    profile = models.ForeignKey(Profile)
    title = models.CharField(max_length=128)
    description = models.TextField()
    lookingFor = models.TextField()
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='Projects_images', blank=True)
    timeline = models.CharField(max_length=128)
    keywords = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Projects, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
