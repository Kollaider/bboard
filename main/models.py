from django.db import models
from django.contrib.auth.models import AbstractUser

class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацю?')
    send_messages = models.BooleanField(default=True, verbose_name='Слать оповещения о новых комментариях?')

    # def delete(self, *args, **kwargs):
    #     for bb in self.bb_set.all():
    #         bb.delete()
    #     super().delete(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        pass

# Create your models here.
