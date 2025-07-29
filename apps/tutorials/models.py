from django.db import models
from django.contrib.auth.models import Group, User
from django.utils import timezone


class Tutorial(models.Model):
    name = models.CharField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    category = models.CharField(null=False)
    published = models.BooleanField(null=False)
    untis_count = models.IntegerField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk and Tutorial.objects.filter(pk=self.pk).exists():
            # Only update when it's not creation
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class Tutorial_Unit(models.Model):
    tutorial = models.ForeignKey(
        Tutorial, on_delete=models.CASCADE, related_name="units"
    )
    title = models.CharField(null=False)
    unit_number = models.IntegerField(null=False)
    content = models.TextField(null=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["tutorial", "title"], name="unique_unit_title_per_tutorial"
            ),
            models.UniqueConstraint(
                fields=["tutorial", "unit_number"],
                name="unique_unit_number_per_tutorial",
            ),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk and Tutorial.objects.filter(pk=self.pk).exists():
            # Only update when it's not creation
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class Image(models.Model):
    name = models.CharField(max_length=50, default="Main Image")
    photo = models.ImageField(upload_to="units/")
    unit = models.ForeignKey(
        Tutorial_Unit, related_name="images", on_delete=models.CASCADE
    )

    photo_url = models.URLField(blank=True, null=True, editable=False)  # New field

    def save(self, *args, **kwargs):
        # Call save first so `photo.url` is available
        self.photo_url = self.photo.url
        # print(self.photo.name)
        super().save(*args, **kwargs)
