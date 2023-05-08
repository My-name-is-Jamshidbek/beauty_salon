"""
all models in here
"""
from django.db import models


class Category(models.Model):
    """
    title field: It represents the title or name of the category. It is a CharField with a maximum length of 100
    characters.
    description field: It represents an optional description for the category. It is a TextField, allowing for longer
    text input. The blank=True parameter allows the field to be left empty.
    photo field: It is an ImageField that allows you to upload and store an image file for the category. The upload_to
    parameter specifies the directory within the media storage where the uploaded category photos will be stored. In
    this case, the photos will be stored in the "category_photos" directory.
    price field: It represents the price of the category. It is a DecimalField with max_digits set to 10 and
    decimal_places set to 2, allowing for a maximum of 10 digits with 2 decimal places.
    The __str__ method is overridden to provide a meaningful string representation of the Category object. In this case,
    it returns the title of the category.
    """
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='category_photos/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Photo(models.Model):
    """
    image field: It is an ImageField specifically designed for handling image uploads. It stores the uploaded image
    file and automatically handles file uploads to the specified directory. In this case, the upload_to parameter is
    set to "photos/", which means that uploaded photos will be stored in the "photos" directory within the media
    storage.
    upload_date field: It is a DateTimeField that automatically records the date and time when the photo was uploaded.
    The auto_now_add=True parameter ensures that the upload_date is set to the current date and time when a new photo
    object is created.
    category field: It is a ForeignKey that establishes a one-to-many relationship between the Photo and Category
    models.
    Each photo belongs to a specific category. The on_delete=models.CASCADE parameter ensures that if a category is
    deleted, all its associated photos will also be deleted. The related_name='photos' parameter allows you to access
    the photos of a category from the category instance.
    """
    image = models.ImageField(upload_to='photos/')
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='photos')

