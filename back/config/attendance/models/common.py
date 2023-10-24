from django.db import models


class BaseModel(models.Model):
    rdate = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
        verbose_name="생성일",
        help_text="데이터 생성일"
    )
    mdate = models.DateField(
        auto_now_add=True,
        blank=True,
        null=False,
        verbose_name="수정일",
        help_text="데이터 수정일"
    )

    class Meta:
        abstract = True
