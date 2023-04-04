from django.db import models
from django.urls import reverse


class SermonCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Sermon(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(SermonCategory, on_delete=models.CASCADE, default="")
    audio = models.FileField(upload_to='audio', blank=True, null=True)
    video = models.FileField(upload_to='video', blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    description = models.TextField(max_length=5000, blank=True, null=True)

    def display_category(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([category.name for category in self.category.all()[:3]])

    display_category.short_description = 'Category'

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('sermon-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class SermonsByOtherFathers(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(SermonCategory, on_delete=models.CASCADE, default="")
    audio = models.FileField(upload_to='audio', blank=True, null=True)
    video = models.FileField(upload_to='video', blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    description = models.TextField(max_length=5000, blank=True, null=True)
    external_link = models.URLField(max_length=200, blank=True, null=True)

    def display_category(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([category.name for category in self.category.all()[:3]])

    display_category.short_description = 'Category'

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('sermon-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, default="")
    book = models.FileField(upload_to='books', null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    description = models.TextField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('book-detail', args=[str(self.id)])


class BooksByOtherFathers(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, default="")
    book = models.FileField(upload_to='books', null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    description = models.TextField(max_length=5000, blank=True, null=True)
    external_link = models.URLField(max_length=200, blank=True, null=True)

    def display_category(self):
        """Creates a string for the Genre. This is required to display category in Admin."""
        return ', '.join([category.name for category in self.category.all()[:3]])

    display_category.short_description = 'Category'

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('other-books-detail', args=[str(self.id)])

    def __str__(self):
        return self.title
