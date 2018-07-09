import copy
from matplotlib.patches import Ellipse, Rectangle
from matplotlib.patheffects import Normal, Stroke
import numpy as np
from PyQt5 import QtCore, QtWidgets


# Classes to handle different interactive modes in matplotlib_widget.

class ModeHandler:
    def __init__(self, matplotlib_widget):
        self.matplotlib_widget = matplotlib_widget

    def clear(self):
        pass

    def move_to_new_axes(self):
        pass

    def on_axes_enter(self, event):
        pass

    def on_axes_leave(self, event):
        pass

    def on_mouse_down(self, event):
        pass

    def on_mouse_up(self, event):
        pass

    def on_mouse_move(self, event):
        pass


# Abstract base class for all region handlers.
class RegionHandler(ModeHandler):
    def __init__(self, matplotlib_widget, listener):
        super().__init__(matplotlib_widget)
        self._listener = listener
        self._line_colour = 'k'
        self._shadow_colour = 'w'
        self._shadow_alpha = 0.75
        self._region_alpha = 0.75

        self._editing = False
        self._points = np.empty((0, 2))
        self._artists = []         # List of artists.
        self._region = None        # Boolean array.
        self._region_image = None  # Image showing region.

    def _create_region_image(self):
        if self._region is not None:
            masked = np.ma.masked_equal(self._region, True)

            cmap = self.matplotlib_widget._create_white_colormap()
            return self.matplotlib_widget._map_axes.imshow( \
                masked, alpha=self._region_alpha, cmap=cmap)
        else:
            return None

    def _finish_editing(self):
        self._editing = False
        self._region = self._calculate_region()
        self._region_image = self._create_region_image()

        self.matplotlib_widget._redraw()
        self.update_listener()

    def _get_path_effects(self):
        return [Stroke(linewidth=3, foreground=self._shadow_colour,
                       alpha=self._shadow_alpha),
                Normal()]

    def clear(self):
        if self.matplotlib_widget._map_axes is not None:
            self._points = np.empty((0, 2))

            for artist in self._artists:
                if artist is not None:
                    artist.remove()
            self._artists = []

            if self._region is not None:
                self._region = None

            if self._region_image is not None:
                self._region_image.remove()
                self._region_image = None

            self._editing = False
            self.matplotlib_widget._redraw()
            self.update_listener()

    def get_region(self):
        return self._region

    def has_region(self):
        return self._region is not None

    def move_to_new_axes(self):
        self._artists = None
        self._region_image = None

        if self.matplotlib_widget._map_axes:
            self._artists = self._create_artists()
            if self._region is not None:
                self._region_image = self._create_region_image()

    def on_axes_enter(self, event):
        if (event.inaxes is not None and
            event.inaxes == self.matplotlib_widget._map_axes):

            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CrossCursor)

    def on_axes_leave(self, event):
        if (event.inaxes is not None and
            event.inaxes == self.matplotlib_widget._map_axes):

            QtWidgets.QApplication.restoreOverrideCursor()

    def update_listener(self):
        if self._listener:
            self._listener.update_from_mode_handler()


# Abstract base class for region handlers that are controlled by a single drag
# of the mouse.
class MouseDragRegionHandler(RegionHandler):
    def __init__(self, matplotlib_widget, listener):
        super().__init__(matplotlib_widget, listener)

    def on_mouse_down(self, event):
        if (not self._editing and
            self.matplotlib_widget._map_axes is not None and
            event.button == 1 and event.dblclick == False and
            event.inaxes == self.matplotlib_widget._map_axes):

            if self._artists:
                self.clear()

            self._editing = True
            self._points = np.asarray([[event.xdata, event.ydata],
                                       [event.xdata, event.ydata]])
            self._artists = self._create_artists()
            self.matplotlib_widget._redraw()

    def on_mouse_move(self, event):
        if (self._editing and self._artists and
            event.inaxes == self.matplotlib_widget._map_axes):

            self._points[1] = (event.xdata, event.ydata)
            self._move_artists()
            self.matplotlib_widget._redraw()

    def on_mouse_up(self, event):
        if (self._editing and self._artists and
            event.button == 1 and event.dblclick == False):

            self._finish_editing()


class EllipseRegionHandler(MouseDragRegionHandler):
    def __init__(self, matplotlib_widget, listener):
        super().__init__(matplotlib_widget, listener)

    def _calculate_region(self):
        project = self.matplotlib_widget._owning_window._project
        if project is not None:
            centre = self._artists[0].center
            size = (self._artists[0].width, self._artists[0].height)
            return project.calculate_region_ellipse(centre, size)
        else:
            return None

    def _create_artists(self):
        centre, size = self._get_centre_and_size()
        ellipse = Ellipse(centre, width=size[0], height=size[1],
                          fc='none', ec=self._line_colour)
        ellipse = self.matplotlib_widget._map_axes.add_patch(ellipse)
        ellipse.set_path_effects(self._get_path_effects())
        return [ellipse]

    def _get_centre_and_size(self):
        start = self._points[0]
        end = self._points[1]
        centre = (start + end)*0.5
        size = end - start
        return centre, size


    def _move_artists(self):
        centre, size = self._get_centre_and_size()
        self._artists[0].center = centre
        self._artists[0].width  = size[0]
        self._artists[0].height = size[1]
        self._artists[0].stale = True

    def get_shape_string(self):
        return 'ellipse'


class RectangleRegionHandler(MouseDragRegionHandler):
    def __init__(self, matplotlib_widget, listener):
        super().__init__(matplotlib_widget, listener)

    def _calculate_region(self):
        project = self.matplotlib_widget._owning_window._project
        if project is not None:
            corner0 = self._artists[0].get_xy()
            corner1 = (corner0[0] + self._artists[0].get_width(),
                       corner0[1] + self._artists[0].get_height())
            return project.calculate_region_rectangle(corner0, corner1)
        else:
            return None

    def _create_artists(self):
        start = self._points[0]
        size = self._points[1] - start
        rectangle = Rectangle(start, width=size[0], height=size[1],
                              fc='none', ec=self._line_colour)
        rectangle = self.matplotlib_widget._map_axes.add_patch(rectangle)
        rectangle.set_path_effects(self._get_path_effects())
        return [rectangle]

    def _move_artists(self):
        start = self._points[0]
        end = self._points[1]
        self._artists[0].set_width( end[0] - start[0])
        self._artists[0].set_height(end[1] - start[1])

    def get_shape_string(self):
        return 'rectangle'


class PolygonRegionHandler(RegionHandler):
    # 3 artists: lines, markers and highlight marker.
    def __init__(self, matplotlib_widget, listener):
        super().__init__(matplotlib_widget, listener)

    def _add_point(self, point):
        # Add point to end of self._points, but only if it is not the same as
        # the last point.
        if len(self._points) == 0 or not np.allclose(point, self._points[-1]):
            self._points = np.vstack((self._points, point))

            if not self._artists:
                self._artists = self._create_artists()
            else:
                self._artists[0].set_data(self._points[:, 0], self._points[:, 1])
                self._artists[1].set_data(self._points[:, 0], self._points[:, 1])
            self.matplotlib_widget._redraw()

    def _calculate_region(self):
        project = self.matplotlib_widget._owning_window._project
        if project is not None:
            return project.calculate_region_polygon(self._points)
        else:
            return None

    def _close_polygon(self):
        if self._artists:
            self._points = np.vstack((self._points, self._points[0]))
            x = self._points[:, 0]
            y = self._points[:, 1]
            self._artists[0].set_data(x, y)
            self._artists[1].set_data(x, y)

            self._finish_editing()

    def _create_artists(self):
        colour = self._line_colour
        lines = self.matplotlib_widget._map_axes.plot( \
            self._points[:, 0], self._points[:, 1], '-', c=colour)[0]
        markers = self.matplotlib_widget._map_axes.plot(\
            self._points[:, 0], self._points[:, 1], 'o', c=colour)[0]

        path_effects = self._get_path_effects()
        lines.set_path_effects(path_effects)
        markers.set_path_effects(path_effects)
        return [lines, markers, None]

    def get_shape_string(self):
        return 'polygon'

    def on_mouse_down(self, event):
        if (event.button == 1 and event.inaxes is not None and
            event.inaxes == self.matplotlib_widget._map_axes):

            if not self._editing:
                self.clear()
                self._editing = True

            if event.dblclick or (self._artists and self._artists[2]):
                self._close_polygon()
            else:
                self._add_point((event.xdata, event.ydata))

    def on_mouse_move(self, event):
        if (self._artists and self._artists[0] is not None and
            len(self._artists[0].get_xdata()) > 1):

            inside, matches = self._artists[1].contains(event)
            if inside:
                if self._artists[2] is None and 0 in matches['ind']:
                    self._artists[2] = self.matplotlib_widget._map_axes.plot(\
                        self._points[0, 0], self._points[0, 1], 'o', c='yellow')[0]
                    self.matplotlib_widget._redraw()
            elif self._artists[2]:
                self._artists[2].remove()
                self._artists[2] = None
                self.matplotlib_widget._redraw()


class ZoomHandler(ModeHandler):
    def __init__(self, matplotlib_widget):
        super().__init__(matplotlib_widget)
        self._zoom_rectangle = None  # Only set when zooming.

    def clear(self):
        if (self._zoom_rectangle is not None and
            self.matplotlib_widget._map_axes is not None):

            self._zoom_rectangle.remove()
            self._zoom_rectangle = None

            self.matplotlib_widget._redraw()

    def on_axes_enter(self, event):
        if (event.inaxes is not None and
            event.inaxes == self.matplotlib_widget._map_axes):

            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CrossCursor)

    def on_axes_leave(self, event):
        if (event.inaxes is not None and
            event.inaxes == self.matplotlib_widget._map_axes):

            QtWidgets.QApplication.restoreOverrideCursor()

    def on_mouse_down(self, event):
        if (self._zoom_rectangle is None and
            self.matplotlib_widget._map_axes is not None and
            event.button == 1 and event.dblclick == False and
            event.inaxes == self.matplotlib_widget._map_axes):

            rectangle = Rectangle((event.xdata, event.ydata), width=0, height=0,
                                  fc='none', ec='k', ls='--')
            self._zoom_rectangle = \
                self.matplotlib_widget._map_axes.add_patch(rectangle)
            self.matplotlib_widget._redraw()

    def on_mouse_move(self, event):
        if (self._zoom_rectangle is not None and
            event.inaxes == self.matplotlib_widget._map_axes):

            x = event.xdata
            y = event.ydata
            self._zoom_rectangle.set_width(x - self._zoom_rectangle.get_x())
            self._zoom_rectangle.set_height(y - self._zoom_rectangle.get_y())
            self.matplotlib_widget._redraw()

    def on_mouse_up(self, event):
        if (self._zoom_rectangle is not None and event.button == 1 and
            event.dblclick == False):

            width = self._zoom_rectangle.get_width()
            height = self._zoom_rectangle.get_height()
            if abs(width) > 1e-10 and abs(height) > 1e-10:
                x = self._zoom_rectangle.get_x()
                y = self._zoom_rectangle.get_y()
                zoom_xs = sorted([x, x+width])
                zoom_ys = sorted([y, y+height], reverse=True)

                from_ = (self.matplotlib_widget._map_axes.get_xlim(),
                         self.matplotlib_widget._map_axes.get_ylim())

                self.matplotlib_widget._owning_window.zoom_append( \
                    from_=from_, to=(zoom_xs, zoom_ys))

            self.clear()
