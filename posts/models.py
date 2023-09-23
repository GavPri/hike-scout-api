from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User 

class Posts(models.Model):
    image_filter_choices = [
    ('_1977', '1977'),
    ('brannan', 'Brannan'),
    ('earlybird', 'Earlybird'),
    ('hudson', 'Hudson'),
    ('inkwell', 'Inkwell'),
    ('lofi', 'Lo-Fi'),
    ('kelvin', 'Kelvin'), ('normal', 'Normal'),
    ('nashville', 'Nashville'), 
    ('rise', 'Rise'),
    ('toaster', 'Toaster'), 
    ('valencia', 'Valencia'),
    ('walden', 'Walden'), 
    ('xpro2', 'X-pro II')

]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=255, blank=True)
    content = models.TextField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default-post_cxcz4u',
        blank = True
    )
    location = GeopositionField(blank=True)
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default=normal
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner} - {self.title}"

# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(owner=instance)

# post_save.connect(create_profile, sender=User)
