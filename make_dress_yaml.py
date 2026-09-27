import yaml
from pathlib import Path

# Load base default configuration
with open('assets/design_params/default.yaml', 'r') as f:
    config = yaml.safe_load(f)

d = config['design']

# 1. Meta elements: Fitted top + Waistband + Full circle skirt
d['meta']['upper']['v'] = 'FittedShirt'
d['meta']['wb']['v'] = 'FittedWB'
d['meta']['bottom']['v'] = 'SkirtCircle'

# 2. Top (fitted bodice)
d['shirt']['strapless']['v'] = False
d['shirt']['length']['v'] = 1.0   # Reaches waist
d['shirt']['width']['v'] = 1.05
d['shirt']['flare']['v'] = 1.0

# 3. Neckline (50s classic wide scoop / boat neckline)
d['collar']['f_collar']['v'] = 'CircleNeckHalf'
d['collar']['b_collar']['v'] = 'CircleNeckHalf'
d['collar']['width']['v'] = 0.35
d['collar']['fc_depth']['v'] = 0.35
d['collar']['bc_depth']['v'] = 0.1

# 4. Waistband (narrow, cinched waist)
d['waistband']['waist']['v'] = 1.0
d['waistband']['width']['v'] = 0.15

# 5. Skirt (full circle 360°, elegant midi length)
d['flare-skirt']['suns']['v'] = 1.0      # 1.0 = Full circle (360 degrees)
d['flare-skirt']['length']['v'] = 0.65   # Below knee (midi)
d['flare-skirt']['rise']['v'] = 1.0

# 6. Sleeves (sleeveless)
d['sleeve']['sleeveless']['v'] = True
d['sleeve']['armhole_shape']['v'] = 'ArmholeCurve'

target = Path('assets/design_params/dress_50s.yaml')
with open(target, 'w') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False)

print(f"Successfully generated {target}")
