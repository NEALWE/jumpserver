import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from orgs.mixins import OrgModelMixin


class FTPLog(OrgModelMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.CharField(max_length=128, verbose_name=_('User'))
    remote_addr = models.CharField(max_length=15, verbose_name=_("Remote addr"), blank=True, null=True)
    asset = models.CharField(max_length=1024, verbose_name=_("Asset"))
    system_user = models.CharField(max_length=128, verbose_name=_("System user"))
    operate = models.CharField(max_length=16, verbose_name=_("Operate"))
    filename = models.CharField(max_length=1024, verbose_name=_("Filename"))
    is_success = models.BooleanField(default=True, verbose_name=_("Success"))
    date_start = models.DateTimeField(auto_now_add=True)


class OperateLog(OrgModelMixin):
    ACTION_CREATE = 'create'
    ACTION_UPDATE = 'update'
    ACTION_DELETE = 'delete'
    ACTION_CHOICES = (
        (ACTION_CREATE, _("Create")),
        (ACTION_UPDATE, _("Update")),
        (ACTION_DELETE, _("Delete"))
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.CharField(max_length=128, verbose_name=_('User'))
    action = models.CharField(max_length=16, verbose_name=_("Action"))
    resource_type = models.CharField(max_length=64, verbose_name=_("Resource Type"))
    resource = models.CharField(max_length=128, verbose_name=_("Resource"))
    remote_addr = models.CharField(max_length=15, verbose_name=_("Remote addr"), blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<{}> {} <{}>".format(self.user, self.action, self.resource)
