from django.db import models


# Create your models here.
class Area(models.Model):
    """省市区"""
    name = models.CharField(max_length=20, verbose_name='名称')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='subs', null=True, blank=True,
                               verbose_name='上级行政区划')

    class Meta:
        db_table = 'tb_areas'  ## 指明数据库表名
        verbose_name = '省市区'  ## 在admin站点中显示的名称
        verbose_name_plural = '省市区'  # # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
