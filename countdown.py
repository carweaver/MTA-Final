#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import datetime
def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 
      
# Driver program 

class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        red = graphics.Color(255, 0, 0)
        blue = graphics.Color(0, 0, 255)
        while True:
          counter = str(datetime.datetime(2020, 1, 17,15,20,0) - datetime.datetime.today())
          graphics.DrawText(canvas, font, 2, 10, blue, counter)
          time.sleep(1)
          canvas.Clear()
        
        

        time.sleep(10)   # show display for 10 seconds before exit


# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
