    # for j in range(ns):
    #     imin = i - (ns-j)*s
    #     if imin < 0:
    #         continue
    #     imax = imin + s + 1
    #     # The fading looks better if we square the fractional length along the
    #     # trail.
    #     alpha = (j/ns)**2
    #     ax.plot(x2[imin:imax], y2[imin:imax], c='r', solid_capstyle='butt',
    #             lw=2, alpha=alpha)