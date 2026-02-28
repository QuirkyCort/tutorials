# HSV and RGB

In Pybricks, the EV3 color sensor only provides RGB values while the Spike Prime only provides HSV values. To convert between them, you can use the following functions.

## RGB to HSV

```python
# Expects RGB values to be in the range of 0 to 100
# Returns HSV in the range of 0-360 (H) and 0-100 (S,V)

def rgb_to_hsv(rgb):
    hsv = [0, 0, 0]
    normRgb = [0, 0, 0]

    for i in range(3):
      normRgb[i] = rgb[i] / 100

    cMax = max(normRgb)
    cMin = min(normRgb)
    diff = cMax - cMin

    if cMax == cMin:
      hsv[0] = 0
    elif cMax == normRgb[0]:
      hsv[0] = 60 * (normRgb[1] - normRgb[2]) / diff
    elif cMax == normRgb[1]:
      hsv[0] = 60 * (2 + (normRgb[2] - normRgb[0]) / diff)
    else:
      hsv[0] = 60 * (4 + (normRgb[0] - normRgb[1]) / diff)

    if hsv[0] < 0:
      hsv[0] += 360

    if cMax == 0:
      hsv[1] = 0
    else:
      hsv[1] = diff / cMax * 100

    hsv[2] = cMax * 100

    return hsv
```

## HSV to RGB

```python
# Expects H to be in the range of 0 to 360. S and V should be in the range of 0 to 100
# Returns RGB in the range of 0-100

def hsv_to_rgb(hsv):
    h, s, v = hsv.h, hsv.s / 100, hsv.v / 100

    c = v * s

    h1 = h / 60
    x = c * (1 - abs(h1 % 2 - 1))
    if h1 < 1:
        r1, g1, b1 = c, x, 0
    elif h1 < 2:
        r1, g1, b1 = x, c, 0
    elif h1 < 3:
        r1, g1, b1 = 0, c, x
    elif h1 < 4:
        r1, g1, b1 = 0, x, c
    elif h1 < 5:
        r1, g1, b1 = x, 0, c
    else:
        r1, g1, b1 = c, 0, x

    m = v - c
    return (100 * (r1 + m), 100 * (g1 + m), 100 * (b1 + m))
```