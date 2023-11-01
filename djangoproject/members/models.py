from django.db import models

# EA 31 Oct 2023 - Added member model class
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)