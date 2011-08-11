MiniMockTest
============

Documentation
-------------

This module provides a class which extends unittest.TestCase which can
be used to easily mock objects in a test case. This module can be used
in conjunction with other test case classes by means of multiple
inheritance http://docs.python.org/tutorial/classes.html#multiple-inheritance

An example of using Django's test case with this module's test case is
simply as follows::

    from minimocktest import MockTestCase
    from django.test import TestCase
    from django.test.client import Client

    class DjangoTestCase(TestCase, MockTestCase):
        '''
        A TestCase class that combines minimocktest and django.test.TestCase
        '''

        def setUp(self):
            TestCase.setUp(self)
            MockTestCase.setUp(self)
            # optional: shortcut client handle for quick testing
            self.client = Client()

        def tearDown(self):
            MockTestCase.tearDown(self)
            TestCase.tearDown(self)

COPYING
-------

This module is provided under the terms of the MIT Licence. The code in
this module relies on the "minimock" library which is included as part of
the package. The copyright notice for "minimock" is included at the
beginning of its source code file.

For more information, see the file LICENCSE or
http://www.opensource.org/licenses/mit-license.php
