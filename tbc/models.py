from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, blank=True)
    username = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='profile_images', default='default_profile.jpg')
    skills = models.TextField(blank=True)
    education = models.TextField(blank=True)
    aboutme = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    portfolio = models.ImageField(upload_to='portfolio_images', blank=True)
    activities = models.ImageField(upload_to='activities_images', blank=True)
    views = models.IntegerField(default=0)
    reviews = models.TextField()
    location = models.CharField(max_length=128, blank=True)


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
    image = models.ImageField(upload_to='LendAndSell_images', default='default_profile.jpg')
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
    image = models.ImageField(upload_to='Service_images', default='default_profile.jpg')
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
    image = models.ImageField(upload_to='Projects_images', default='default_profile.jpg')
    timeline = models.CharField(max_length=128)
    keywords = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Projects, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comments(models.Model):
    author = models.ForeignKey(User, blank=True)
    comment = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    profile = models.ForeignKey(Profile, null=True, blank=True)
    lendandsell = models.ForeignKey(LendAndSell, null=True, blank=True)
    service = models.ForeignKey(Service, null=True, blank=True)
    project = models.ForeignKey(Projects, null=True, blank=True)


    def save(self, *args, **kwargs):
        super(Comments, self).save(*args, **kwargs)

    def __str__(self):
        return self.author.username

#class Contact(models.Model):
#        from_email = forms.EmailField(required=True)
#        subject = forms.CharField(required=True)
#        message = forms.CharField(widget=forms.Textarea, required=True)
