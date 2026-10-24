import pygarment as pyg
from assets.bodies.body_params import BodyParameters
from assets.garment_programs.meta_garment import MetaGarment
from assets.garment_programs import bodice
import yaml

# Let's inspect what happens if we apply:
# self.edges[0].end[0] = -waist when bottom_dart is False
body = BodyParameters('assets/bodies/dominika.yaml')

# Check DOMINIKA waist
print("Waist Dominika:", body['waist'])
