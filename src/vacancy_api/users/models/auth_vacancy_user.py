"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, Group, Permission
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from .auth_vacancy_level import VacancyLevel
from lib.convert import *
from lib.functions import *


class VacancyUser(AbstractBaseUser, PermissionsMixin):
    """
    空室情報ユーザ
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        db_column='username',
        max_length=150,
        unique=True,
        db_index=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    display_name = models.CharField(_('display_name'), db_column='display_name', max_length=100, null=True, blank=True)
    email = models.EmailField(_('email address'), db_column='email', null=True, blank=True)
    is_staff = models.BooleanField(_('staff status'), db_column='is_staff', default=False)
    is_active = models.BooleanField(_('active'), db_column='is_active', default=True)
    is_company = models.BooleanField(_('company'), db_column='is_company', default=False)

    level = models.ForeignKey(
        VacancyLevel,
        db_column='level_id',
        related_name='vacancy_user_levels',
        db_index=True,
        on_delete=models.PROTECT,
        default=3,
    )

    allow_org_image = models.BooleanField(_('allow_org_image'), db_column='allow_org_image', default=False)
    trader_name = models.CharField(_('trader_name'), db_column='trader_name', max_length=100, null=True, blank=True)
    trader_department_name = models.CharField(_('trader_department_name'), db_column='trader_department_name', max_length=100, null=True, blank=True)
    trader_department_tel = models.CharField(_('trader_department_tel'), db_column='trader_department_tel', max_length=20, null=True, blank=True)
    trader_department_address = models.CharField(_('trader_department_address'), db_column='trader_department_address', max_length=255, null=True, blank=True)
    note = models.CharField(_('note'), db_column='note', max_length=255, null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), db_column='date_joined', default=timezone.now)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('vacancy groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="vacancy_user_set",
        related_query_name="vacancy_user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('vacancy user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="vacancy_user_set",
        related_query_name="vacancy_user",
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        managed = False
        db_table = 'auth_vacancy_user'
        verbose_name = _('vacancy_user')
        verbose_name_plural = _('vacancy_users')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)

    @property
    def full_name(self):
        return self.get_full_name()

    @property
    def is_trader(self):
        return not self.is_company

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.display_name

    def get_short_name(self):
        return self.display_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


