"""ROI segmentation for the napari-curvealign plugin.

The implementation ships in the tme-quant release as
:mod:`tme_quant.segmentation`. This module re-exports that API so the
plugin can keep importing ``napari_curvealign.segmentation``.
"""

from tme_quant.segmentation import (
    SegmentationMethod,
    SegmentationOptions,
    check_available_methods,
    create_tumor_boundary_rois,
    get_recommended_parameters,
    masks_to_roi_data,
    segment_image,
)

__all__ = [
    "SegmentationMethod",
    "SegmentationOptions",
    "check_available_methods",
    "create_tumor_boundary_rois",
    "get_recommended_parameters",
    "masks_to_roi_data",
    "segment_image",
]
