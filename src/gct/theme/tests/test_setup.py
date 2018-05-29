# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from gct.theme.testing import GCT_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that gct.theme is properly installed."""

    layer = GCT_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if gct.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'gct.theme'))

    def test_browserlayer(self):
        """Test that IGctThemeLayer is registered."""
        from gct.theme.interfaces import (
            IGctThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IGctThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = GCT_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(username=TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['gct.theme'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if gct.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'gct.theme'))

    def test_browserlayer_removed(self):
        """Test that IGctThemeLayer is removed."""
        from gct.theme.interfaces import \
            IGctThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IGctThemeLayer,
            utils.registered_layers(),
        )
