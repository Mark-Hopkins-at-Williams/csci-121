def pressure(moles, temperature, volume):
    boltzmann = 1.380649 * 10**(-23)
    avogadro = 6.02214076 * 10**23
    return (moles * boltzmann * avogadro * temperature) / volume