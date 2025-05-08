# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.FloatField()
    category = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    website_link = models.TextField(blank=True, null=True)
    last_updated = models.TextField(blank=True, null=True)  # This field type is a guess.
    
    
    def __str__(self):
        return f"{self.name}"
    
    #leave this as is so i dont overwrite my data
    class Meta:
        managed = False
        db_table = 'grocery_items'
        
