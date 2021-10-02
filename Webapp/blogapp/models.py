from django.db import models

METH = (
	('economics','Economics'),
	('lifestyle','Lifestyle'),
	('politics','Politics'),
)



class BlogModel(models.Model):
    title   = models.CharField(max_length=100,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    method  = models.CharField(max_length=40,default='Bengaluru',choices=METH)
    approved = models.BooleanField(default=False)