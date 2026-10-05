### napari-curvealign

napari plugin for [CurveAlign](https://loci.wisc.edu/software/curvealign/). Curvelet quantification and ROI segmentation live in [tme-quant](https://github.com/uw-loci/tme-quant). This package is the interactive UI.

`napari_curvealign.segmentation` re-exports `tme_quant.segmentation`. Cellpose and StarDist stay an extra of the library:

```bash
uv pip install 'tme-quant[segmentation]'
```

### Install

The library split is on the `split-napari-curvealign` branch until that pull request merges. This package depends on that branch. After it is on `main`, change the `tme-quant` dependency in `pyproject.toml` to `uw-loci/tme-quant` `main`.

```bash
uv sync
uv run napari
```

Open **Plugins → napari-curvealign** (display name **CurveAlign**).

### Tests

```bash
QT_QPA_PLATFORM=offscreen uv run pytest -q
```
