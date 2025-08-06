import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading
#QUestion no.1

@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance,created, **kwargs):
    print("Signal started...")
    time.sleep(5)
    print("Signal finished!")

#Question2
@receiver(post_save, sender=User)
def thread_check_signal(sender, instance, **kwargs):
    print("Signal thread:", threading.current_thread().name)

#Question3
@receiver(post_save, sender=User)
def transaction_test_signal(sender, instance, created, **kwargs):
    print("Signal handler running...")
    raise Exception("Fake error from signal")