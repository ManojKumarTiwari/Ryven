from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node
from custom_src.retain import m


# API METHODS

# self.main_widget        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# self.set_output_val(self, index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, append=True, widget_type='', widget_name='', widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_new_output(type_, label, append=True, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')

# ------------------------------------------------------------------------------


class BreakWeather_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(BreakWeather_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        # ...

        self.initialized()

    # don't call self.update_event() directly, use self.update() instead
    def update_event(self, input_called=-1):
        w = self.input(0)
        
        self.set_output_val(0, w.ref_time)
        self.set_output_val(1, w.srise_time)
        self.set_output_val(2, w.sset_time)
        self.set_output_val(3, w.status)
        self.set_output_val(4, w.detailed_status)
        self.set_output_val(5, w.weather_code)
        self.set_output_val(6, w.weather_icon_name)
        self.set_output_val(7, w.clouds)
        self.set_output_val(8, w.visibility_distance)
        self.set_output_val(9, w.dewpoint)
        self.set_output_val(10, w.humidity)
        self.set_output_val(11, w.humidex)
        self.set_output_val(12, w.heat_index)
        self.set_output_val(13, w.utc_offset)
        self.set_output_val(14, w.uvi)
        self.set_output_val(15, w.pressure['press'])
        self.set_output_val(16, w.pressure['sea_level'])
        self.set_output_val(17, w.temp)
        self.set_output_val(18, w.rain)
        self.set_output_val(19, w.wind())
        self.set_output_val(20, w.snow)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...



    # optional - important for threading - stop everything here
    def removing(self):
        pass
