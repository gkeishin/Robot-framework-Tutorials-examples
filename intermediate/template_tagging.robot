*** Settings ***
Documentation   Set Tags and remove tags in template.

*** Test cases ***

Sample Tags Templates

    #user   #mode 
    ABC     ABC
    XYZ     XYZ 
    123     123

    [Template]  Set Tags by Name


*** Keywords ***

Set Tags by Name
    [Arguments]  ${user}   ${mode}
    Set Tags   Test_${user}_${mode}
    Log To Console   \n\t Test Case: ${TEST_NAME} \t Test Tag: ${TEST TAGS}
    Remove Tags   Test_${user}_${mode}




*** Out put of the sample example ****
==============================================================================
Template Tagging :: Set Tags and remove tags in template.                     
==============================================================================
Sample Tags Templates                                                 
	 Test Case: Sample Tags Templates 	 Test Tag: [u'Test_ABC_ABC']
.
	 Test Case: Sample Tags Templates 	 Test Tag: [u'Test_XYZ_XYZ']
.
	 Test Case: Sample Tags Templates 	 Test Tag: [u'Test_123_123']
Sample Tags Templates                                                 | PASS |
------------------------------------------------------------------------------
Template Tagging :: Set Tags and remove tags in template.             | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
