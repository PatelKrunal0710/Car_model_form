from django.db import models

class personinfo(models.Model):
    Name = models.CharField(max_length=120)
    Brand = models.CharField(max_length=120)
    completed = models.IntegerField()

    def __str__(self):
        return self.Name


class checklist_master(models.Model):
    view_no = models.IntegerField()
    chk_item = models.CharField(max_length=120)
    chk_type = models.CharField(max_length=120)

    def __str__(self):
        return self.chk_iteam

class docinfo(models.Model):
    chk_list = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    comments = models.CharField(max_length=120,blank=True, null = True)
    
    def __str__(self):
        return self.chk_list