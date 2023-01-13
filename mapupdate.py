from staticmap import *


coords = {'0':((-0.157584, 51.442900), 'red'),
          '1':((-0.12490963567885897, 51.46512754750073),'green'),
          '2':((-0.14098394494189165, 51.46733802607161), 'blue')}

m = StaticMap(600, 400, 5)

for coord in coords.values():
    marker = CircleMarker(coord[0], coord[1], 12)
    m.add_marker(marker)

image = m.render()
image.save('images/map.png')