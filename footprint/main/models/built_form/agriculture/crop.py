# coding=utf-8

# UrbanFootprint v1.5
# Copyright (C) 2017 Calthorpe Analytics
#
# This file is part of UrbanFootprint version 1.5
#
# UrbanFootprint is distributed under the terms of the GNU General
# Public License version 3, as published by the Free Software Foundation. This
# code is distributed WITHOUT ANY WARRANTY, without implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License v3 for more details; see <http://www.gnu.org/licenses/>.


from footprint.main.managers.geo_inheritance_manager import GeoInheritanceManager
from footprint.main.mixins.agriculture_attribute_set_mixin import AgricultureAttributeSetMixin
from footprint.main.models.built_form.primary_component import PrimaryComponent

class Crop(PrimaryComponent, AgricultureAttributeSetMixin):
    """
    Crop represents a template crop, such as "Alfalfa" or "Carrot"
    """
    objects = GeoInheritanceManager()

    class Meta(object):
        # This is not abstract so that django can form a many-to-many relationship with it in built_form_set
        app_label = 'main'
