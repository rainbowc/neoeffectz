from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=500,blank=True, null=True )
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    message = models.CharField(max_length=1000, blank=True, null=True)
    

    def save(self, *args, **kwargs):
        if not self.subject:  
            self.subject = self.email  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subject