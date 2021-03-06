from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node
from custom_src.retain import m

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        self.img_unRgba = None
        self.img_Rgba = None

        self.initialized()


    def update_event(self, input_called=-1):
        self.img_unRgba= self.input(0)
      
        self.img_Rgba= cv2.cvtColor(self.img_unRgba,cv2.COLOR_BGRA2RGBA)
        #self.cnvt=cv2.imshow('gray_image',self.img_Rgb)
        self.main_widget.show_image(self.img_Rgba)
        self.set_output_val(0, self.img_Rgba)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...



    # optional - important for threading - stop everything here
    def removing(self):
        pass
