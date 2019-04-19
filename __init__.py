# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# -----------------------------------------
# depends on:
#   lex_suite.lexgame
#   lex_suite.lex_statemachine

bl_info = {
    "name" : "Lex2D",
    "author" : "lexomir",
    "description" : "",
    "blender" : (2, 80, 0),
    "location" : "",
    "warning" : "uh oh spaghetti-o's",
    "category" : "Scene"
}

import bpy
import sys
from . import auto_load

auto_load.init()

def register():
    auto_load.register()


def unregister():
    auto_load.unregister()


_lex_suite = None
def get_lex_suite():
    global _lex_suite
    if _lex_suite:
        return _lex_suite
    else:
        _lex_suite = sys.modules.get('lex_suite')
        return _lex_suite

def __lex_suite_registered__(lex_suite_module):
    from .utils import _lex_suite_callbacks
    global _lex_suite
    _lex_suite = lex_suite_module
    for cb in _lex_suite_callbacks:
        cb(lex_suite_module)