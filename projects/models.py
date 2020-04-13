from django.db import models

class Project(models.Model):

    titel = models.CharField(max_length=100, default='')
    omschrijving = models.TextField()
    ingredient = models.TextField()
#    afbeelding = models.ImageField(upload_to='media')
    created_on = models.DateTimeField(auto_now_add=True)    
    
    
    def __str__(self):
        return self.titel
    def first_image(self):
    # code to determine which image to show. The First in this case.
        return self.images[0]
    def second_image(self):
    # code to determine which image to show. The First in this case.
        return self.images[1]
    def third_image(self):
    # code to determine which image to show. The First in this case.
        return self.images[2]

    
class ProjectImage(models.Model):
    property = models.ForeignKey(Project, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
