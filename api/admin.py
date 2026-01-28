from django.contrib import admin

from .models import User, UsersList, Season, Episode, Actor, ActorsList


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

@admin.register(Season)
class SeasonsAdmin(admin.ModelAdmin):
    list_display = ("name", "year")
    ordering = ("name",)

@admin.register(Episode)
class EpisodesAdmin(admin.ModelAdmin):
    list_display = ("title", "name", "duration", "season")
    ordering = ("name",)

    list_filter = ("season", )  # filtrer par saison
    search_fields = ("name", "title")  # recherche par nom ou titre

class ActorInline(admin.TabularInline):  # afficher tous les acteurs dans ActorsList
    model = Actor
    extra = 1  # ajouter un acteur supplémentaire vide dans l'admin par défaut

@admin.register(ActorsList)
class ActorsListAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = (ActorInline,)

@admin.register(Actor)
class ActorsAdmin(admin.ModelAdmin):
    list_display = ("actor_name", "name", "lastname", "image", "season")
    ordering = ("actor_name",)

    list_filter = ("season", "ActorsList")  # filtrer par saison
    search_fields = ("actor_name",)  # recherche par nom     