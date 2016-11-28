from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPen, QBrush, QPainterPath, QPainter, QPolygon, QPalette
from PyQt5.QtCore import QSize, QPoint, QRect, Qt


class RenderArea(QWidget):

    Shape = {'Line': 1,
             'Points': 2,
             'Polygon': 3,
             'Rect': 4,
             'RoundedRect': 5,
             'Ellipse': 6,
             'Pie': 7,
             'Chord': 8,
             'Path': 9,
             'Polyline': 10,
             'Arc': 11,
             'Text': 12,
             'Pixmap': 13}

    def __init__(self):
        super(RenderArea, self).__init__()

        self.shape = self.Shape['Polygon']
        self.antialiased = False
        self.transformed = False

        self.pixmap = QPixmap("./images/qt-logo.png")

        pallet = QPalette()
        pallet.setColor(QPalette.Background, Qt.black)
        self.setPalette(pallet)
        self.setAutoFillBackground(True)

        self.pen = QPen()
        self.brush = QBrush()

    def sizeHint(self):
        return QSize(400, 200)

    def minimumSize(self):
        return QSize(100, 100)

    def setShape(self, shape):
        self.shape = shape
        self.update()

    def setPen(self, pen):
        self.pen = pen
        self.update()

    def setBrush(self, brush):
        self.brush = brush
        self.update()

    def setAntialiased(self, antialiased):
        self.antialiased = antialiased
        self.update()

    def setTransformed(self, transformed):
        self.transformed = transformed
        self.update()

    def paintEvent(self, event):
        point1 = QPoint(10, 80)
        point2 = QPoint(20, 10)
        point3 = QPoint(80, 30)
        point4 = QPoint(90, 70)

        startAngle = 20 * 16
        arcLength = 120 * 16

        points = [point1, point2, point3, point4]

        rect = QRect(10, 20, 80, 60)

        path = QPainterPath()
        path.moveTo(20, 80)
        path.lineTo(20, 30)
        path.cubicTo(80, 0, 50, 50, 80, 80)

        painter = QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)

        if self.antialiased:
            painter.setRenderHint(QPainter.Antialiasing, True)

        for i in range(0, self.width(), 100):
            for j in range(0, self.height(), 50):


                painter.save()
                painter.translate(i, j)

                if self.transformed:
                    painter.translate(50, 50)
                    painter.rotate(60.0)
                    painter.scale(0.6, 0.9)
                    painter.translate(-50, -50)

                if self.shape == self.Shape['Line']:
                    painter.drawLine(10.0, 50.0, 10.0, 80.0)
                    break
                elif self.shape == self.Shape['Points']:
                    painter.drawPoints(QPolygon(points))
                    break
                elif self.shape == self.Shape['Polygon']:
                    painter.drawPolygon(QPolygon(points))
                    break
                elif self.shape == self.Shape['Rect']:
                    painter.drawRect(rect)
                    break
                elif self.shape == self.Shape['Polyline']:
                    painter.drawPolyline(QPolygon(points))
                    break
                elif self.shape == self.Shape['RoundedRect']:
                    painter.drawRoundedRect(rect, 25, 25, Qt.RelativeSize)
                    break
                elif self.shape == self.Shape['Ellipse']:
                    painter.drawEllipse(rect)
                    break
                elif self.shape == self.Shape['Arc']:
                    painter.drawArc(rect, startAngle, arcLength)
                    break
                elif self.shape == self.Shape['Chord']:
                    painter.drawChord(rect, arcLength, arcLength)
                    break
                elif self.shape == self.Shape['Pie']:
                    painter.drawPie(rect, startAngle, arcLength)
                    break
                elif self.shape == self.Shape['Path']:
                    painter.drawPath(path)
                    break
                elif self.shape == self.Shape['Text']:
                    painter.drawText(rect, Qt.AlignCenter, "Qt by\nThe Qt Company")
                    break
                elif self.shape == self.Shape['Pixmap']:
                    painter.drawPixmap(10, 10, self.pixmap)
                    break

            painter.restore()

        painter.setRenderHint(QPainter.Antialiasing, False)
        painter.setPen(Qt.white)
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(QRect(0, 0, self.width() - 1, self.height() - 1))

