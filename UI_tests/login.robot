*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Check main page
    Open Browser  http://127.0.0.1:8080/login  Chrome
    Maximize Browser Window
    Get WebElement  name:username
    Input Text  name:username  user1
    Get WebElement  name:password
    Input Text  name:password  1
    #Click Element       //*[contains(text(),'Log In')]
    submit form
#    Close Window