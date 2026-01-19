from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    birth = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    image = models.FileField(upload_to="public", null=True)

    def __str__(self):
        return self.name + " " + self.lastname

    UsersList = models.ForeignKey(
        "UsersList", null=False, on_delete=models.CASCADE
    )  # CASCADE, si on éfface la liste on éfface tous les users associés


class UsersList(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self): # afficher le nom de la liste dans l'admin et le filtre de Users par UsersList
        return self.name
    
    class Meta:
        verbose_name = "User List"
        verbose_name_plural = "Users List"
