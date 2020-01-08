from django.db import models


class jobTitle(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class newJob(models.Model):
    
    jobtitle = models.ForeignKey(jobTitle, on_delete = models.CASCADE)
    fulltime = models.BooleanField()
    description = models.TextField()
    location    = models.CharField(max_length=50)
    contact =   models.CharField(max_length=20)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description