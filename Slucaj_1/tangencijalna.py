from pylab import *
from numpy.linalg import norm

# Parametri projektila i vazduha
m = 0.25                      		# masa (kg)
pr = 0.030                		# prečnik (m)
gv = 1.293                 		# gustina vazduha (kg/m^3)
D = 3.0 * gv * pr**2     		# koeficijent otpora
Dm = D / m                   		# D podeljeno sa masom
g = array([0.0, 0.0, 9.8])   		# ubrzanje gravitacije

# Parametri tornada
umax = 50.0                  		# maksimalna brzina vetra (m/s)
pt = 5.0                  		# poluprečnik tornada (m)

# Početni uslovi
r0 = array([-100.0, 0.0, 0.0])             		# početna pozicija
alpha = 45.0 * pi / 180.0                  		# ugao u radijanima
v0 = 100.0 * array([cos(alpha), 0, sin(alpha)])  	# početna brzina

# Vreme simulacije
vreme = 10.0
vk = 0.001
n = int(round(vreme / vk))

# Alokacija nizova
r = zeros((n, 3), float)
v = zeros((n, 3), float)
a = zeros((n, 3), float)
t = zeros(n, float)
Ftang = zeros(n, float)  # niz za tangencijalnu silu

# Inicijalizacija
r[0] = r0
v[0] = v0
i = 0

# Glavna petlja simulacije
while (i + 1 < n) and (r[i, 2] >= 0.0):
    rr = norm(r[i])  # udaljenost od centra tornada

    if rr < pt:
        U = umax * (rr / pt)
    else:
        U = umax * (pt / rr)

    u = U * array([-r[i,1]/rr, r[i,0]/rr, 0.0])  # tangencijalna brzina vetra

    vrel = v[i] - u
    aa = -g - Dm * norm(vrel) * vrel

    # Izračun tangencijalne sile
    F = -m * aa - m * g
    if norm(u) > 1e-8:
        u_hat = u / norm(u)
        Ftang[i] = abs(dot(F, u_hat))
    else:
        Ftang[i] = 0.0

    a[i] = aa
    v[i + 1] = v[i] + vk * aa
    r[i + 1] = r[i] + vk * v[i + 1]
    t[i + 1] = t[i] + vk
    
    if i % 1000 == 0:
        print(f"i = {i},Tangencijalna sila = {Ftang[i]:.4f} N")
    i += 1

imax = i

# Ispis rezultata
vreme_u_tornadu = round(t[imax-1], 4)
print(f"Vreme provedeno u tornadu: {vreme_u_tornadu} s")

# Graf tangencijalne sile u zavisnosti od vremena
figure()
plot(t[:imax], Ftang[:imax], label="Tangencijalna sila")
xlabel("t (s)")
ylabel("F_tang (N)")
title("Tangencijalna sila na projektil u zavisnosti od vremena")
grid(True)
legend()

show()

