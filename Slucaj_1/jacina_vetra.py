import numpy as np
import matplotlib.pyplot as plt

# Parametri tornada
pt = 50        # "poluprečnik" tornada (m)
umax = 100     # maksimalna brzina vetra (m/s)

# Udaljenosti od centra tornada (od 0 do 150 metara)
rr = np.linspace(0.1, 150, 500)  # kreće od 0.1 da se izbegne deljenje nulom

# Izračunavanje brzine vetra za svaku udaljenost
U = np.where(rr > pt, umax * (pt / rr), umax * (rr / pt))

# Crtanje grafa
plt.plot(rr, U)
plt.axvline(pt, color='red', linestyle='--', label='granica tornada (pt)')
plt.xlabel('Udaljenost od centra tornada (m)')
plt.ylabel('Brzina vetra (m/s)')
plt.title('Model brzine vetra oko tornada')
plt.grid(True)
plt.legend()
plt.show()

