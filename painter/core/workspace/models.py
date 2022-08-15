import uuid as uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True


class WorkSpace(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=True, unique=True, primary_key=True)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/', null=False, max_length=255)

    class Meta:
        db_table = 'workspaces'
        verbose_name = _('Workspace')
        verbose_name_plural = _('Workspaces')

    def __str__(self):
        return self.title

    def __repr__(self):
        return 'Image(%s, %s)' % (self.title, self.image)

#
# class Resource(models.Model):
#
#     workspace = models.OneToOneField(WorkSpace,
#                                      blank=False,
#                                      null=False,
#                                      related_name="resources",
#                                      related_query_name="resource",
#                                      on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'workspace_resources'
#         verbose_name = _('Resource')
#         verbose_name_plural = _('Resources')
