import Graphics
import Myro
Myro.init("COM3")
rob = Myro.get.Robot()

win = Graphics.Windows("Mi Ventana",320,240)
win.show()

while(win.Visible)
irLeft = rob.getIR("left")
irRight = rob.getIR("right")

distanceLeft = rob.getDistance("left")
distanceReght = rob.grtDistance("right")
text = text(Point(100,50)),"ir_left"