import yaml
from pathlib import Path
from assets.bodies.body_params import BodyParameters
from assets.garment_programs.meta_garment import MetaGarment
from pygarment.data_config import Properties
from datetime import datetime

body = BodyParameters('assets/bodies/dominika.yaml')

# Test with bottom_dart: False, side_dart: True
with open('assets/design_params/dress_50s_elastic.yaml', 'r') as f:
    config = yaml.safe_load(f)

d = config['design']
d['shirt']['bottom_dart'] = {'v': False, 'type': 'bool'}
d['shirt']['side_dart'] = {'v': True, 'type': 'bool'}

target_yaml = Path('assets/design_params/dress_50s_no_bottom_dart.yaml')
with open(target_yaml, 'w') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False)

print(f"Zapisano {target_yaml}")

dress = MetaGarment('dress_50s_no_bottom_dart', body, d)
pattern = dress.assembly()
print("Montaz sukienki bez dolnych zaszewek udany!")

sys_props = Properties('./system.json')
folder = pattern.serialize(
    Path(sys_props['output']),
    tag='_' + datetime.now().strftime("%y%m%d-%H-%M-%S"),
    to_subfolder=True,
    with_printable=True
)
print(f"Wykroj zapisany w: {folder}")

import shutil
shutil.copy(target_yaml, Path(folder) / 'dress_50s_no_bottom_dart.yaml')
shutil.copy('assets/bodies/dominika.yaml', Path(folder) / 'dominika.yaml')

