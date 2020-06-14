# Built-in imports.
from uuid import uuid4
from datetime import datetime, timedelta

# Django imports.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Local imports.
from accounts.managers import UserManager

# Third party imports.
from jwt import encode as jwt_encode


class User(AbstractBaseUser, PermissionsMixin):
    u_id = models.UUIDField(default=uuid4, editable=False)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125, null=True, blank=True)
    email = models.EmailField(max_length=75, db_index=True, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.
        """

        return self.email

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().
        """

        return self._generate_jwt_token()

    @classmethod
    def by_uid(self, uid):
        qs = self.objects.filter(u_id=uid)
        if qs.exists():
            return qs.first()
        return None

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """

        dt = datetime.now() + timedelta(days=60)
        token = jwt_encode(dict(
            id=self.pk, exp=int(dt.strftime('%s'))
        ), settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')