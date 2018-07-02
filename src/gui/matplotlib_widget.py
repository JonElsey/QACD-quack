from enum import Enum, unique
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.figure import Figure
import numpy as np
from PyQt5 import QtCore, QtWidgets

from .enums import ArrayType, ModeType, PlotType
from .mode_handler import *


class MatplotlibWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(MatplotlibWidget, self).__init__(parent)

        self._canvas = FigureCanvas(Figure())
        self._layout = QtWidgets.QVBoxLayout()
        self._layout.addWidget(self._canvas)
        self.setLayout(self._layout)

        self._map_axes = None

        self._image = None       # Image used for element map.
        self._bar = None         # Bar used for histogram.
        self._bar_norm_x = None  # Normalised x-positions of centres of bars
                                 #   in range 0 (= min) to 1.0 (= max value).
        self._array_type = ArrayType.INVALID
        self._cmap_int_max = None  # One beyond end, as in numpy slicing.

        self._valid_colormap_names = self._determine_valid_colormap_names()
        self._colormap_name = 'rainbow'

        # Initialised in initialise().
        self._owning_window = None
        self._mode_type = ModeType.INVALID
        self._mode_handler = None

        self._map_xlim = None        # Zoom to this when create new map.
        self._map_ylim = None

        # Created when first needed.
        self._black_colormap = None
        self._white_colormap = None

    def _adjust_layout(self):
        #self._canvas.figure.tight_layout(pad=1.5)
        pass

    def _create_black_colormap(self):
        if self._black_colormap == None:
            colors = [(0, 0, 0), (0, 0, 0)]
            self._black_colormap = \
                LinearSegmentedColormap.from_list('black', colors, N=1)
        return self._black_colormap

    def _create_white_colormap(self):
        if self._white_colormap == None:
            colors = [(1, 1, 1), (1, 1, 1)]
            self._white_colormap = \
                LinearSegmentedColormap.from_list('white', colors, N=1)
        return self._white_colormap

    def _determine_valid_colormap_names(self):
        # Exclude reversed cmaps which have names ending with '_r'.
        all_ = set(filter(lambda s: not s.endswith('_r'), cm.cmap_d.keys()))

        # Exclude qualitative and repeating cmaps, and the deprecated
        # 'spectral' which has been replaced with 'nipy_spectral'.
        exclude = set(['Accent', 'Dark2', 'Paired', 'Pastel1', 'Pastel2',
                       'Set1', 'Set2', 'Set3', 'Vega10', 'Vega20', 'Vega20b',
                       'Vega20c', 'flag', 'prism', 'spectral', 'tab10',
                       'tab20', 'tab20b', 'tab20c'])
        return sorted(all_.difference(exclude))

    def _redraw(self):
        self._canvas.draw()
        #self._canvas.draw_idle()

    def clear(self):
        # Clear current plots.
        self._zoom_rectangle = None
        self._canvas.figure.clear()
        self._map_axes = None
        self._image = None
        self._bar = None
        self._bar_norm_x = None
        self._array_type = ArrayType.INVALID
        self._cmap_int_max = None  # One beyond end, as in numpy slicing.

        self._redraw()

    def clear_all(self):
        # Clear everything, including cached zoom limits, etc.
        self._map_xlim = None
        self._map_ylim = None
        self.clear()

    def create_colormap(self):
        if self._array_type == ArrayType.PHASE:
            return self._create_black_colormap()
        if self._cmap_int_max is None:
            return cm.get_cmap(self.get_colormap_name())
        else:
            return cm.get_cmap(self.get_colormap_name(), self._cmap_int_max)

    def get_colormap_name(self):
        return self._colormap_name

    def get_valid_colormap_names(self):
        return self._valid_colormap_names

    def initialise(self, owning_window, zoom_enabled=True):
        self._owning_window = owning_window
        if zoom_enabled:
            self._canvas.mpl_connect('axes_enter_event', self.on_axes_enter)
            self._canvas.mpl_connect('axes_leave_event', self.on_axes_leave)
            self._canvas.mpl_connect('button_press_event', self.on_mouse_down)
            self._canvas.mpl_connect('button_release_event', self.on_mouse_up)
            self._canvas.mpl_connect('motion_notify_event', self.on_mouse_move)

            self.set_mode_type(ModeType.ZOOM)
        else:
            self.set_mode_type(ModeType.INVALID)

        self._canvas.mpl_connect('resize_event', self.on_resize)

    def on_axes_enter(self, event):
        if self._mode_handler:
            self._mode_handler.on_axes_enter(event)

    def on_axes_leave(self, event):
        if self._mode_handler:
            self._mode_handler.on_axes_leave(event)

    def on_mouse_down(self, event):
        if self._mode_handler:
            self._mode_handler.on_mouse_down(event)

    def on_mouse_move(self, event):
        if self._mode_handler:
            self._mode_handler.on_mouse_move(event)

    def on_mouse_up(self, event):
        if self._mode_handler:
            self._mode_handler.on_mouse_up(event)

    def on_resize(self, event):
        self._adjust_layout()

    def set_colormap_limits(self, lower, upper):
        if self._image is not None:
            self._image.set_clim(lower, upper)
            cmap = self._image.get_cmap()
            cmap.set_over('w')
            cmap.set_under('w')
            self._redraw()

    def set_colormap_name(self, colormap_name):
        self._colormap_name = colormap_name
        cmap = self.create_colormap()

        if self._array_type == ArrayType.PHASE:
            return

        if self._image is not None:
            self._image.set_cmap(cmap)

        if self._bar is not None:
            colors = cmap(self._bar_norm_x)
            for index, item in enumerate(self._bar):
                item.set_color(colors[index])

        self._redraw()

    def set_map_zoom(self, xs, ys):
        if self._map_axes is not None:
            self._map_xlim = xs
            self._map_ylim = ys

            self._map_axes.set_xlim(xs)
            self._map_axes.set_ylim(ys)
            self._redraw()

    def set_mode_type(self, mode_type):
        if mode_type != self._mode_type:
            self._mode_type = mode_type

            if self._mode_handler:
                self._mode_handler.clear()

            if mode_type == ModeType.ZOOM:
                self._mode_handler = ZoomHandler(self)
            elif mode_type == ModeType.REGION_RECTANGLE:
                self._mode_handler = RectangleRegionHandler(self)
            elif mode_type == ModeType.REGION_ELLIPSE:
                self._mode_handler = EllipseRegionHandler(self)
            elif mode_type == ModeType.REGION_POLYGON:
                self._mode_handler = PolygonRegionHandler(self)
            else:
                self._mode_handler = None

    def update(self, plot_type, array_type, array, array_stats, title):
        # Derived quantities.
        show_colorbar = True
        cmap_int_max = None
        if array_type == ArrayType.CLUSTER:
            cmap_int_max = array_stats['max'] + 1
        elif array_type == ArrayType.PHASE:
            show_colorbar = False
            cmap_int_max = 2

        self._array_type = array_type
        self._cmap_int_max = cmap_int_max

        if self._mode_handler:
            self._mode_handler.clear(redraw=False)

        figure = self._canvas.figure
        figure.clear()

        map_axes = None
        histogram_axes = None
        if plot_type == PlotType.MAP:
            map_axes = figure.subplots()
        elif plot_type == PlotType.HISTOGRAM:
            histogram_axes = figure.subplots()
        elif plot_type == PlotType.BOTH:
            map_axes, histogram_axes = figure.subplots( \
                nrows=2, gridspec_kw={'height_ratios': (3,1)})
        else:
            raise RuntimeError('Invalid plot type')

        cmap = self.create_colormap()

        if cmap_int_max is None:
            show_stats = True
            norm = Normalize(array_stats['min'], array_stats['max'])
            cmap_ticks = None
        else:
            show_stats = False
            norm = Normalize(-0.5, cmap_int_max-0.5)
            cmap_ticks = np.arange(0, cmap_int_max)
            if cmap_int_max >= 15:
                cmap_ticks = cmap_ticks[::2]

        if map_axes is None:
            self._image = None
        else:
            self._image = map_axes.imshow(array, cmap=cmap, norm=norm)
            if show_colorbar:
                colorbar = figure.colorbar(self._image, ax=map_axes,
                                           ticks=cmap_ticks)
            if title is not None:
                map_axes.set_title(title + ' map')
            if self._map_xlim is not None:
                map_axes.set_xlim(self._map_xlim)
                map_axes.set_ylim(self._map_ylim)

        if histogram_axes is None:
            self._bar = None
            self._bar_norm_x = None
        else:
            if cmap_int_max is None:
                bins = 100
            else:
                bins = np.arange(0, cmap_int_max+1)-0.5
            hist, bin_edges = np.histogram(np.ma.compressed(array), bins=bins)
            width = bin_edges[1] - bin_edges[0]
            bin_centres = bin_edges[:-1] + 0.5*width
            self._bar_norm_x = norm(bin_centres)
            colors = cmap(self._bar_norm_x)
            self._bar = histogram_axes.bar(bin_centres, hist, width,
                                           color=colors)
            if cmap_ticks is not None:
                histogram_axes.set_xticks(cmap_ticks)

            if show_stats:
                mean = array_stats.get('mean')
                median = array_stats.get('median')
                std = array_stats.get('std')
                if mean is not None:
                    histogram_axes.axvline(mean, c='k', ls='-', label='mean')
                    if std is not None:
                        histogram_axes.axvline(mean-std, c='k', ls='-.',
                                               label='mean \u00b1 std')
                        histogram_axes.axvline(mean+std, c='k', ls='-.')
                if median is not None:
                    histogram_axes.axvline(median, c='k', ls='--',
                                           label='median')
                histogram_axes.legend()

            if map_axes is None and title is not None:
                histogram_axes.set_title(title + ' histogram')

        self._map_axes = map_axes
        self._adjust_layout()
        self._redraw()
