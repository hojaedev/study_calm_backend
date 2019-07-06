from django.db import models

class ProductDetail(models.Model):

    class Meta:
        db_table = 'Prod_Details'
        verbose_name = 'Listing Service Detail'
        verbose_name_plural = 'Listing Service Details'
    id = models.AutoField(primary_key=True)
    PRODUCT_TYPE = (
        ('room', 'Room'),
        ('seat', 'Seat'),
        ('all', 'All Category')
    )
    act_type = models.CharField(
        max_length=4,
        choices=PRODUCT_TYPE,
        blank=False
    )
    price = models.IntegerField(default=0, blank=True)
    long_name_kr = models.CharField(max_length=50, blank=False)
    long_name_en = models.CharField(max_length=80)
    detail = models.CharField(max_length=100, blank=True, null=True)
    # icon = models.ImageField()

    def __str__(self):
        return self.long_name_kr