#!/usr/bin/env python

# Tutorial available at: https://www.youtube.com/watch?v=nmb-0KcgXzI
# Feedback welcome: jacksonbates@hotmail.com

from gimpfu import *
from pdb import *

def photo_scan(image, drawable):
    # function code goes here...
    pdb.gimp_image_undo_group_start(image)
    active_layer = image.active_layer
    if active_layer == -1:
      pdb.gimp_message("No active layer")
    layer_copy1 = active_layer.copy()
    layer_copy2 = active_layer.copy()
    image.add_layer(layer_copy1)
    image.add_layer(layer_copy2)
    layer_copy2.mode = LAYER_MODE_GRAIN_EXTRACT
    pdb.plug_in_dilate(image, layer_copy2, 0, 0, 1.0, 0, 0, 255)
    pdb.plug_in_dilate(image, layer_copy2, 0, 0, 1.0, 0, 0, 255)
    pdb.plug_in_dilate(image, layer_copy2, 0, 0, 1.0, 0, 0, 255)
    pdb.plug_in_dilate(image, layer_copy2, 0, 0, 1.0, 0, 0, 255)
    pdb.plug_in_gauss(image, layer_copy2, 10, 10, 0)
    print(layer_copy2.mode)
    result = pdb.gimp_image_merge_down(image, layer_copy2, 0)
    pdb.gimp_drawable_levels(result, HISTOGRAM_VALUE, 0, 0.46, False, 0.6, 0, 1, False)
    pdb.gimp_image_undo_group_end(image)
    

register(
    "python_fu_photo_scan",
    "Corrects sheet of paper",
    "Takes a photograph of a sheet of paper and colors it to be printed",
    "Jason Baldus", 
    "Licensed under GPL v2", 
    "2020",
    "Photo Scan Correct...",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        # basic parameters are: (UI_ELEMENT, "variable", "label", Default)
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
        # PF_SLIDER, SPINNER have an extra tuple (min, max, step)
        # PF_RADIO has an extra tuples within a tuple:
        # eg. (("radio_label", "radio_value), ...) for as many radio buttons
        # PF_OPTION has an extra tuple containing options in drop-down list
        # eg. ("opt1", "opt2", ...) for as many options
        # see ui_examples_1.py and ui_examples_2.py for live examples
    ],
    [],
    photo_scan, 
    menu="<Image>/Script-Fu/Color"
    )  # second item is menu location

main()
