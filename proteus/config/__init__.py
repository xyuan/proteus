import os

if 'PROTEUS_ARCH' in os.environ and os.environ['PROTEUS_ARCH'].startswith('garnet'):
    from garnet import *
elif 'PROTEUS_ARCH' in os.environ and os.environ['PROTEUS_ARCH'].startswith('spirit'):
    from spirit import *
elif 'PROTEUS_ARCH' in os.environ and os.environ['PROTEUS_ARCH'].startswith('copper'):
    from copper import *
elif 'PROTEUS_ARCH' in os.environ and os.environ['PROTEUS_ARCH'].startswith('lightning'):
    from lightning import *
elif 'PROTEUS_ARCH' in os.environ and os.environ['PROTEUS_ARCH'].startswith('viutill'):
    from viutill import *
else:
    from default import *
