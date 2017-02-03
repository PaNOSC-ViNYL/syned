"""
Implement an undulator with vertical and horizontal magnetic fields.
"""
import numpy as np
import scipy.constants.codata

from syned.storage_ring.magnetic_structures.insertion_device import InsertionDevice

class Undulator(InsertionDevice):

    def __init__(self,
                 K_vertical = 0.0,
                 K_horizontal = 0.0,
                 period_length = 0.0,
                 number_of_periods = 1):
        InsertionDevice.__init__(self, K_vertical, K_horizontal, period_length, number_of_periods)


    def resonance_wavelength(self, gamma, theta_x, theta_z):
        wavelength = (self.periodLength() / (2.0*gamma **2)) * \
                     (1 + self.K_vertical()**2 / 2.0 + self.K_horizontal()**2 / 2.0 + \
                      gamma**2 * (theta_x**2 + theta_z ** 2))

        return wavelength

    def resonanceFrequency(self, gamma, theta_x, theta_z):
        codata = scipy.constants.codata.physical_constants
        codata_c = codata["speed of light in vacuum"][0]

        frequency = codata_c / self.resonance_wavelength(gamma, theta_x, theta_z)

        return frequency

    def resonance_energy(self, gamma, theta_x, theta_y, harmonic=1):
        codata = scipy.constants.codata.physical_constants
        energy_in_ev = codata["Planck constant"][0] * self.resonanceFrequency(gamma, theta_x, theta_y) / codata["elementary charge"][0]

        return energy_in_ev*harmonic

    def gaussianCentralConeDivergence(self, gamma, n=1):
        return (1/gamma)*np.sqrt((1.0/(2.0*n*self.periodNumber())) * (1.0 + self.K_horizontal()**2/2.0 + self.K_vertical()**2/2.0))

    @classmethod
    def initialize_as_vertical_undulator(cls, K = 0.0, period_length = 0.0, periods_number = 1):
        return Undulator(K_vertical=K,
                         K_horizontal=0.0,
                         period_length=period_length,
                         number_of_periods=periods_number)

if __name__ == "__main__":

    a = Undulator()

    fd = a.to_full_dictionary()
    dict = a.to_dictionary()

    print(dict)

    for key in fd:
        print(key,fd[key][0])

    for key in fd:
        print(key,dict[key])

    print(a.keys())
    print(a.info())
