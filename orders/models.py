from django.db import models
from products.models import Product
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from accounts.models import City, User
from django.core.validators import MaxValueValidator, MinValueValidator , MinLengthValidator
import uuid
from enum import Enum
import os

class Order(models.Model):
  first_name = models.CharField(max_length=60, blank=True, null=True)
  last_name = models.CharField(max_length=60, blank=True, null=True)
  email = models.EmailField()
  phone_regex = RegexValidator(regex=r'^01[1|0|2|5][0-9]{8}$',
                               message="Phone number must match egyptian format")
  phone = models.CharField(validators=[phone_regex], max_length=11,
                           blank=True, null=True,
                           help_text=_('من فضلك ادخل رقم موبايل صحيح'))
  address = models.CharField(max_length=150, blank=True, null=True)
  description = models.TextField(blank=True, null=True)

  city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  #1 in review 2 repleyed with price 3 accepted
  order_status = models.PositiveIntegerField(default=1)

  class Meta:
    ordering = ('-created',)

  def __str__(self):
    return str(self.id) + " - " + "طلب " + self.first_name + " " + self.last_name

  def get_total_cost(self):
    return sum(item.get_cost() for item in self.items.all())





class OrderItem(models.Model):
  order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
  product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
  price = models.FloatField(null=True, blank=True,
    validators=[MinValueValidator(0.0), MaxValueValidator(1000000)],
    
  )
  quantity = models.PositiveIntegerField(default=1)
  ITEM_STATUS_CHOICES = (
    ('r' , "تم رفض اللسعر"),
    ('a' , "تم قبول السعر")
  )
  status = models.CharField(
    choices=ITEM_STATUS_CHOICES,
    max_length=5,
    null=True,
    blank=True
    )
  def __str__(self):
    return "Order : "+str(self.order.id) + "-" + str(self.product)


def get_file_path(instance, filename):
  ext = filename.split('.')[-1]
  filename = "%s.%s" % (uuid.uuid4(), ext)
  return os.path.join('orders/', filename)


class OrderImage(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  img = models.ImageField(upload_to='orders/%Y/%m/%d', blank=True)

  def __str__(self):
    return str(self.order.id)