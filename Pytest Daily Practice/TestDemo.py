'''
Pytest is unit testing framework.

The rules are ->
    1. File should start or end with "test_ or Test"
    2. Function should start with "test_"
    3. Class should start with "Test"

When we follow these rules pytest will automatically recognize these files, class and functions,
So without giving function call we can execute the test function
And w/o creating object we can execute the test class

-v -> verbosity -> Gives detailed description of the code
-s -> scripting -> Will print all the print statements

Note: Pytest can not recognize the files, functions, class which are not following these rules
'''


#----------------------------------------Function Based-----------------------------------------
# def test_registration() :
#     print('Registering....')
# def test_login() :
#     print('Logging in ...')
# def test_logout() :
#     print('Logging out ...')


#--------------------------------------Class Based----------------------------------------------
# class Test_Demo:
#     def test_register(self):
#         print('Registering...')
#     def test_login(self):
#         print('Login...')
#     def test_logout(self):
#         print('Logout...')
