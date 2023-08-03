from django.db import models


class BeFit(models.Model):
    icon_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Light(models.Model):
    description = models.CharField(max_length=50, default=0)
    week = models.CharField(max_length=50)
    icon_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Normal(models.Model):
    description = models.CharField(max_length=50, default=0)
    week = models.CharField(max_length=50)
    icon_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Strong(models.Model):
    description = models.CharField(max_length=50, default=0)
    week = models.CharField(max_length=50)
    icon_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class SuperStrong(models.Model):
    description = models.CharField(max_length=50, default=0)
    week = models.CharField(max_length=50)
    icon_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Super(models.Model):
    description = models.CharField(max_length=50, default=0)
    week = models.CharField(max_length=50)
    icon_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

