import yaml
from pathlib import Path
from assets.garment_programs.meta_garment import MetaGarment
from assets.bodies.body_params import BodyParameters
from pygarment.data_config import Properties
from datetime import datetime

# 1. Load default template
with open('assets/design_params/default.yaml', 'r') as f:
    config = yaml.safe_load(f)

d = config['design']

# 2. Meta: Dopasowana/lekko zbluzowana góra + prosty pasek na gumkę + spódnica z koła
d['meta']['upper']['v'] = 'FittedShirt'
d['meta']['wb']['v'] = 'StraightWB'      # Prosty pas z tunelem na gumkę
d['meta']['bottom']['v'] = 'SkirtCircle'  # Spódnica z koła

# 3. Góra
d['shirt']['strapless']['v'] = False
d['shirt']['length']['v'] = 1.05          # Lekki naddatek do talii (efekt zbluzowania)
d['shirt']['width']['v'] = 1.05
d['shirt']['flare']['v'] = 1.05

# 4. Dekolt
d['collar']['f_collar']['v'] = 'CircleNeckHalf'
d['collar']['b_collar']['v'] = 'CircleNeckHalf'
d['collar']['width']['v'] = 0.35          # Elegancka łódka
d['collar']['fc_depth']['v'] = 0.35
d['collar']['bc_depth']['v'] = 0.1

# 5. Pasek z gumką w talii (StraightWB)
d['waistband']['waist']['v'] = 1.0        # Dopasowany do obwodu talii
d['waistband']['width']['v'] = 0.1        # Wąski pasek/tunel na gumkę (~3.5 cm)

# 6. Spódnica z pełnego koła
d['flare-skirt']['suns']['v'] = 1.0       # 360 stopni pełne koło
d['flare-skirt']['length']['v'] = 0.65    # Długość midi
d['flare-skirt']['rise']['v'] = 1.0

# 7. RĘKAWY SZEROKIE Z GUMKĄ NA KOŃCU (Bishop / Puffy Elastic Sleeve)
d['sleeve']['sleeveless']['v'] = False    # Z rękawami!
d['sleeve']['armhole_shape']['v'] = 'ArmholeCurve'
d['sleeve']['length']['v'] = 0.85         # Długi rękaw do nadgarstka (lub 0.7 na 3/4)
d['sleeve']['connecting_width']['v'] = 0.2
d['sleeve']['end_width']['v'] = 1.6       # Bardzo szeroki dół rękawa (balonowy)
d['sleeve']['sleeve_angle']['v'] = 15

# Mankiet z gumką (CuffBand ze ściągaczem)
d['sleeve']['cuff']['type']['v'] = 'CuffBand'
d['sleeve']['cuff']['top_ruffle']['v'] = 1.8     # Mocne umarszczenie materiału do gumki
d['sleeve']['cuff']['cuff_len']['v'] = 0.06      # Wąski mankiet/gumka (~2.5 cm)

# Zapisujemy do assets/design_params/dress_50s_elastic.yaml
target_yaml = Path('assets/design_params/dress_50s_elastic.yaml')
with open(target_yaml, 'w') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False)
print(f"Zapisano {target_yaml}")

# Testujemy montaż z wymiarami dominika.yaml
body = BodyParameters('./assets/bodies/dominika.yaml')
dress = MetaGarment('dress_50s_elastic', body, d)
pattern = dress.assembly()
print("Montaz sukienki udany!")
if dress.is_self_intersecting():
    print("Ostrzezenie: self-intersecting")

# Zapisujemy wykrój
sys_props = Properties('./system.json')
folder = pattern.serialize(
    Path(sys_props['output']),
    tag='_' + datetime.now().strftime("%y%m%d-%H-%M-%S"),
    to_subfolder=True,
    with_printable=True
)
print(f"Wykroj zapisany w: {folder}")
