"""Angaar: satellite reclamation check (reproduces the numbers on slide 4).

Reads free Sentinel-2 L2A images from the Earth Search STAC catalogue (no login),
computes NDVI inside a declared reclamation polygon, and reports the green area.

    pip install rasterio pyproj numpy
    python satellite_check.py

The polygon is an overburden dump in Jharia coalfield. The satellite values are real;
the "declared" figure is a simulated number for the demo.
"""
import json
import urllib.request

import numpy as np
import rasterio
from rasterio.features import geometry_mask
from rasterio.windows import from_bounds
from pyproj import Transformer

STAC = "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/"
SCENES = {"2025-03-02": "S2B_45QVG_20250302_0_L2A", "2026-03-02": "S2C_45QVG_20260302_0_L2A"}

# east OB dump, Jharia coalfield (lon, lat)
DUMP = [(86.41253, 23.76021), (86.41645, 23.76091), (86.41989, 23.75934),
        (86.42064, 23.75618), (86.41746, 23.75481), (86.41353, 23.75615)]
DECLARED_HA = 12.0          # simulated value typed in by the mine
GREEN_NDVI = 0.30           # median NDVI of natural vegetation 3 km west, same image


def ndvi_inside(item_id):
    item = json.load(urllib.request.urlopen(STAC + item_id))
    to_utm = Transformer.from_crs("EPSG:4326", "EPSG:32645", always_xy=True)
    ring = [to_utm.transform(lon, lat) for lon, lat in DUMP]
    xs, ys = [p[0] for p in ring], [p[1] for p in ring]
    bands = {}
    with rasterio.Env(AWS_NO_SIGN_REQUEST="YES"):
        for name in ("red", "nir"):
            with rasterio.open(item["assets"][name]["href"]) as src:
                win = from_bounds(min(xs) - 50, min(ys) - 50, max(xs) + 50, max(ys) + 50, src.transform)
                win = win.round_offsets().round_lengths()
                bands[name] = src.read(1, window=win).astype("float32")
                transform = src.window_transform(win)
    red, nir = bands["red"], bands["nir"]
    ndvi = np.where((nir + red) > 0, (nir - red) / (nir + red), np.nan)
    inside = geometry_mask([{"type": "Polygon", "coordinates": [ring + [ring[0]]]}],
                           out_shape=ndvi.shape, transform=transform, invert=True)
    pixel_ha = 10 * 10 / 10000
    # exact polygon area (shoelace formula in UTM metres), and green 10 m pixels inside it
    area_ha = abs(sum(xs[i] * ys[i - 1] - xs[i - 1] * ys[i] for i in range(len(xs)))) / 2 / 10000
    return area_ha, np.nansum(ndvi[inside] >= GREEN_NDVI) * pixel_ha


if __name__ == "__main__":
    for day, item_id in SCENES.items():
        area, green = ndvi_inside(item_id)
        print(f"{day}: dump area {area:.1f} ha, green (NDVI >= {GREEN_NDVI}) {green:.1f} ha")
    print(f"Declared reclaimed: {DECLARED_HA:.1f} ha -> mismatch if green area is well below it")
