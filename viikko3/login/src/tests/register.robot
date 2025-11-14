*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  jorma
    Set Password And Confirmation  huuha123
    Click Button  Register
    Registering Should Succeed

Register With Too Short Username And Valid Password
    Set Username  jo
    Set Password And Confirmation  huuha123
    Click Button  Register
    Registering Should Not Succeed
    Page Should Contain  at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  jorma
    Set Password And Confirmation  huuha1
    Click Button  Register
    Registering Should Not Succeed
    Page Should Contain  at least 8 characters

Register With Valid Username And Invalid Password
    Set Username  jorma
    Set Password And Confirmation  huuhaahuu
    Click Button  Register
    Registering Should Not Succeed
    Page Should Contain  one non-letter character

Register With Nonmatching Password And Password Confirmation
    Set Username  jorma
    Set Password  huuhaa123
    Set Password Confirmation  haahuu123
    Click Button  Register
    Registering Should Not Succeed
    Page Should Contain  Incorrect password confirmation

Register With Username That Is Already In Use
    Set Username  testman
    Set Password And Confirmation  huuhaa123
    Click Button  Register
    Registering Should Not Succeed
    Page Should Contain  Username already in use

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Set Password And Confirmation
    [Arguments]  ${password}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password}

Registering Should Succeed
    Welcome Page Should Be Open

Registering Should Not Succeed
    Register Page Should Be Open


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  testman  test123123
    Go To  ${REGISTER_URL}