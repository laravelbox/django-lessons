from django.contrib import admin
from .models import Member

# Register your models here.

# EA 1 Nov 2023 - Registered member model
#admin.site.register(Member)

# EA 1 Nov 2023 - Set list display for member
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Member, MemberAdmin)