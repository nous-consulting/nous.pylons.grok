from nous.pylons.grok import the_multi_grokker

from zope.component.testing import setUp as zcSetUp, tearDown as zcTearDown
from zope.component.eventtesting import PlacelessSetup as EventPlacelessSetup


class GrokLayer(object):

    @classmethod
    def setUp(cls):
        # Zope component setup
        zcSetUp()
        EventPlacelessSetup().setUp()

    @classmethod
    def tearDown(cls):
        zcTearDown()

    @classmethod
    def testTearDown(cls):
        the_multi_grokker.clear()
