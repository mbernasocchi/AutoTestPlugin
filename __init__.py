# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TestPlugin
                                 A QGIS plugin
 my awesome plugin
                             -------------------
        begin                : 2016-06-27
        copyright            : (C) 2016 by Marco Bernasocchi
        email                : marco@opengis.ch
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TestPlugin class from file TestPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .test_plugin import TestPlugin
    return TestPlugin(iface)
