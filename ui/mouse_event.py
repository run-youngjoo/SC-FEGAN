# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np

class GraphicsScene(QGraphicsScene):
    def __init__(self, mode_list, parent=None):
        QGraphicsScene.__init__(self, parent)
        self.modes = mode_list
        self.mouse_clicked = False
        self.prev_pt = None

        # self.masked_image = None

        # save the points
        self.mask_points = []
        self.sketch_points = []
        self.stroke_points = []

        # strokes color
        self.stk_color = None

    def reset(self):
        # save the points
        self.mask_points = []
        self.sketch_points = []
        self.stroke_points = []

        # strokes color
        self.stk_color = None

        self.prev_pt = None

    def mousePressEvent(self, event):
        self.mouse_clicked = True

    def mouseReleaseEvent(self, event):
        self.prev_pt = None
        self.mouse_clicked = False

    def mouseMoveEvent(self, event):
        if self.mouse_clicked:
            if self.modes[0] == 1:
                if self.prev_pt:
                    self.drawMask(self.prev_pt, event.scenePos())
                    pts = {}
                    pts['prev'] = (int(self.prev_pt.x()),int(self.prev_pt.y()))
                    pts['curr'] = (int(event.scenePos().x()),int(event.scenePos().y()))
                    self.mask_points.append(pts)
                    self.prev_pt = event.scenePos()
                else:
                    self.prev_pt = event.scenePos()
            elif self.modes[1] == 1:
                if self.prev_pt:
                    self.drawSketch(self.prev_pt, event.scenePos())
                    pts = {}
                    pts['prev'] = (int(self.prev_pt.x()),int(self.prev_pt.y()))
                    pts['curr'] = (int(event.scenePos().x()),int(event.scenePos().y()))
                    self.sketch_points.append(pts)
                    self.prev_pt = event.scenePos()
                else:
                    self.prev_pt = event.scenePos()
            elif self.modes[2] == 1:
                if self.prev_pt:
                    self.drawStroke(self.prev_pt, event.scenePos())
                    pts = {}
                    pts['prev'] = (int(self.prev_pt.x()),int(self.prev_pt.y()))
                    pts['curr'] = (int(event.scenePos().x()),int(event.scenePos().y()))
                    pts['color'] = self.stk_color
                    self.stroke_points.append(pts)
                    self.prev_pt = event.scenePos()
                else:
                    self.prev_pt = event.scenePos()

    def drawMask(self, prev_pt, curr_pt):
        lineItem = QGraphicsLineItem(QLineF(prev_pt, curr_pt))
        lineItem.setPen(QPen(Qt.white, 12, Qt.SolidLine)) # rect
        self.addItem(lineItem)

    def drawSketch(self, prev_pt, curr_pt):
        lineItem = QGraphicsLineItem(QLineF(prev_pt, curr_pt))
        lineItem.setPen(QPen(Qt.black, 1, Qt.SolidLine)) # rect
        self.addItem(lineItem)

    def drawStroke(self, prev_pt, curr_pt):
        lineItem = QGraphicsLineItem(QLineF(prev_pt, curr_pt))
        lineItem.setPen(QPen(QColor(self.stk_color), 4, Qt.SolidLine)) # rect
        self.addItem(lineItem)

    def get_stk_color(self, color):
        self.stk_color = color

    def erase_prev_pt(self):
        self.prev_pt = None