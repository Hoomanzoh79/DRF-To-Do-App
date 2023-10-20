from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User,Profile
from task.models import Task
import random


my_task_list = [
'cook dinner','study for exam','go to the gym',
'eat lunch','play football','watch movie',
'buy laptop','go out with friends','take a walk','learn programming',]

class Command(BaseCommand):
    def __init__(self,*args,**kwargs):
        super(Command,self).__init__(*args,**kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(),password='Test@123456')
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.bio = self.fake.paragraph(nb_sentences=5)
        profile.save()

        # create 10 random tasks
        for _ in range(10):
            Task.objects.create(
                author=profile,
                is_done=False,
                title=random.choice(my_task_list),
            )