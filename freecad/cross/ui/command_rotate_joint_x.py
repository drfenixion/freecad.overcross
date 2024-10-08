from __future__ import annotations

import FreeCAD as fc

import FreeCADGui as fcgui

from ..freecad_utils import message
from ..freecad_utils import validate_types
from ..freecad_utils import is_lcs
from ..gui_utils import tr
from ..wb_utils import rotate_origin


# Stubs and type hints.
from ..joint import Joint
from ..link import Link
DO = fc.DocumentObject
CrossLink = Link
CrossJoint = Joint
LCS = DO  # Local coordinate systen, TypeId == "PartDesign::CoordinateSystem"


class _RotateJointXCommand:
    """Command to rotate joint by X axis.
    """

    def GetResources(self):
        return {'Pixmap': 'rotate_joint_x.svg',
                'MenuText': tr('Rotate joint by X axis'),
                'Accel': 'R, X',
                'ToolTip': tr('Rotate joint by X axis.\n'
                              '\n'
                              'Select: joint or link or subobject (body, part, etc) of link\n'
                              )}

    def IsActive(self):
        return bool(fcgui.Selection.getSelection())

    def Activated(self):
        doc = fc.activeDocument()

        doc.openTransaction(tr("Rotate joint origin by X axis"))
        rotate_origin(x = 90, y = None, z = None)
        doc.commitTransaction()

        doc.recompute()


fcgui.addCommand('RotateJointX', _RotateJointXCommand())
