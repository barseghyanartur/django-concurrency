from concurrency.tests.all import *  # NOQA
from concurrency.tests.forms import WidgetTest, FormFieldTest, ConcurrentFormTest  # NOQA
from concurrency.tests.middleware import ConcurrencyMiddlewareTest  # NOQA
from concurrency.tests.conf import SettingsTest  # NOQA
from concurrency.tests.api import ConcurrencyTestApi  # NOQA

from concurrency.tests.admin_edit import TestAdminEdit  # NOQA
from concurrency.tests.admin_list_editable import TestListEditable, TestListEditableWithNoActions  # NOQA
from concurrency.tests.admin_actions import TestAdminActions  # NOQA

try:
    from concurrency.tests.south_test import *  # NOQA
except ImportError:
    pass
