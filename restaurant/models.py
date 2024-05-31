from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateField()

    class Meta:
        ordering = ['booking_date']

    def __str__(self) -> str:
        return self.name
    

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


