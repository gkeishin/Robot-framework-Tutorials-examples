# Refer https://robot-framework.readthedocs.io/en/3.0.1/autodoc/robot.parsing.html
from robot.parsing.model import TestData

# hard coded 1 rbot test suite source, you can input the files in loop
# Example test suite from https://github.com/openbmc/openbmc-test-automation/blob/master/tests/test_basic_poweron.robot
suite = TestData(parent=None, source="/home/rango/openbmc-test-automation/tests/test_basic_poweron.robot")

# suite object has the property and grab the  "testcase_table" --> "name

for testcase in suite.testcase_table:
    print "Test Case name:", testcase.name
    # U can do stuff what u need
