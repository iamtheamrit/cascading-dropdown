from django.db import models

# Create your models here.

class DateTimeStampedAbstractModel(models.Model):
    """
    An abstract base class model that provides self-populating 'created_on' and 'modified_on' fields. 
    """
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True