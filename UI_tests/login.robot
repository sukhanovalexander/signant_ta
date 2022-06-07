*** Settings ***
Resource  resources.robot

*** Test Cases ***
Login with non-existing user
    Open Browser  ${login_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user1}[password]
    Click button  Log In
    ${url}=  Get Location
    Should Be Equal  ${url}  ${error_url}
    Close Window

Register missing user
    Open Browser  ${register_url}  ${browser}
#    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user1}[password]
    Input text  ${fnfield}  ${user1}[firstname]
    Input text  ${lnfield}  ${user1}[lastname]
    Input text  ${phfield}  ${user1}[phone]
    Click button  Register
    ${url}=  Get Location
    Should Be Equal  ${url}  ${register_url}
    Close Window

Register missing password
    Open Browser  ${register_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
#    Input text  ${passfield}  ${user1}[password]
    Input text  ${fnfield}  ${user1}[firstname]
    Input text  ${lnfield}  ${user1}[lastname]
    Input text  ${phfield}  ${user1}[phone]
    Click button  Register
    ${url}=  Get Location
    Should Be Equal  ${url}  ${register_url}
    Close Window

Register missing firstname
    Open Browser  ${register_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user1}[password]
#    Input text  ${fnfield}  ${user1}[firstname]
    Input text  ${lnfield}  ${user1}[lastname]
    Input text  ${phfield}  ${user1}[phone]
    Click button  Register
    ${url}=  Get Location
    Should Be Equal  ${url}  ${register_url}
    Close Window

Register missing lastname
    Open Browser  ${register_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user1}[password]
    Input text  ${fnfield}  ${user1}[firstname]
#    Input text  ${lnfield}  ${user1}[lastname]
    Input text  ${phfield}  ${user1}[phone]
    Click button  Register
    ${url}=  Get Location
    Should Be Equal  ${url}  ${register_url}
    Close Window

Register missing phone
    Open Browser  ${register_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user1}[password]
    Input text  ${fnfield}  ${user1}[firstname]
    Input text  ${lnfield}  ${user1}[lastname]
#    Input text  ${phfield}  ${user1}[phone]
    Click button  Register
    ${url}=  Get Location
    Should Be Equal  ${url}  ${register_url}
    Close Window

Register user1
    Open Browser  ${register_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user1}[password]
    Input text  ${fnfield}  ${user1}[firstname]
    Input text  ${lnfield}  ${user1}[lastname]
    Input text  ${phfield}  ${user1}[phone]
    Click button  Register
    ${url}=  Get Location
    Should Be Equal  ${url}  ${login_url}
    Close Window

Register user1 again
    Open Browser  ${register_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user1}[password]
    Input text  ${fnfield}  ${user1}[firstname]
    Input text  ${lnfield}  ${user1}[lastname]
    Input text  ${phfield}  ${user1}[phone]
    Click button  Register
    ${url}=  Get Location
    Should Be Equal  ${url}  ${register_url}
    Close Window

Login with valid user
    Open Browser  ${login_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user1}[password]
    Click button  Log In
    ${url}=  Get Location
    Should Be Equal  ${url}  ${user_url}
    Close Window

Add second user
    Open Browser  ${register_url}  ${browser}
    Input text  ${userfield}  ${user2}[username]
    Input text  ${passfield}  ${user2}[password]
    Input text  ${fnfield}  ${user2}[firstname]
    Input text  ${lnfield}  ${user2}[lastname]
    Input text  ${phfield}  ${user2}[phone]
    Click button  Register
    ${url}=  Get Location
    Should Be Equal  ${url}  ${login_url}
    Close Window

Login with other user password
    Open Browser  ${login_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user2}[password]
    Click button  Log In
    ${url}=  Get Location
    Should Be Equal  ${url}  ${error_url}
    Close Window

Login with empty password
    Open Browser  ${login_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
#    Input text  ${passfield}  ${user1}[password]
    Click button  Log In
    ${url}=  Get Location
    Should Be Equal  ${url}  ${login_url}
    Close Window

Login with empty username
    Open Browser  ${login_url}  ${browser}
#    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user2}[password]
    Click button  Log In
    ${url}=  Get Location
    Should Be Equal  ${url}  ${login_url}
    Close Window

Login with all fields empty
    Open Browser  ${login_url}  ${browser}
#    Input text  ${userfield}  ${user1}[username]
#    Input text  ${passfield}  ${user2}[password]
    Click button  Log In
    ${url}=  Get Location
    Should Be Equal  ${url}  ${login_url}
    Close Window



#Create user
#    Open Browser  http://127.0.0.1:8080/login  ${BROWSER}
#    Input Text  name:username  user1
#    Input Text  name:password  1
    #Click Element       //*[contains(text(),'Log In')]
#    submit form
#    Close Window