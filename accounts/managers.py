# Django imports.
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`. 

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, *arg, **kwargs):
        """
        Create and return a `User` i.e Author
        with an email, username and password.
        """

        email = kwargs.get('email', None)
        password = kwargs.get('password', None)
        first_name = kwargs.get('first_name', None)
        last_name = kwargs.get('last_name', None)

        if not first_name:
            raise TypeError('Users must have first name.')

        if not email:
            raise TypeError('Users must have a email')

        if not password:
            raise TypeError('Users must have a password.')

        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, *args, **kwargs):
        """
        Create and return a `User` with superuser (admin) permissions.
        """

        first_name = kwargs.get('first_name', None)
        if not first_name:
            kwargs['first_name'] = 'Edison Admin'

        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user