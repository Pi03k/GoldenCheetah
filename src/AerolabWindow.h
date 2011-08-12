/*
 * Copyright (c) 2009 Andy M. Froncioni (me@andyfroncioni.com)
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the Free
 * Software Foundation; either version 2 of the License, or (at your option)
 * any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
 * more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, write to the Free Software Foundation, Inc., 51
 * Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 */

#ifndef _GC_AerolabWindow_h
#define _GC_AerolabWindow_h 1
#include "GoldenCheetah.h"

#include <QtGui>

class Aerolab;
class MainWindow;
class QCheckBox;
class QwtPlotZoomer;
class QwtPlotPicker;
class QLineEdit;
class QLCDNumber;
class RideItem;
class IntervalItem;

class AerolabWindow : public GcWindow {
  Q_OBJECT
  G_OBJECT


  public:
  AerolabWindow(MainWindow *mainWindow);
  void setData(RideItem *ride);
  void zoomInterval(IntervalItem *); // zoom into a specified interval
  double getCanvasTop() const;
  double getCanvasBottom() const;

  QSlider *eoffsetSlider;

  public slots:
  void setCrrFromSlider();
  void setCdaFromSlider();
  void setCdaFromText(const QString text);
  void setTotalMassFromSlider();
  void setRhoFromSlider();
  void setEtaFromSlider();
  void setEoffsetFromSlider();
  void setAutoEoffset(int value);
  void setByDistance(int value);
  void rideSelected();
  void zoomChanged();
  void configChanged();
  void intervalSelected();

  protected slots:

  protected:
  MainWindow  *mainWindow;
  Aerolab *aerolab;
  QwtPlotZoomer *allZoomer;

  // Bike parameter controls:
  QSlider *crrSlider;
  QLineEdit *crrLineEdit;
  QLCDNumber *crrQLCDNumber;
  QSlider *cdaSlider;
  QLineEdit *cdaLineEdit;
  QLCDNumber *cdaQLCDNumber;
  QSlider *mSlider;
  QLineEdit *mLineEdit;
  QLCDNumber *mQLCDNumber;
  QSlider *rhoSlider;
  QLineEdit *rhoLineEdit;
  QLCDNumber *rhoQLCDNumber;
  QSlider *etaSlider;
  QLineEdit *etaLineEdit;
  QLCDNumber *etaQLCDNumber;

  QLineEdit *eoffsetLineEdit;
  QLCDNumber *eoffsetQLCDNumber;

};

#endif // _GC_AerolabWindow_h
