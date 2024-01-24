from decimal import Decimal

from django.db import models

from users.models import CustomUser


class Site(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField()
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class DataSize(models.Model):
    website = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='data')
    sent_data_size = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    received_data_size = models.DecimalField(decimal_places=2, max_digits=20, default=0)

    def __str__(self):
        return f'{self.sent_data_size}/{self.received_data_size}'

    def sent_data_size_mb(self):
        return self.kilobytes_to_megabytes(self.sent_data_size)

    def received_data_size_mb(self):
        return self.kilobytes_to_megabytes(self.received_data_size)

    def kilobytes_to_megabytes(self, kilobytes):
        megabytes = Decimal(kilobytes) / Decimal(1024)
        return megabytes.quantize(Decimal('0.00'))
