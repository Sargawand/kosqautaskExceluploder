from django.db import models

# Create your models here.
class uploadExcel(models.Model):
    name = models.CharField(max_length=255)
    # excel_file = models.FieldFile(upload='uploaded_excels/')
    excel_file = models.FileField(upload_to='uploaded_excels/')
    upload_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name