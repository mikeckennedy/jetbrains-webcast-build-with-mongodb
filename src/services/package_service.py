from typing import Optional, List

from data.downloads import Download
from data.packages import Package
from data.release_history import ReleaseHistory
from data.users import User


class PackageService:
    @classmethod
    def package_count(cls):
        return Package.objects().count()

    @classmethod
    def release_count(cls):
        return ReleaseHistory.objects().count()

    @classmethod
    def user_count(cls):
        return User.objects().count()

    @classmethod
    def download_count(cls):
        return Download.objects().count()

    @classmethod
    def find_package_by_name(cls, name):
        package = Package.objects(name=name).first()
        return package

    @classmethod
    def latest_release(cls, package: Package) -> Optional[ReleaseHistory]:
        release = ReleaseHistory \
            .objects(package_id=package.id) \
            .order_by('-created') \
            .first()

        return release

    @classmethod
    def find_maintainers(cls, package: Package) -> List[User]:
        users = User.objects(id__in=package.maintainers)
        return list(users)

    @classmethod
    def popular_packages(cls, limit: int) -> List[Package]:
        packages = Package.objects()\
            .order_by('-total_downloads')\
            .limit(limit)

        return list(packages)
