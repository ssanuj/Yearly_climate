from django.db import models


class Area_desc(models.Model):
    """
    Area and what data you require
    """
    name = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.name

class Temp_record(models.Model):
    """

    Temperatures table with data transposed from all the tables

    """
    #Fields
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    month1 = models.FloatField()
    month2 = models.FloatField()
    month3 = models.FloatField()
    month4 = models.FloatField()
    month5 = models.FloatField()
    month6 = models.FloatField()
    month7 = models.FloatField()
    month8 = models.FloatField()
    month9 = models.FloatField()
    month10 = models.FloatField()
    month11 = models.FloatField()
    month12 = models.FloatField()
    winter = models.FloatField()
    spring = models.FloatField()
    summer = models.FloatField()
    autumn = models.FloatField()
    annual = models.FloatField()
    min_temp = models.FloatField()
    max_temp = models.CharField(max_length=1)
    mean_temp = models.CharField(max_length=1)
    rainfall = models.CharField(max_length=1)
    sunshine = models.CharField(max_length=1)
    area = models.ForeignKey(Area_desc, on_delete=models.CASCADE)

    def __str___(self):
        return self.year + ' - ' + self.month + ' - ' + self.max_temp

