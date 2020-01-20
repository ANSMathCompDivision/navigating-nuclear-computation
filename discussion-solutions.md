# Answers to discussion questions:

## Objective 1:

**What happens as you vary the initial concentration of atoms?**

The resulting activity increases or decreases proportionally. Looking at our
original equation for activity, the initial concentration is outside of the
exponential term, so the effect of initial concentration will be proportional
to the final activity if time and half-life remain constant.

**How does the activity compare if you have a very short half-life vs. a very long half-life?**

Given a specific time, t, half-life can make a very strong difference on the
final activity of two radionuclides with the same initial concentration.
If you have a very short half-life and the time is much longer than several
half-lives, the final activity may be very small.

**What happens if the length of time you wait is very different from the time of your half life?**

If the length of time elapsed to calculate activity differs strongly from your
half-life (such as by 10x or more), then you will either see a final activity
that is either very very small (less than 1%) compared to your initial activity (if t >>
t_(1/2)). Or if (t<<t_(1/2)) then the final activity will likely be very close
to your initial activity.

**What other functions could you write that would make this function easier to use?**

You could write a simple function to calculate the decay constant of a radionuclide given the half life as an input.

## Objective 2:

**How does changing the distance away from the source affect the total particle rate hitting the body?**

Moving away from the source will decrease the particle rate hitting the body by
a factor of r^2.

**Imagine if Michael Jordan and Simone Biles were both in the room with this source. Would the particle rate that each of them sees be different? How would it differ?**

We assumed in our exercise that the cross-sectional area of the human body
being exposed is the person's `height` times the person's `width` across their
shoulders. Michael Jordan is significantly larger in both directions (210 cm by
58cm),
whereas Simone Biles is substantively smaller (142 cm by 38cm). As a result, Simone Biles'
body will see a lower particle rate incident on her body than Michael Jordan if
they are the same distance from the source.

**What would happen if instead of facing the source, you turned sideways so your shoulder was pointing to it?**

If you turn 90 degrees from your initial position facing the source, your
exposure area would change from `height` times `shoulder width` to `height`
times `body depth`, which is probably the distance from your chest to your
spine (through your body). This dimension will be much smaller than the
shoulder width, so you would be lowering the number of particles incident on
your body by decreasing the exposure area.

**Do you think there are assumptions to this equation? What are they? Hint: what happens if you make the distance from the source very small?**

There are many good answers to this question, but we will provide a few:
* The equation is assuming the source can be approximated as a point. If not,
  the exposure area at a distance r may not be adequately represented as
  `4*pi*r^2`.
* If the distance is very small, the area of the person may become larger than
  the surface area of the sphere surrounding the source. This is because we
  assume the source is at a point. If a human is too close, their area
  cannot be projected onto a sphere with the assumptions of this equation.
* This equation assumes that there is no attenuation (or removal) of particles
  due to the material between the person and the source. In a
  room on earth, this material is likely air and this assumption is reasonable. However, as the
  distance becomes great, air attenuation may become another non-negligble
  factor. If, instead, the person were next to a source underwater, the
  material attenuation would be significant and we'd have to add an
  additional term to this equation.

**What other functions could you write that would make this function easier to use?**

Rather than calculating the person's cross-sectional area by hand, you could
write a function that calculates the person's area given their height and width.
You could even have the inputs be in inches or feet and then have the function convert to cm!

## Objective 3:

**If you were choosing a shielding material, what type of macroscopic cross section would you look for and why?**

If you wanted to shield people well, then choosing a material with a high
macroscopic cross section would be ideal. A higher macroscopic cross section
will require less shielding thickness to achieve the same reduction in source
intensity.

**Do you think there are assumptions to this equation?  What are they?**

This is a challenge question. There are assumptions here. The macroscopic cross
section is energy dependent, and often times our sources will change energy as
they traverse material in a shield. This equation assumes that that is not an
issue.
