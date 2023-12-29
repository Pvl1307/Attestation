from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)
