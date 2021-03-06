
import unittest
import os

from PySide.QtCore import QSettings
from QtMobility.ServiceFramework import QServiceManager

class InterfaceDefault(unittest.TestCase):

    def testNullInterfaceDefault(self):
        manager = QServiceManager()

        self.assertFalse(manager.interfaceDefault('').isValid())


class AddRemoveService(unittest.TestCase):

    def setUp(self):
        self.settings = QSettings('com.nokia.qt.serviceframework.tests',
                                  'SampleServicePlugin')
        self.manager = QServiceManager()

        self.serviceXml = os.path.join(os.path.dirname(__file__),
                                  'sampleservice.xml')

    def testAddRemoveService(self):
        self.assertTrue(self.manager.addService(self.serviceXml))
        self.assertTrue('SampleService' in self.manager.findServices())
        self.assertTrue(self.settings.value('installed'))

        self.assertEqual(self.manager.findServices('com.nokia.qt.TestInterfaceA'),
                         ['SampleService'])
        self.assertTrue(self.manager.removeService('SampleService'))
        self.assertTrue('SampleService' not in self.manager.findServices())

        self.assertEqual(self.manager.findServices('com.nokia.qt.TestInterfaceA'), [])
        self.assertFalse(self.settings.value('installed'))


class RemoveService(unittest.TestCase):

    def testRemoveNonExistent(self):
        manager = QServiceManager()

        self.assertFalse(manager.removeService('NonExistentService'))

if __name__ == '__main__':
    unittest.main()
