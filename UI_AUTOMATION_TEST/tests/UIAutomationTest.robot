*** Settings ***
Library    ${CURDIR}/../lib/WebControler.py    WITH NAME    Website

*** Variables ***
${WEB_URL}    http://localhost:8080
${USERNAME}     tomsmith
${PASSWORD}     SuperSecretPassword!
${INVALID_USERNAME}     tomsmitsaaah
${INVALID_PASSWORD}     SuperSecretPasswordFailed!

*** Test Cases ***

Valid Login Test
    [Documentation]    Verify user can login with valid credentials

    Start Browser
    Login To Website Successfully    ${WEB_URL}    ${USERNAME}    ${PASSWORD}
    [Teardown]    Close Browser

Invalid User Login Test
    [Documentation]    Verify error message appears for invalid credentials
    
    Start Browser
    Login To Website Failed    ${WEB_URL}    ${INVALID_USERNAME}    ${PASSWORD}

    [Teardown]    Close Browser

Invalid Password Login Test
    [Documentation]    Verify error message appears for invalid credentials
    
    Start Browser
    Login To Website Failed    ${WEB_URL}    ${USERNAME}    ${INVALID_PASSWORD}

    [Teardown]    Close Browser

Checkboxes Test
    [Documentation]    Verify that checkboxes can be checked and unchecked
    Start Browser
    Open Webpage    ${WEB_URL}
    Go to Checkboxes Page
    Verify Check Box 1 is unchecked
    Select Check Box 1
    Verify Check Box 1 is checked
    Verify Check Box 2 is checked
    UnSelect Check Box 2
    Verify Check Box 2 is unchecked
    [Teardown]    Close Browser

Dropdown Test
    [Documentation]    Verify each option in dropdown can be selected
    Start Browser
    Open Webpage    ${WEB_URL}
    Go to Dropdown Page
    Verify Dropdown Select From List
    [Teardown]    Close Browser


Upload File Test
    [Documentation]    Verify each option in dropdown can be selected
    Start Browser
    Open Webpage    ${WEB_URL}
    Go to File Upload Page
    Verify Upload File
    [Teardown]    Close Browser


*** Keywords ***
Start Browser
    Website.Start

Open Webpage
    [Arguments]    ${url}
    Website.Open Web Page    ${url}

Login To Website Successfully
    [Arguments]    ${url}    ${username}    ${password}
    Open Webpage    ${url}
    Website.Navigate To Login Form
    Website.Login    ${username}    ${password}

Login To Website Failed
    [Arguments]    ${url}    ${username}    ${password}
    Open Webpage    ${url}
    Website.Navigate To Login Form
    Website.Login    ${username}    ${password}    ${True}

Close Browser
     Website.Close

Go to Checkboxes Page
    Website.Navigate To Check Boxes

Verify Check box ${number} is ${expected_state}
    Website.Verify Checkbox State    ${number}    ${expected_state}

Select Check box ${number}
    Website.Interact With Checkbox    ${number}
    
UnSelect Check box ${number}
    Website.Interact With Checkbox    ${number}    uncheck

Go to Dropdown Page
    Website.Navigate To Dropdown

Verify Dropdown Select From List
    Website.verify Dropdown Selection

Go to File Upload Page
    Website.Navigate To File Upload

Verify Upload File
    Website.verify File Upload