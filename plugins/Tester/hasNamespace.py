import medic
from maya import OpenMaya
import re


class HasNamespace(medic.PyTester):
    ReNS = re.compile("[:]")
    def __init__(self):
        super(HasNamespace, self).__init__()

    def Name(self):
        return "HasNamespace"

    def Description(self):
        return "Node(s) has a namespace"

    def Match(self, node):
        return True

    def test(self, node):
        if node.dg().isFromReferencedFile():
            return None

        if HasNamespace.ReNS.search(node.name()):
            return medic.PyReport(node)

        return None


def Create():
    return HasNamespace()
