### napari-curvealign

napari plugin for [CurveAlign](https://loci.wisc.edu/software/curvealign/). Curvelet quantification lives in [tme-quant](https://github.com/uw-loci/tme-quant) and is imported as `pycurvelets`. This repository is the interactive UI, including ROI segmentation (`napari_curvealign.segmentation`).

Cellpose and StarDist are optional:

```bash
uv sync --extra segmentation
```

### Install

```bash
uv sync
uv run napari
```

Open **Plugins → napari-curvealign** (display name **CurveAlign**).

tme-quant still registers its own copy of this plugin. After [PR 63](https://github.com/uw-loci/tme-quant/pull/63) and [PR 64](https://github.com/uw-loci/tme-quant/pull/64) are merged, a follow-up pull request in tme-quant can remove `src/napari_curvealign` and point here. Until that lands, installing both packages can show two CurveAlign widgets.

### Tests

```bash
QT_QPA_PLATFORM=offscreen uv run pytest -q
```
