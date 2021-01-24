from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.hashers import make_password
import random

from apps.users.models import UserProfile, Department
from faker import Faker


class Command(BaseCommand):
    """生成测试用户数据"""
    help = 'generate User Test Data'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        genFakeData = Faker(locale='zh_CN')
        gender = ['男', '女']
        section_list = [section.id for section in Department.objects.raw('select id from department')]
        for entry in range(options['n']):
            s = UserProfile.objects.create(username=genFakeData.name_male(),
                                           password=make_password("12345678"),
                                           email=genFakeData.email(),
                                           sex=random.choice(gender),
                                           department_id=section_list[random.randint(0, len(section_list)-1)],
                                           bg_telephone=genFakeData.phone_number())
            s.save()
        self.stdout.write(self.style.SUCCESS('Successfully Added !'))
