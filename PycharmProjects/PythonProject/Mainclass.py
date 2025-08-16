# Open Website
import time

import pytest

from Navigation import Navigation
from Admin import Admin
from test import driver

nav=Navigation()
driver=nav.open_website()


ad=Admin(driver)
time.sleep(20)
ad.add_Admin()

time.sleep(20)



