from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Branch(models.Model):
    bank = models.ForeignKey('banks.Bank', related_name='get_branches', on_delete=models.CASCADE)
    ifsc = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    state = models.CharField(max_length=250)

    def __str__(self):
        return f"{str(self.bank)}:{self.branch}"
