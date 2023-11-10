import unittest
import os
from pyrdp.player import Player
from pyrdp.mitm import MITMConfig, RDPMITM
from pyrdp.logging import LOGGER, SessionLogger
from pyrdp.layer import PlayerLayer
from pyrdp.mitm.actions import Action, ScreenshotAction

class TestRDPClient(unittest.TestCase):
    def setUp(self):
        self.server = "WIN11-VM"
        self.username = "Robin.F.Collins@outlook.com"
        self.password = "TestPassword"
        self.config = MITMConfig(self.server, self.username, self.password)
        self.mitm = RDPMITM(self.config, LOGGER, SessionLogger(LOGGER))
        self.player = Player(PlayerLayer())
        self.mitm.connect()

    def test_connection(self):
        self.assertTrue(self.mitm.state.isConnected)

class TestScreenshotCapture(unittest.TestCase):
    def setUp(self):
        self.server = "WIN11-VM"
        self.username = "Robin.F.Collins@outlook.com"
        self.password = "TestPassword"
        self.config = MITMConfig(self.server, self.username, self.password)
        self.mitm = RDPMITM(self.config, LOGGER, SessionLogger(LOGGER))
        self.player = Player(PlayerLayer())
        self.mitm.connect()
        self.screenshot_action = ScreenshotAction("screenshot.png")
        self.screenshot_action.perform(self.mitm)

    def test_screenshot_capture(self):
        self.assertTrue(os.path.exists("screenshot.png"))

if __name__ == '__main__':
    unittest.main()