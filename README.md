### napari-curvealign

napari plugin for [CurveAlign](https://loci.wisc.edu/software/curvealign/). Curvelet quantification lives in [tme-quant](https://github.com/uw-loci/tme-quant) and is imported as `pycurvelets`. This repository is only that UI. `src/` is the `napari_curvealign` package, including ROI segmentation.

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

tme-quant is pinned to the `v0.1.0-pre-split` tag, the last version whose repo root installs as one package. That version still registers its own copy of this plugin, so napari can show two CurveAlign widgets. [tme-quant#73](https://github.com/uw-loci/tme-quant/pull/73) removes that copy, and [tme-quant#74](https://github.com/uw-loci/tme-quant/pull/74) splits tme-quant into `pycurvelets-core` plus curvelet backend projects; once both are merged this dependency moves to `pycurvelets-core`.

### Tests

```bash
QT_QPA_PLATFORM=offscreen uv run pytest -q
```
