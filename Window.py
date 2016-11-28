import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QGridLayout, QSpinBox, QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QLinearGradient, QRadialGradient, QConicalGradient, QBrush, QPixmap
from RenderArea import RenderArea


class Window(QWidget):

    IdRole = Qt.UserRole

    def __init__(self):
        super(Window, self).__init__()
        self.window()



    def window(self):

        self.renderArea = RenderArea()

        self.shapeComboBox = QComboBox()
        self.shapeComboBox.addItem("Line", self.renderArea.Shape['Line'])
        self.shapeComboBox.addItem("Points", self.renderArea.Shape['Points'])
        self.shapeComboBox.addItem("Polygon", self.renderArea.Shape['Polygon'])
        self.shapeComboBox.addItem("Rect", self.renderArea.Shape['Rect'])
        self.shapeComboBox.addItem("RoundedRect", self.renderArea.Shape['RoundedRect'])
        self.shapeComboBox.addItem("Ellipse", self.renderArea.Shape['Ellipse'])
        self.shapeComboBox.addItem("Pie", self.renderArea.Shape['Pie'])
        self.shapeComboBox.addItem("Chord", self.renderArea.Shape['Chord'])
        self.shapeComboBox.addItem("Path", self.renderArea.Shape['Path'])
        self.shapeComboBox.addItem("Polyline", self.renderArea.Shape['Polyline'])
        self.shapeComboBox.addItem("Arc", self.renderArea.Shape['Arc'])
        self.shapeComboBox.addItem("Text", self.renderArea.Shape['Text'])
        self.shapeComboBox.addItem("Pixmap", self.renderArea.Shape['Pixmap'])

        shapeLabel = QLabel('&Shape:')
        shapeLabel.setBuddy(self.shapeComboBox)

        self.penWidthSpenBox = QSpinBox()
        self.penWidthSpenBox.setRange(0, 20)
        self.penWidthSpenBox.setSpecialValueText("0 (cosmetic pen)")

        penWidthLabel = QLabel('Pen &Width:')
        penWidthLabel.setBuddy(self.penWidthSpenBox)

        self.penStyleComboBox = QComboBox()
        self.penStyleComboBox.addItem("Solid", Qt.SolidLine)
        self.penStyleComboBox.addItem("Dash", Qt.DashLine)
        self.penStyleComboBox.addItem("Dot", Qt.DotLine)
        self.penStyleComboBox.addItem("Dash Dot", Qt.DashDotLine)
        self.penStyleComboBox.addItem("Dash Dot Dot", Qt.DashDotDotLine)
        self.penStyleComboBox.addItem("None", Qt.NoPen)

        penStyleLabel = QLabel('&Pen Style')
        penStyleLabel.setBuddy(self.penStyleComboBox)

        self.penCapComboBox = QComboBox()
        self.penCapComboBox.addItem("Flat", Qt.FlatCap)
        self.penCapComboBox.addItem("Square", Qt.SquareCap)
        self.penCapComboBox.addItem("Round", Qt.RoundCap)

        penCapLabel = QLabel("Pen &Cap:")
        penCapLabel.setBuddy(self.penCapComboBox)

        self.penJoinComboBox = QComboBox()
        self.penJoinComboBox.addItem("Miter", Qt.MiterJoin)
        self.penJoinComboBox.addItem("Bevel", Qt.BevelJoin)
        self.penJoinComboBox.addItem("Round", Qt.RoundJoin)

        penJoinLabel = QLabel('Pen &Join:')
        penJoinLabel.setBuddy(self.penJoinComboBox)

        self.brushStyleComboBox = QComboBox()
        self.brushStyleComboBox.addItem("Linear Gradient", Qt.LinearGradientPattern)
        self.brushStyleComboBox.addItem("Radial Gradient", Qt.RadialGradientPattern)
        self.brushStyleComboBox.addItem("Conical Gradient", Qt.ConicalGradientPattern)
        self.brushStyleComboBox.addItem("Texture", Qt.TexturePattern)
        self.brushStyleComboBox.addItem("Solid", Qt.SolidPattern)
        self.brushStyleComboBox.addItem("Horizontal", Qt.HorPattern)
        self.brushStyleComboBox.addItem("Vertical", Qt.VerPattern)
        self.brushStyleComboBox.addItem("Cross", Qt.CrossPattern)
        self.brushStyleComboBox.addItem("Backward Diagonal", Qt.BDiagPattern)
        self.brushStyleComboBox.addItem("Forward Diagonal", Qt.FDiagPattern)
        self.brushStyleComboBox.addItem("Diagonal Cross", Qt.DiagCrossPattern)
        self.brushStyleComboBox.addItem("Dense 1", Qt.Dense1Pattern)
        self.brushStyleComboBox.addItem("Dense 2", Qt.Dense2Pattern)
        self.brushStyleComboBox.addItem("Dense 3", Qt.Dense3Pattern)
        self.brushStyleComboBox.addItem("Dense 4", Qt.Dense4Pattern)
        self.brushStyleComboBox.addItem("Dense 5", Qt.Dense5Pattern)
        self.brushStyleComboBox.addItem("Dense 6", Qt.Dense6Pattern)
        self.brushStyleComboBox.addItem("Dense 7", Qt.Dense7Pattern)

        brushStyleLabel = QLabel("&Brush")
        brushStyleLabel.setBuddy(self.brushStyleComboBox)

        otherOptionsLabel = QLabel("Options:")
        antialiasingCheckBox = QCheckBox("&Antialiasing")
        transformationsCheckBos = QCheckBox("&Transformations")



        #Connects
        self.shapeComboBox.activated.connect(self.shapeChanged)
        self.penWidthSpenBox.valueChanged.connect(self.penChanged)
        self.penStyleComboBox.activated.connect(self.penChanged)
        self.penCapComboBox.activated.connect(self.penChanged)
        self.penJoinComboBox.activated.connect(self.penChanged)
        self.brushStyleComboBox.activated.connect(self.brushChanged)
        antialiasingCheckBox.toggled.connect(self.renderArea.setAntialiased)
        transformationsCheckBos.toggled.connect(self.renderArea.setTransformed)


        mainLayout = QGridLayout()
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(3, 1)
        mainLayout.addWidget(self.renderArea, 0, 0, 1, 4)
        mainLayout.addWidget(shapeLabel, 2, 0, Qt.AlignRight)
        mainLayout.addWidget(self.shapeComboBox, 2, 1)
        mainLayout.addWidget(penWidthLabel, 3, 0, Qt.AlignRight)
        mainLayout.addWidget(self.penWidthSpenBox, 3, 1)
        mainLayout.addWidget(penStyleLabel, 4, 0, Qt.AlignRight)
        mainLayout.addWidget(self.penStyleComboBox, 4, 1)
        mainLayout.addWidget(penCapLabel, 3, 2, Qt.AlignRight)
        mainLayout.addWidget(self.penCapComboBox, 3, 3)
        mainLayout.addWidget(penJoinLabel, 2, 2, Qt.AlignRight)
        mainLayout.addWidget(self.penJoinComboBox, 2, 3)
        mainLayout.addWidget(brushStyleLabel, 4, 2, Qt.AlignRight)
        mainLayout.addWidget(self.brushStyleComboBox, 4, 3)
        mainLayout.addWidget(otherOptionsLabel, 5, 0, Qt.AlignRight)
        mainLayout.addWidget(antialiasingCheckBox, 5, 1, 1, 1, Qt.AlignRight)
        mainLayout.addWidget(transformationsCheckBos, 5, 2, 1, 2, Qt.AlignRight)
        self.setLayout(mainLayout)
        self.shapeChanged()
        self.penChanged()
        self.brushChanged()

        antialiasingCheckBox.setChecked(True)

        self.setWindowTitle('Basic Drawing')
        self.show()

    def shapeChanged(self):
        shape = self.renderArea.Shape[self.shapeComboBox.currentText()]
        self.renderArea.setShape(shape)

    def penChanged(self):
        width = self.penWidthSpenBox.value()
        style = Qt.PenStyle(self.penStyleComboBox.itemData(self.penStyleComboBox.currentIndex(), self.IdRole))
        cap = Qt.PenCapStyle(self.penCapComboBox.itemData(self.penCapComboBox.currentIndex(), self.IdRole))
        join = Qt.PenJoinStyle(self.penJoinComboBox.itemData(self.penJoinComboBox.currentIndex(), self.IdRole))
        self.renderArea.setPen(QPen(Qt.white, width, style, cap, join))

    def brushChanged(self):
        style = Qt.BrushStyle(self.brushStyleComboBox.itemData(self.brushStyleComboBox.currentIndex(), self.IdRole))

        if style == Qt.LinearGradientPattern:
            linearGradient = QLinearGradient(0, 0, 100, 100)
            linearGradient.setColorAt(0.0, Qt.white)
            linearGradient.setColorAt(0.2, Qt.green)
            linearGradient.setColorAt(1.0, Qt.black)
            self.renderArea.setBrush(linearGradient)
        elif style == Qt.RadialGradientPattern:
            radialGradient = QRadialGradient(50, 50, 50, 70, 70)
            radialGradient.setColorAt(0.0, Qt.white)
            radialGradient.setColorAt(0.2, Qt.green)
            radialGradient.setColorAt(1.0, Qt.black)
            self.renderArea.setBrush(radialGradient)
        elif style == Qt.ConicalGradientPattern:
            conicalGradient = QConicalGradient(50, 50, 150)
            conicalGradient.setColorAt(0.0, Qt.white)
            conicalGradient.setColorAt(0.2, Qt.green)
            conicalGradient.setColorAt(1.0, Qt.black)
            self.renderArea.setBrush(conicalGradient)
        elif style == Qt.TexturePattern:
            self.renderArea.setBrush(QBrush(QPixmap(":/images/brick.png")))
        else:
            self.renderArea.setBrush(QBrush(Qt.green, style))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
