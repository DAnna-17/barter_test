from django.db import models
from django.utils import timezone


class Ad(models.Model):  # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
    # id = models.DecimalField(primary_key=True, auto_created=True, max_digits=100, decimal_places=0)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.TextField()
    category = models.TextField()
    condition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):  # С помощью функции меняем то, как будет представлена запись в модели.
        return self.title  # Указываем, что она будет идентифицироваться с помощью своего заголовка.

    class Meta:
        verbose_name_plural = "Ads"



class ExchangeProposal(models.Model):  # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
    statuses_list = ((-1, 'отклонена'), (1, 'принята'), (0, 'ожидает'))

    # id = models.DecimalField(primary_key=True, auto_created=True, max_digits=100, decimal_places=0)
    ad_sender = models.ForeignKey('Ad', on_delete=models.CASCADE, related_name='senders')
    ad_receiver = models.ForeignKey('Ad', on_delete=models.CASCADE, related_name='receivers')
    comment = models.TextField()
    status = models.CharField(choices=statuses_list, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # С помощью функции меняем то, как будет представлена запись в модели.
        return self.title  # Указываем, что она будет идентифицироваться с помощью своего заголовка.

    def proceed1(self):
        self.status = -1
    def proceed2(self):
        self.status = 1
    def proceed3(self):
        self.status = 0

    class Meta:
        verbose_name_plural = "Entries"


