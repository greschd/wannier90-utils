"""Predefined trial orbitals"""

atomic_orbitals = {}
atomic_orbitals[0] = {}
atomic_orbitals[0][1] = 's'
atomic_orbitals[1] = {}
atomic_orbitals[1][1] = 'pz'
atomic_orbitals[1][2] = 'px'
atomic_orbitals[1][3] = 'py'
atomic_orbitals[2] = {}
atomic_orbitals[2][1] = 'dz2'
atomic_orbitals[2][2] = 'dxz'
atomic_orbitals[2][3] = 'dyz'
atomic_orbitals[2][4] = 'dx2-y2'
atomic_orbitals[2][5] = 'dxy'
atomic_orbitals[3] = {}
atomic_orbitals[3][1] = 'fz3'
atomic_orbitals[3][2] = 'fxz2'
atomic_orbitals[3][3] = 'fyz2'
atomic_orbitals[3][4] = 'fz(x2-y2)'
atomic_orbitals[3][5] = 'fxyz'
atomic_orbitals[3][6] = 'fx(x2-3y2)'
atomic_orbitals[3][7] = 'fy(3x2-y2)'

hybrid_orbitals = {}
hybrid_orbitals[-1] = {}
hybrid_orbitals[-1][1] = 'sp-1'
hybrid_orbitals[-1][2] = 'sp-2'
hybrid_orbitals[-2] = {}
hybrid_orbitals[-2][1] = 'sp2-1'
hybrid_orbitals[-2][2] = 'sp2-2'
hybrid_orbitals[-2][3] = 'sp2-3'
hybrid_orbitals[-3] = {}
hybrid_orbitals[-3][1] = 'sp3-1'
hybrid_orbitals[-3][2] = 'sp3-2'
hybrid_orbitals[-3][3] = 'sp3-3'
hybrid_orbitals[-3][4] = 'sp3-4'
hybrid_orbitals[-4] = {}
hybrid_orbitals[-4][1] = 'sp3d-1'
hybrid_orbitals[-4][2] = 'sp3d-2'
hybrid_orbitals[-4][3] = 'sp3d-3'
hybrid_orbitals[-4][4] = 'sp3d-4'
hybrid_orbitals[-4][5] = 'sp3d-5'
hybrid_orbitals[-5] = {}
hybrid_orbitals[-5][1] = 'sp3d2-1'
hybrid_orbitals[-5][2] = 'sp3d2-2'
hybrid_orbitals[-5][3] = 'sp3d2-3'
hybrid_orbitals[-5][4] = 'sp3d2-4'
hybrid_orbitals[-5][5] = 'sp3d2-5'
hybrid_orbitals[-5][6] = 'sp3d2-6'

orbitals = {**atomic_orbitals, **hybrid_orbitals}
