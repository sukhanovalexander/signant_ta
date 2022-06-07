*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported SeleniumLibrary.
Library           SeleniumLibrary
Library  Collections
Library  SeleniumLibrary
Variables  variables.py
Library  String

*** Variables ***
#${SERVER}         localhost:8080
#${BROWSER}        Chrome
#${base_url}      http://${SERVER}/
#${login_url}    http://${SERVER}/login
#${REGISTER URL}      http://${SERVER}/register
#${ERROR URL}      http://${SERVER}/error
#${USER URL}      http://${SERVER}/user
#&{user1}=   username=User11  password=Pass11  firstname=Firsname11  lastname=Lastname11  phone=Phone11
#${userfield}  name:username
#${passfield}  name:password
#${fnfield}  name:firstname
#${lnfield}  name:lastname
#${phfield}  name:phone

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Login Page Should Be Open

Error Page

Login Page Should Be Open
    Title Should Be    Login Page

Go To Login Page
    Go To    ${LOGIN URL}
    Login Page Should Be Open

Input Username
    [Arguments]    ${username}
    Input Text    username_field    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password_field    ${password}

Submit Credentials
    Click Button    login_button

Welcome Page Should Be Open
    Location Should Be    ${WELCOME URL}
    Title Should Be    Welcome Page
