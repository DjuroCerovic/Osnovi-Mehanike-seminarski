from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(r[:imax, 0], r[:imax, 1], r[:imax, 2])
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("z (m)")
ax.set_title("3D putanja projektila kroz tornado")
show()

