# from tkinter import CASCADE
# from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    categoryId = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=20)

class Questions(models.Model):
    qId = models.CharField(max_length=20, primary_key=True)
    question = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Responses(models.Model):
    class Options(models.IntegerChoices):
        VeryInaccurate = 1
        ModeratelyInaccurate = 2
        Neutral = 3
        ModeratelyAccurate = 4
        VeryAccurate = 5
    ext_1 = models.IntegerField(choices=Options.choices)
    ext_2 = models.IntegerField(choices=Options.choices)
    ext_3 = models.IntegerField(choices=Options.choices)
    ext_4 = models.IntegerField(choices=Options.choices)
    ext_5 = models.IntegerField(choices=Options.choices)
    ext_6 = models.IntegerField(choices=Options.choices)
    ext_7 = models.IntegerField(choices=Options.choices)
    ext_8 = models.IntegerField(choices=Options.choices)
    ext_9 = models.IntegerField(choices=Options.choices)
    ext_10 = models.IntegerField(choices=Options.choices)
    nrt_1 = models.IntegerField(choices=Options.choices)
    nrt_2 = models.IntegerField(choices=Options.choices)
    nrt_3 = models.IntegerField(choices=Options.choices)
    nrt_4 = models.IntegerField(choices=Options.choices)
    nrt_5 = models.IntegerField(choices=Options.choices)
    nrt_6 = models.IntegerField(choices=Options.choices)
    nrt_7 = models.IntegerField(choices=Options.choices)
    nrt_8 = models.IntegerField(choices=Options.choices)
    nrt_9 = models.IntegerField(choices=Options.choices)
    nrt_10 = models.IntegerField(choices=Options.choices)
    agr_1 = models.IntegerField(choices=Options.choices)
    agr_2 = models.IntegerField(choices=Options.choices)
    agr_3 = models.IntegerField(choices=Options.choices)
    agr_4 = models.IntegerField(choices=Options.choices)
    agr_5 = models.IntegerField(choices=Options.choices)
    agr_6 = models.IntegerField(choices=Options.choices)
    agr_7 = models.IntegerField(choices=Options.choices)
    agr_8 = models.IntegerField(choices=Options.choices)
    agr_9 = models.IntegerField(choices=Options.choices)
    agr_10 = models.IntegerField(choices=Options.choices)
    csn_1 = models.IntegerField(choices=Options.choices)
    csn_2 = models.IntegerField(choices=Options.choices)
    csn_3 = models.IntegerField(choices=Options.choices)
    csn_4 = models.IntegerField(choices=Options.choices)
    csn_5 = models.IntegerField(choices=Options.choices)
    csn_6 = models.IntegerField(choices=Options.choices)
    csn_7 = models.IntegerField(choices=Options.choices)
    csn_8 = models.IntegerField(choices=Options.choices)
    csn_9 = models.IntegerField(choices=Options.choices)
    csn_10 = models.IntegerField(choices=Options.choices)
    opn_1 = models.IntegerField(choices=Options.choices)
    opn_2 = models.IntegerField(choices=Options.choices)
    opn_3 = models.IntegerField(choices=Options.choices)
    opn_4 = models.IntegerField(choices=Options.choices)
    opn_5 = models.IntegerField(choices=Options.choices)
    opn_6 = models.IntegerField(choices=Options.choices)
    opn_7 = models.IntegerField(choices=Options.choices)
    opn_8 = models.IntegerField(choices=Options.choices)
    opn_9 = models.IntegerField(choices=Options.choices)
    opn_10 = models.IntegerField(choices=Options.choices)
