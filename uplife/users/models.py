from authtools.models import AbstractNamedUser


class User(AbstractNamedUser):
    @property
    def first_name(self):
        return self.name.split()[0]
    
    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"