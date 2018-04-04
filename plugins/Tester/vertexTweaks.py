import medic
from maya import OpenMaya
from maya import cmds

class VertexTweaks(medic.PyTester):
    def __init__(self):
        super(VertexTweaks, self).__init__()

    def Name(self):
        return "VertexTweaks"

    def Description(self):
        return "Verticies are tweaked. Not Frozen."

    def Match(self, node):
        return node.object().hasFn(OpenMaya.MFn.kMesh)

    def test(self, node, geom = None):
        plug = node.dg().findPlug("pnts", True)
        tweaked = False
        for i in range(plug.numElements()):
            elm = plug.elementByPhysicalIndex(i)
            for j in range(3):
                if abs(elm.child(j).asDouble()) > 0.000001:
                    return medic.PyReport(node)

        return None

    def IsFixable(self):
        return True

    def fix(self, report, params):
        obj_name = report.node().name()
        cmds.polyMoveVertex(obj_name, ch=0)

        return True

def Create():
    return VertexTweaks()
