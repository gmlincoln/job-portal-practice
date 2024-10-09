from django.contrib import admin

from Job_Portal_App.models import User_Model

# Register your models here.

@admin.register(User_Model)
class User_Model_Display(admin.ModelAdmin):

    list_display = ('username', 'first_name', 'last_name', 'email', 'user_type')