from django.db import models

# Create your models here.

# user model
class User(models.Model):
    username=models.CharField(max_length=150,primary_key=True)
    name=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    profile_bio=models.CharField(max_length=150,null=True)
    last_login=models.DateTimeField(null=True)
    last_logout=models.DateTimeField(null=True)
    username.primary_key
    def __str__(self):
        return self.username
    
# connections model
class Connections(models.Model):
    id=models.IntegerField(null=True)
    connection_id=models.CharField(max_length=200,primary_key=True)
    user1=models.ForeignKey(User,to_field="username", related_name="user1",on_delete=models.CASCADE)
    user2=models.ForeignKey(User,to_field="username", related_name="user2",on_delete=models.CASCADE)
    def __str__(self):
        return self.connection_id
    
# messages model
class Messages(models.Model):
    timestamp=models.DateTimeField(null=True,auto_now_add=True)
    connection_id=models.ForeignKey(Connections,to_field="connection_id", on_delete=models.CASCADE)
    message=models.CharField(max_length=200,blank=True,null=False)
    sender=models.ForeignKey(User,to_field="username", on_delete=models.CASCADE)
    
class UserProfilePic(models.Model):
    username=models.ForeignKey(User,to_field="username", related_name="user_name",on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to="images/",default="images/default.jpg")