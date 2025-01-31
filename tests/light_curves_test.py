import jax.numpy as jnp

from jaxoplanet import orbits
from jaxoplanet.light_curves import LimbDarkLightCurve


def test_light_curve():
    # Fiducial planet parameters:
    params = {
        "period": 300.456,
        "radius": 0.1,
        "u": jnp.array([0.3, 0.2]),
        "bo": 0.8,
    }
    # The light curve calculation requires an orbit
    orbit = orbits.keplerian.Body(
        period=params["period"], radius=params["radius"], impact_param=params["bo"]
    )

    # Compute a limb-darkened light curve using jaxoplanet
    t = jnp.linspace(-0.3, 0.3, 1000)

    LimbDarkLightCurve(params["u"]).light_curve(orbit, t=t)
