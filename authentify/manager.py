
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, name, last_name, birth_date, password = None):
        user = self.model(
            email = self.normalize_email(email),
            name = name, 
            last_name = last_name,
            birth_date = birth_date, 
        )

        user.set_password(password)
        
        user.save()

        return user

    def create_superuser(self, email, name, last_name, birth_date, password):
        user = self.create_user(
            email = email,
            name = name, 
            last_name = last_name,
            password = password,
            birth_date = birth_date, 
            )
        
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save()

        return user