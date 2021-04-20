from django.db import models

# # Create your models here.


class BookStore(models.Model):
    cash_balance = models.FloatField(null=False)
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return '{0} (cash: {1})'.format(self.name, self.cash_balance)


class Book(models.Model):
    book_store = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False)

    def __str__(self):
        return '{0} (price: {1})'.format(self.name, self.price)


class OpeningHour(models.Model):
    class WeekDay(models.TextChoices):
        MON = "Mon", "Monday"
        TUES = "Tues", "Tuesday"
        WED = "Wed", "Wednesday"
        THURS = "Thurs", "Thursday"
        FRI = "Fri", "Friday"
        SAT = "Sat", "Saturday"
        SUN = "Sun", "Sunday"

    book_store = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    week_day = models.CharField(max_length=5, choices=WeekDay.choices)
    start_hour = models.PositiveSmallIntegerField(null=True)
    start_min = models.PositiveSmallIntegerField(null=True)
    end_hour = models.PositiveSmallIntegerField(null=True)
    end_min = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return '{0} ({1}:{2} - {3}:{4})'.format(
            self.week_day, self.start_hour, self.start_min, self.end_hour, self.end_min
        )


class User(models.Model):
    name = models.CharField(max_length=50, null=False)
    cash_balance = models.FloatField(null=False)

    def __str__(self):
        return '{0} (cash: {1})'.format(self.name, self.cash_balance)


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200, null=False)
    store_name = models.CharField(max_length=100, null=False)
    transaction_amount = models.FloatField(null=False)
    transaction_date = models.DateField(null=False)

    def __str__(self):
        return 'book: {0}, store: {1}(amount: {2}, date: {3})'.format(
            self.book_name, self.store_name, self.transaction_amount, self.transaction_date)
