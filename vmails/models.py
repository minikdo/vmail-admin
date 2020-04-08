from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from passlib.hash import sha512_crypt


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified``
    and ``created_by`` fields.
    """

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey(User, default=1,
                                   on_delete=models.SET_NULL,
                                   null=True)

    class Meta:
        abstract = True


class Domain(TimeStampedModel):
    domain = models.CharField(max_length=64)

    def __str__(self):
        return self.domain


class Mailbox(TimeStampedModel):
    username = models.CharField(max_length=32, help_text='without @')
    domain = models.ForeignKey('Domain', on_delete=models.CASCADE)
    realname = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=500)

    class Meta:
        unique_together = ['username', 'domain']
        ordering = ['username']

    def clean(self):
        if "@" in self.username:
            raise ValidationError({'username': 'only username without @'})

    def save(self, *args, **kwargs):
        self.password = sha512_crypt.encrypt(self.password)
        self.password = "{SHA512-CRYPT}" + self.password

        super().save(*args, *kwargs)

    def __str__(self):
        return "{} ({}@{})".format(self.realname, self.username,
                                   self.domain.domain)


class Alias(TimeStampedModel):
    alias = models.CharField(max_length=32, help_text='without @')
    mailbox = models.ForeignKey('Mailbox', on_delete=models.CASCADE)

    def __str__(self):
        return "{} -> {}".format(self.alias, self.mailbox)
