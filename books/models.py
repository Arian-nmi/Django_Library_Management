from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title


# todo:تمرین اضافه کردن فایل و اد کردن آن در گیت هاب git add   git commit   git push