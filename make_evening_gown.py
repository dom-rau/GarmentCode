import yaml
from pathlib import Path
from assets.garment_programs.meta_garment import MetaGarment
from assets.bodies.body_params import BodyParameters
from pygarment.data_config import Properties
from datetime import datetime

# 1. Wczytujemy szablon domyślny
with open('assets/design_params/default.yaml', 'r') as f:
    config = yaml.safe_load(f)

d = config['design']

# 2. Architektura: Dopasowany gorset + dopasowana długa spódnica (suknia wieczorowa maxi)
d['meta']['upper']['v'] = 'FittedShirt'
d['meta']['wb']['v'] = None              # Płynne przejście bez paska (jednoczęściowy look)
d['meta']['bottom']['v'] = 'PencilSkirt'  # Długa dopasowana spódnica z rozcięciem

# 3. Prawa strona góry (z ramiączkiem / ramieniem)
d['shirt']['strapless']['v'] = False
d['shirt']['length']['v'] = 1.0           # Dokładnie do talii
d['shirt']['width']['v'] = 1.02           # Dopasowana do biustu
d['shirt']['flare']['v'] = 1.0

# Dekolt prawej strony
d['collar']['f_collar']['v'] = 'CircleNeckHalf'
d['collar']['b_collar']['v'] = 'CircleNeckHalf'
d['collar']['width']['v'] = 0.25
d['collar']['fc_depth']['v'] = 0.35
d['collar']['bc_depth']['v'] = 0.15

# Bez rękawów
d['sleeve']['sleeveless']['v'] = True
d['sleeve']['armhole_shape']['v'] = 'ArmholeCurve'

# 4. ASYMETRIA - JEDNO RAMIĘ SKOŚNE (Lewe ramię odkryte / strapless)
d['left']['enable_asym']['v'] = True
d['left']['shirt']['strapless']['v'] = True   # Odsłonięte lewe ramię!
d['left']['shirt']['width']['v'] = 1.02
d['left']['shirt']['flare']['v'] = 1.0

d['left']['collar']['f_collar']['v'] = 'CircleNeckHalf'
d['left']['collar']['b_collar']['v'] = 'CircleNeckHalf'
d['left']['collar']['width']['v'] = 0.25

d['left']['sleeve']['sleeveless']['v'] = True
d['left']['sleeve']['armhole_shape']['v'] = 'ArmholeCurve'

# 5. DŁUGA SPÓDNICA MAXI Z ROZCIĘCIEM NA JEDNEJ NODZE
d['pencil-skirt']['length']['v'] = 0.90       # Długość maxi do kostek/ziemi
d['pencil-skirt']['rise']['v'] = 1.0          # Od linii talii
d['pencil-skirt']['flare']['v'] = 1.05        # Smukła, elegancka linia
d['pencil-skirt']['low_angle']['v'] = 0

# Rozcięcie na lewej nodze (zmysłowe wysokie pęknięcie na 70% długości spódnicy)
d['pencil-skirt']['left_slit']['v'] = 0.70    # Wysokie rozcięcie na lewej nodze
d['pencil-skirt']['right_slit']['v'] = 0.0
d['pencil-skirt']['front_slit']['v'] = 0.0
d['pencil-skirt']['back_slit']['v'] = 0.0
d['pencil-skirt']['style_side_cut']['v'] = None

# Zapisujemy do assets/design_params/evening_gown.yaml
target_yaml = Path('assets/design_params/evening_gown.yaml')
with open(target_yaml, 'w') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False)
print(f"Zapisano: {target_yaml}")

# Testujemy montaż z wymiarami dominika.yaml
body = BodyParameters('./assets/bodies/dominika.yaml')
gown = MetaGarment('evening_gown', body, d)
pattern = gown.assembly()
print("Montaz sukni wieczorowej udany!")
if gown.is_self_intersecting():
    print("Ostrzezenie: self-intersecting")

# Zapisujemy wykrój
sys_props = Properties('./system.json')
folder = pattern.serialize(
    Path(sys_props['output']),
    tag='_' + datetime.now().strftime("%y%m%d-%H-%M-%S"),
    to_subfolder=True,
    with_printable=True
)

import shutil
shutil.copy(target_yaml, folder)
shutil.copy('./assets/bodies/dominika.yaml', folder)

print(f"Wykroj zapisany w: {folder}")
