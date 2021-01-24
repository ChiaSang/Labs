from django.core.management.base import BaseCommand
import random

from apps.asset.models import Asset, AssetType, AssetStatus
from apps.users.models import UserProfile, Department
from faker import Faker


class Command(BaseCommand):
    """生成测试资产数据"""
    help = 'generate Asset Test Data'

    def add_arguments(self, parser):
        parser.add_argument('n', nargs='+', type=int)

        parser.add_argument(
            '--type',
            action='store_true',
            # 如果参数包含delete则action为True，反之False
            help='Delete poll instead of closing it',
        )
        parser.add_argument(
            '--status',
            action='store_true',
            help='Delete poll instead of closing it',
        )
        parser.add_argument(
            '--section',
            action='store_true',
            help='Delete poll instead of closing it',
        )
        parser.add_argument(
            '--asset',
            action='store_true',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        print(args, options)
        genFakeData = Faker(locale='zh_CN')
        if options['type']:
            for _ in range(options['n'][0]):
                AssetType.objects.create(asset_type=genFakeData.word())
            self.stdout.write(
                self.style.SUCCESS('AssetType Successfully Added !'))
        elif options['section']:
            section = ['技术', '财务', '采购', '人力', '后勤', '生产', '总裁办', '研发']
            for _ in range(len(section) - 1):
                Department.objects.create(dp_name=section[_])
            self.stdout.write(
                self.style.SUCCESS('AssetStatus Successfully Added !'))
        elif options['status']:
            status = ['损坏', '报废', '正常']
            for a_status in status:
                AssetStatus.objects.create(asset_status=a_status)
            self.stdout.write(
                self.style.SUCCESS('AssetStatus Successfully Added !'))
        elif options['asset']:
            type_list = [
                type.id
                for type in AssetType.objects.raw('select id from AssetType')
            ]
            status_list = [
                status.id for status in AssetStatus.objects.raw(
                    'select id from AssetStatus')
            ]
            section_list = [
                section.id for section in Department.objects.raw(
                    'select id from Department')
            ]
            users_list = [user.id for user in UserProfile.objects.all()]
            # 原生sql获取类型id生成一个数组
            for _ in range(options['n'][0]):
                Asset.objects.create(
                    asset_type_id=type_list[random.randint(
                        0,
                        len(type_list) - 1)],
                    asset_status_id=status_list[random.randint(
                        0,
                        len(status_list) - 1)],
                    asset_name=genFakeData.text(random.randint(5, 8)),
                    asset_model=genFakeData.license_plate(),
                    specification=genFakeData.text(16),
                    asset_holder_id=users_list[random.randint(
                        0,
                        len(users_list) - 1)],
                    asset_dep_id=section_list[random.randint(
                        0,
                        len(section_list) - 1)],
                    purchase_time=genFakeData.date(),
                    used_time=random.randint(1, 9),
                    asset_uuid=genFakeData.uuid4(),
                    comment=genFakeData.text(16))
            self.stdout.write(self.style.SUCCESS('Asset Successfully Added !'))
