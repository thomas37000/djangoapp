from django.contrib import admin

from .models import User, UsersList


class UserInline(admin.TabularInline):  # afficher tous les users dans UserList
    model = User
    extra = 1  # ajouter un user supplémentaire vide dans l'admin par défaut


@admin.register(UsersList)
class UsersListAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = (UserInline,)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "lastname",
        "email",
        "age",
        "UsersList",
    )  # list_display affiche les champs de la table

    list_filter = ("UsersList", )  # filtrer par UsersList
    search_fields = ("name", "email")  # recherche par nom ou email