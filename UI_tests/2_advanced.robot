*** Settings ***
Resource  resources.robot


# This test set should be executed after 1_basic.robot tests
*** Test Cases ***
Login check data
    Open Browser  ${login_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user1}[password]
    Click button  Log In
    ${url}=  Get Location
    Should Be Equal  ${url}  ${user_url}
    ${rowCount}=    Get Element Count  //*[@id="content"]/tbody/tr
    Should Be Equal  ${rowCount}  ${5}
    FOR   ${rowIndex}  IN RANGE  2  ${rowCount} + 1
     ${curText}      Get Text     //*[@id="content"]/tbody/tr[${rowIndex}]/td[${2}]
     ${temp}=  Evaluate  $rowIndex - 2
     Should Be Equal  ${curText}  ${user1_np}[${temp}]  # checks that exported data is as expected
    END
    Close Window


Login check logout check
    Open Browser  ${login_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user1}[password]
    Click button  Log In
    ${url}=  Get Location
    Should Be Equal  ${url}  ${user_url}
    ${rowCount}=    Get Element Count  //*[@id="content"]/tbody/tr
    Should Be Equal  ${rowCount}  ${5}
    FOR   ${rowIndex}  IN RANGE  2  ${rowCount} + 1
     ${curText}      Get Text     //*[@id="content"]/tbody/tr[${rowIndex}]/td[${2}]
     ${temp}=  Evaluate  $rowIndex - 2
     Should Be Equal  ${curText}  ${user1_np}[${temp}]  # checks that exported data is as expected
    END
    Click link  xpath://html/body/nav/ul/li[2]/a
    ${rowCount}=    Get Element Count  //*[@id="content"]/tbody/tr
    Should Be Equal  ${rowCount}  ${0}
    Close Window


Login check logout check login
    Open Browser  ${login_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user1}[password]
    Click button  Log In
    ${url}=  Get Location
    Should Be Equal  ${url}  ${user_url}
    ${rowCount}=    Get Element Count  //*[@id="content"]/tbody/tr
    Should Be Equal  ${rowCount}  ${5}
    FOR   ${rowIndex}  IN RANGE  2  ${rowCount} + 1
     ${curText}      Get Text     //*[@id="content"]/tbody/tr[${rowIndex}]/td[${2}]
     ${temp}=  Evaluate  $rowIndex - 2
     Should Be Equal  ${curText}  ${user1_np}[${temp}]  # checks that exported data is as expected
    END
    Click link  xpath://html/body/nav/ul/li[2]/a
    ${rowCount}=    Get Element Count  //*[@id="content"]/tbody/tr  # no table with data
    Should Be Equal  ${rowCount}  ${0}
    #  Logging in as user2
    Click link  xpath://html/body/nav/ul/li[2]/a
    Input text  ${userfield}  ${user2}[username]
    Input text  ${passfield}  ${user2}[password]
    Click button  Log In
    ${url}=  Get Location
    Should Be Equal  ${url}  ${user_url}
    ${rowCount}=    Get Element Count  //*[@id="content"]/tbody/tr
    Should Be Equal  ${rowCount}  ${5}
    FOR   ${rowIndex}  IN RANGE  2  ${rowCount} + 1
     ${curText}      Get Text     //*[@id="content"]/tbody/tr[${rowIndex}]/td[${2}]
     ${temp}=  Evaluate  $rowIndex - 2
     Should Be Equal  ${curText}  ${user2_np}[${temp}]  # checks that exported data is as expected
    END
    Close Window

Register login check
    Open Browser  ${register_url}  ${browser}
    Input text  ${userfield}  ${user3}[username]
    Input text  ${passfield}  ${user3}[password]
    Input text  ${fnfield}  ${user3}[firstname]
    Input text  ${lnfield}  ${user3}[lastname]
    Input text  ${phfield}  ${user3}[phone]
    Click button  Register
    ${url}=  Get Location
    Should Be Equal  ${url}  ${login_url}

    Click link  xpath://html/body/nav/ul/li[2]/a
    Input text  ${userfield}  ${user3}[username]
    Input text  ${passfield}  ${user3}[password]
    Click button  Log In
    ${rowCount}=    Get Element Count  //*[@id="content"]/tbody/tr
    FOR   ${rowIndex}  IN RANGE  2  ${rowCount} + 1
     ${curText}      Get Text     //*[@id="content"]/tbody/tr[${rowIndex}]/td[${2}]
     ${temp}=  Evaluate  $rowIndex - 2
     Should Be Equal  ${curText}  ${user3_np}[${temp}]  # checks that exported data is as expected
    END
    Close Window

Error try again login
    Open Browser  ${login_url}  ${browser}
    Input text  ${userfield}  ${user1}[username]
    ${pass}=  Generate Random String  5-10
    Input text  ${passfield}  ${pass}
    Click button  Log In
    ${url}=  Get Location
    Should Be Equal  ${url}  ${error_url}

    Click link  xpath://html/body/nav/ul/li[2]/a
    Input text  ${userfield}  ${user1}[username]
    Input text  ${passfield}  ${user1}[password]
    Click button  Log In
    ${url}=  Get Location
    Should Be Equal  ${url}  ${user_url}
    ${rowCount}=    Get Element Count  //*[@id="content"]/tbody/tr
    FOR   ${rowIndex}  IN RANGE  2  ${rowCount} + 1
     ${curText}      Get Text     //*[@id="content"]/tbody/tr[${rowIndex}]/td[${2}]
     ${temp}=  Evaluate  $rowIndex - 2
     Should Be Equal  ${curText}  ${user1_np}[${temp}]  # checks that exported data is as expected
    END
    Close Window
