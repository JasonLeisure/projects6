from django.db import models


class BinVO(models.Model):
    closet_name = models.CharField(max_length=100)
    import_href = models.CharField(max_length=50, unique=True)


class Shoe(models.Model):
    manufacturer = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    picture_url = models.URLField(null=True)
    bin = models.ForeignKey(
        BinVO,
        related_name="shoes",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.model_name
