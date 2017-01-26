"""
Base class for all radiation sources: bending magnet or insertion devices (wiggler, undulator)
Every source can attach settings, i.e. inherits from DriverSettingsManager.
"""

from syned.storage_ring.magnetic_structure import MagneticStructure
from syned.storage_ring.electron_beam import ElectronBeam

class LightSource(object):
    def __init__(self, name="Undefined", electron_beam=ElectronBeam(), magnetic_structure=MagneticStructure()):
        self._name = name
        self._electron_beam = electron_beam
        self._magnetic_structure = magnetic_structure

    def get_name(self):
        return self._name

    def get_electron_beam(self):
        return self._electron_beam

    def get_magnetic_structure(self):
        return self._magnetic_structure