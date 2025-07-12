__all__ = (
    "StudyDirection",
    "StudyLanguage",
    "StudyForm",
    "User",
    "PassportData",
    "StudyInfo",
    "Application",
    "AMOCrmLead",
    "EducationType",
    "StudyType",
)


from .admin.study_direction import StudyDirection
from .admin.study_lenguage import StudyLanguage
from .admin.study_form import StudyForm
from .user import User
from .passport_data import PassportData
from .study_info import StudyInfo
from .application import Application
from .admin.study_type import StudyType
from .crm import AMOCrmLead
from .admin.education_type import EducationType

