import sys
import numpy

import Orange.data
from Orange.widgets import widget, gui
from Orange.widgets.utils.signals import Input, Output


class OWDataSamplerA(widget.OWWidget):
    name = "Data Sampler"
    description = "Randomly selects a subset of instances from the data set"
    icon = "icons/DataSamplerA.svg"
    priority = 10

    class Inputs:
        data = Input("Data", Orange.data.Table)

    class Outputs:
        sample = Output("Sampled Data", Orange.data.Table)

    want_main_area = False

    def __init__(self):
        super().__init__()

        # GUI
        box = gui.widgetBox(self.controlArea, "Info")
        self.infoa = gui.widgetLabel(
            box, "No data on input yet, waiting to get something.")
        self.infob = gui.widgetLabel(box, '')