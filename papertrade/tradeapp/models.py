from django.db import models


class React(models.Model):
    trader = models.CharField(max_length=30)