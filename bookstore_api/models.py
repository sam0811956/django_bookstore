from django.db import models
from bookstore_api.repository.opening_hour import OpeningHourManager
from bookstore_api.repository.book_store import BookStoreManager
from bookstore_api.repository.book import BookManager
from bookstore_api.repository.user import UserManager
from bookstore_api.repository.purchase import PurchaseManager
# # Create your models here.


class BookStore(models.Model):
    cash_balance = models.FloatField(null=False)
    name = models.CharField(max_length=100, null=False)
    objects = BookStoreManager()

    def __str__(self):
        return '{0} (cash: {1})'.format(self.name, self.cash_balance)

    def weekly_open_hours(self):
        return sum(
            map(
                lambda op_hour_obj: op_hour_obj.open_hours(), self.openinghour_set.all()
            )
        )


class Book(models.Model):
    book_store = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False)
    objects = BookManager()

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
    objects = OpeningHourManager()

    def __str__(self):
        return '{0} ({1}:{2} - {3}:{4})'.format(
            self.week_day, self.start_hour, self.start_min, self.end_hour, self.end_min
        )

    def open_hours(self):
        hour_diff = (self.end_hour + (self.end_min / 60)) - \
            (self.start_hour + (self.start_min / 60))

        return hour_diff + 12 if hour_diff < 0 else hour_diff


class User(models.Model):
    name = models.CharField(max_length=50, null=False)
    cash_balance = models.FloatField(null=False)
    objects = UserManager()

    def __str__(self):
        return '{0} (cash: {1})'.format(self.name, self.cash_balance)


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchasehistory', null=True, blank=True)
    book_name = models.CharField(max_length=200, null=False)
    store_name = models.CharField(max_length=100, null=False)
    transaction_amount = models.FloatField(null=False)
    transaction_date = models.DateTimeField(blank=True, null=True)
    objects = PurchaseManager()

    def __str__(self):
        return 'book: {0}, store: {1}(amount: {2}, date: {3})'.format(
            self.book_name, self.store_name, self.transaction_amount,
            self.transaction_date)
