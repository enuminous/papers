# HORIZON Brings Cosmic Horizons Into the Browser

*An interactive observatory connects a frozen cosmology model with the paths of light across an expanding universe*

**Science and technology · October 24, 2026**

[Open HORIZON](https://enuminous.github.io/Cosmology/) · [Download the Word article](HORIZON-Cosmology-Journalistic-Article.docx)

Matthew Chenoweth Wright has put a working cosmological model inside a single downloadable web page. In HORIZON, the public interface to his new Cosmology repository, visitors can move through cosmic time, switch backgrounds and send a simulated light signal toward an observer. The result makes an abstract question tangible: in an expanding universe, which signals can actually reach us? [^1]

![HORIZON interface in Recursion view with nested illustrative spheres, cosmic time controls and calculated C1Q readouts](assets/horizon-cosmology/horizon-preview-2026-10-24.jpg)

*HORIZON in its Recursion view. The nested geometry is illustrative artwork; the side panels show calculated quantities for the selected background. Project screenshot.*[^1]

Published at enuminous.github.io/Cosmology, the application brings a desktop-style interface to Wright’s EFMW research program. Its dark display holds luminous spheres, a cosmic timeline and numerical readouts. Visitors can orbit the scene, inspect a spacetime diagram or enter a recursion view of geometrically nested worlds. The downloaded HTML file contains the interface, calculation engine and reference data, so it can run without an account, installation or internet connection. [^1]

The light-signal experiment addresses a common source of confusion. The Hubble sphere marks the distance at which recession caused by cosmic expansion equals the speed of light. It is not generally an impassable boundary. Under a suitable expansion history, an inward-moving photon can initially become more distant from an observer and nevertheless arrive later. That behavior is a consequence of general relativity, discussed in detail by cosmologists Tamara Davis and Charles Lineweaver. A numerical test supplied with HORIZON reproduces such a trajectory against an analytic solution. [^2]

HORIZON distinguishes that sphere from the distance light can traverse over the supplied history and from an event horizon, which depends on the universe’s future expansion. This distinction affects what the software is willing to display. The frozen EFMW calculation ends at the present epoch; its future event horizon is therefore left unspecified. A separate comparison model includes an assumed future and can calculate one. [^1]

Behind the interface sits EFMW-COSMO-C1Q version 1.0.0, a cosmological specification frozen on October 16 and published in the repository on October 23. Here, “frozen” means the equations, parameter choices, initial conditions and numerical conventions have been recorded. Changing the physics requires a new version. This gives later comparisons a stable reference: a prediction cannot quietly become a different prediction after the data are examined. [^3]

The model combines spatially flat general relativity with ordinary matter, photons, cold dark matter, neutrinos and one canonical scalar field. A scalar field assigns a value to each point in spacetime. Its energy can influence cosmic expansion. C1Q uses a quadratic potential, V(φ) = ½m²φ², and sets the cosmological constant to zero. The scalar supplies the component responsible for accelerated expansion in the reference calculation. [^3]

This is an example of quadratic quintessence, an established class of dark-energy models. A slowly evolving field can behave approximately like a cosmological constant before its motion becomes more significant. The release identifies that existing physics explicitly. Its contribution is a particular executable model and its documented calculations; an additional EFMW-specific physical effect has not been established. [^3][^4]

The browser carries 1,001 samples from the frozen expansion history, spanning a scale factor of one hundred-millionth of today’s value through the present. It interpolates those samples to calculate elapsed time and light travel. The resulting age is about 13.595 billion years since the model’s initial surface. The browser approximation differs from the original higher-accuracy solver by roughly 0.0016 percent. Those digits describe numerical agreement within a chosen model, rather than a new measurement of the universe’s age. [^1][^5]

The broader research package also goes beyond the browser’s horizon calculations. It uses an adapted, pinned version of CLASS, an established cosmological calculation code, to produce predictions for cosmic microwave background spectra and the linear growth of matter structure. These calculations include the scalar’s perturbations, allowing its effects to enter the predicted fluctuations as well as the average expansion. The browser does not rerun that full calculation. [^5][^6]

At the fixed reference point, the scalar’s present equation-of-state parameter, which relates pressure to energy density, is about −0.857. A cosmological constant would have a value of −1. At one specified scale, k = 0.1 h/Mpc, the calculated present-day linear matter power is about 3.86 percent lower than in the package’s matched Lambda cold dark matter comparison. That is a concrete difference for future testing, conditional on holding the other inputs fixed. It is not an observed suppression or evidence that C1Q fits the sky better. [^5]

Several inputs already constrain the outcome. The present expansion rate and ordinary density parameters are chosen. The scalar’s starting amplitude is then solved so that the specified flat-universe density budget closes. Its resulting share of the present energy density cannot therefore count as an independent discovery of the observed dark-energy fraction. The documentation makes this calibration step visible. [^3][^7]

The imagery has equally explicit boundaries. The recursion view can nest between two and ten scenes, but it does not evolve daughter universes. Its glowing tracers and filaments are generated visual elements, not predictions of real galaxies. Another mode displays a prescribed bounce, a geometry that contracts and then expands. That geometry is separate from C1Q; sustaining it in flat general relativity would require stress-energy properties absent from the frozen canonical model. These distinctions let visitors explore ideas without treating every animation as a physical result. [^1]

The release also preserves a record of calculations that failed scrutiny. An early perturbation implementation was rejected after a comparison between coordinate descriptions exposed a discrepancy; the audit identifies missing source terms in the relevant scalar equation. The earlier outputs remain in the repository, while the reference uses the stated synchronous-gauge implementation. An ill-conditioned early-time diagnostic is likewise retained and excluded from usable predictions. Further independent perturbation checks remain open. [^7]

Fresh checks for this article passed all 12 application tests and all nine background checks. The latter were rerun in a temporary copy, preserving the published files, alongside reanalysis of the saved CLASS tables. The full CLASS calculation was not rebuilt for this article. GitHub’s published application and package workflows also report success for the inspected revision. These checks support reproducibility and numerical behavior; they do not establish that the model describes nature. [^8]

That next stage is set out in a prospective testing protocol. It proposes comparison with DESI baryon acoustic oscillation measurements and Pantheon+ supernova data, followed by complementary checks using the Planck cosmic microwave background likelihood and additional distance or growth observations. Both C1Q and its conventional comparison would need consistent treatment of uncertainties, nuisance parameters and the freedom to fit data. The release contains no observational likelihood result, fitted posterior or completed statistical preference between the models. [^9]

HORIZON already offers a public way to examine how those assumptions affect an expanding universe. A reader can follow a light path, save the session and then inspect the equations behind the display. Whether the frozen model survives comparison with the sky is still an open question. The repository now provides a specific calculation for that comparison to test.

## Sources and reporting notes

Reporting is based on the public release inspected on October 24, 2026, at revision [`f457a1fc414257d5e4d2ddbeb8985db2cb714363`](https://github.com/enuminous/Cosmology/tree/f457a1fc414257d5e4d2ddbeb8985db2cb714363). The live page matched the repository HTML byte for byte. The application tests and background reproduction were rerun; saved CLASS tables were reanalyzed. No new full CLASS evolution or observational fit was performed. No interviews are represented in this article.

[Reporting verification record](assets/horizon-cosmology/article-verification-2026-10-24.json).

[^1]: **HORIZON application and methods.** [Live application](https://enuminous.github.io/Cosmology/) · [Controls, numerical method and evidence boundaries](https://github.com/enuminous/Cosmology/blob/f457a1fc414257d5e4d2ddbeb8985db2cb714363/webapp/README.md) · [Calculation engine](https://github.com/enuminous/Cosmology/blob/f457a1fc414257d5e4d2ddbeb8985db2cb714363/webapp/physics.js)

[^2]: **Cosmic horizons and photon behavior.** [Davis and Lineweaver, Expanding Confusion, PASA 21 (2004), 97–109](https://doi.org/10.1071/AS03040) · [HORIZON analytic and regression tests](https://github.com/enuminous/Cosmology/blob/f457a1fc414257d5e4d2ddbeb8985db2cb714363/webapp/test.cjs)

[^3]: **Frozen cosmological specification and publication record.** [Model and assumptions](https://github.com/enuminous/Cosmology/blob/f457a1fc414257d5e4d2ddbeb8985db2cb714363/docs/MODEL.md) · [Publication note](https://github.com/enuminous/Cosmology/blob/f457a1fc414257d5e4d2ddbeb8985db2cb714363/PUBLICATION.md)

[^4]: **Established quintessence context.** [Chiba, Slow-Roll Thawing Quintessence, Physical Review D 79 (2009), with erratum](https://arxiv.org/abs/0902.4037)

[^5]: **Calculated outputs and their numerical limits.** [Numerical results](https://github.com/enuminous/Cosmology/blob/f457a1fc414257d5e4d2ddbeb8985db2cb714363/docs/NUMERICAL_RESULTS.md) · [Perturbation prescription](https://github.com/enuminous/Cosmology/blob/f457a1fc414257d5e4d2ddbeb8985db2cb714363/docs/PERTURBATIONS.md)

[^6]: **The CLASS numerical framework.** [Blas, Lesgourgues and Tram, CLASS II, JCAP 07 (2011) 034](https://arxiv.org/abs/1104.2933)

[^7]: **Calibration, rejected implementations and unresolved obligations.** [Evidence audit](https://github.com/enuminous/Cosmology/blob/f457a1fc414257d5e4d2ddbeb8985db2cb714363/docs/AUDIT.md)

[^8]: **Verification of the inspected revision.** [Application workflow](https://github.com/enuminous/Cosmology/actions/runs/40046509539) · [Frozen-package workflow](https://github.com/enuminous/Cosmology/actions/runs/40046509321) · [Reproduction script used for the article checks](https://github.com/enuminous/Cosmology/blob/f457a1fc414257d5e4d2ddbeb8985db2cb714363/tools/verify_publication.py)

[^9]: **Proposed empirical comparison and acceptance rules.** [Prospective test protocol](https://github.com/enuminous/Cosmology/blob/f457a1fc414257d5e4d2ddbeb8985db2cb714363/docs/TEST_PROTOCOL.md)
