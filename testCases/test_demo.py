from testCases.test_login import Test_admin_Login
from testCases.RecruitmentRequest.test_addRecruitmentRequest import Test_Add_Recruitment_Request
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.HiringManagerPage import HiringManager

class Test_Demo:

    Test_Add_Recruitment_Request.test_addRecruitmentRequest_login('self','setup')
    Test_Add_Recruitment_Request.test_addRecruitmentRequest('self','setup')

