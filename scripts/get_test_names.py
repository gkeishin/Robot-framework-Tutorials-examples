# Refer https://robot-framework.readthedocs.io/en/3.0.1/autodoc/robot.parsing.html
from robot.parsing.model import TestData

# hard coded 1 rbot test suite source, you can input the files in loop
# Example test suite from https://github.com/openbmc/openbmc-test-automation/blob/master/tests/test_basic_poweron.robot
suite = TestData(parent=None, source="/home/rango/openbmc-test-automation/tests/test_basic_poweron.robot")

# suite object has the property and grab the  "testcase_table" --> "name

for testcase in suite.testcase_table:
    print "Test Case name:", testcase.name
    # U can do stuff what u need

--------------- END of CODE ------------------------

O/P: When you execute the script it would look like this.
    
rango@ubuntu:~/Robot-framework-Tutorials-examples$ python scripts/get_test_names.py 
Test Case name: Verify Front And Rear LED At Standby
Test Case name: Power On Test
Test Case name: Check For Application Failures
Test Case name: Verify Uptime Average Against Threshold
Test Case name: Test SSH And IPMI Connections
rango@ubuntu:~/Robot-framework-Tutorials-examples$
    
