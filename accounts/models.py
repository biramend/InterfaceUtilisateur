from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save

from InterfaceUtilisateur import settings


class MyUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Veillez donner un email valide")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


# Create your models here.
class CustomerUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    objects = MyUserManager()
    # blank=False pour dire que le numéro  ne doit pas etre nul

    USERNAME_FIELD = "email"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

"""
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCAD)


def poset_save_receive(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(poset_save_receive, sender=settings.AUTH_USER_MODEL)



"""
# Une class profile qui va nous permettre  par exemple de distinguer un client et un vendeur dans un site
