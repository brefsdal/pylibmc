"""Memcached serialize tests"""

import pylibmc
from nose.tools import eq_
from tests import PylibmcTestCase

class TestSerialize(PylibmcTestCase):
    def testSerialize(self):
        self.mc.set("num12345", {"num": 12345})
        eq_(self.mc.get("num12345"), {u"num": 12345})
        self.mc.set("arr12345", [1,2,3,4,5])
        eq_(self.mc.get("arr12345"), [1,2,3,4,5])
