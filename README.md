# PoppyRattle

Poppy creature based on Poppy Humanoid's right arm, equipped with a toy interaction gripper at the wrist.

This robotic device is based on the Poppy 6-DOF right arm by Joel Ortiz and Poppy Right Gripper by Sebastien Mick. This is a collaborative work-in-progress between the Emergence of Communication Lab and MESA Lab at UC Merced. This version of the Poppy Humanoid basic right arm shakes rattles and plays with toys for insight to the emergence of developmental stages and attention shift in infants.

# Installation
Installation requires setuptools. Dependencies are the same as the other custom Poppy creatures: pypot and poppy-creature. Usual ways to set up the modules are:

Running python setup.py requires that the dependencies are already available on the Python version.
Running pip install . in the module's root directory will automatically fetch and install the dependencies.
Depending on the version of poppy-creature, this custom Poppy creature may have to be manually "registered" in the installed_poppy_creatures dictionary, in $PYTHON_MODULES/poppy/creatures/__init__.py.