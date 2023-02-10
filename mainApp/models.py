from django.db import models
class portfolio(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mob = models.CharField(max_length=15)
    domain = models.CharField(max_length=30)
    disc = models.TextField()
    experience = models.CharField(max_length=10)
    address = models.CharField(max_length=60)
    resume = models.FileField(upload_to="resume")
    pic1 = models.ImageField(upload_to="picture_raunak")
    pic2 = models.ImageField(upload_to="picture_raunak")
    pic3 = models.ImageField(upload_to="picture_raunak")
    def __str__(self):
        return self.name    
class education(models.Model):
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    college = models.CharField(max_length=30)
    marks = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class service(models.Model):
    name = models.CharField(max_length=30) 
    field = models.CharField(max_length=20)
    serveice1 = models.CharField(max_length=20) 
    serveice2 = models.CharField(max_length=20,null=True,blank=True)
    serveice3 = models.CharField(max_length=20,null=True,blank=True)
    serveice4 = models.CharField(max_length=20,null=True,blank=True)
    serveice5 = models.CharField(max_length=20,null=True,blank=True)  
    def __str__(self):
        return self.name
# Create your models here.
