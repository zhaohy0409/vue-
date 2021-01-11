from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=30)
    userpassword=models.CharField(max_length=64)
    age=models.IntegerField()
    salay=models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'

    def __str__(self):
        return self.username