#! /usr/bin/env python
# encoding: utf-8


from platform import system
from waflib import Logs


# usage
# CXX='ccache g++' python3 ./waf-2.0.18 configure build -pv -j 20

APPNAME = 'GoldenCheetah'


TOP = '.'
OUT = 'build'


def options(opt):
    opt.load('compiler_cxx compiler_c qt5')


def configure(conf):
    conf.load('compiler_cxx compiler_c qt5')
    conf.load('clang_compilation_database')
    conf.check_cfg(package='python3', args='--libs --cflags', uselib_store='PYTHON')
    conf.check_cfg(package='libusb', args='--libs --cflags', uselib_store='LIBUSB')
    conf.check_cfg(package='libzip', args='--libs --cflags', uselib_store='LIBZIP')


# qzip/zip.cpp
# src/Python/PythonEmbed.cpp
# src/Python/PythonSyntax.cpp
# src/Python/SIP/Bindings.cpp
# src/Python/SIP/sipgoldencheetahBindings.cpp
# src/Python/SIP/sipgoldencheetahPythonDataSeries.cpp
# src/Python/SIP/sipgoldencheetahQString.cpp
# src/Python/SIP/sipgoldencheetahcmodule.cpp
# src/Charts/RideWindow.cpp

SOURCES = """
src/ANT/ANT.cpp
src/ANT/ANTChannel.cpp
src/ANT/ANTLogger.cpp
src/ANT/ANTMessage.cpp
src/ANT/ANTlocalController.cpp
src/Charts/Aerolab.cpp
src/Charts/AerolabWindow.cpp
src/Charts/AllPlot.cpp
src/Charts/AllPlotInterval.cpp
src/Charts/AllPlotSlopeCurve.cpp
src/Charts/AllPlotWindow.cpp
src/Charts/BlankState.cpp
src/Charts/CPPlot.cpp
src/Charts/ChartBar.cpp
src/Charts/ChartSettings.cpp
src/Charts/CpPlotCurve.cpp
src/Charts/CriticalPowerWindow.cpp
src/Charts/DiaryWindow.cpp
src/Charts/ExhaustionDialog.cpp
src/Charts/GcOverlayWidget.cpp
src/Charts/GcPane.cpp
src/Charts/GoldenCheetah.cpp
src/Charts/HistogramWindow.cpp
src/Charts/HomeWindow.cpp
src/Charts/HrPwPlot.cpp
src/Charts/HrPwWindow.cpp
src/Charts/IndendPlotMarker.cpp
src/Charts/IntervalSummaryWindow.cpp
src/Charts/LTMCanvasPicker.cpp
src/Charts/LTMChartParser.cpp
src/Charts/LTMOutliers.cpp
src/Charts/LTMPlot.cpp
src/Charts/LTMPopup.cpp
src/Charts/LTMSettings.cpp
src/Charts/LTMTool.cpp
src/Charts/LTMTrend.cpp
src/Charts/LTMWindow.cpp
src/Charts/LogTimeScaleDraw.cpp
src/Charts/MUPlot.cpp
src/Charts/MUWidget.cpp
src/Charts/MetadataWindow.cpp
src/Charts/OverviewWindow.cpp
src/Charts/PfPvPlot.cpp
src/Charts/PfPvWindow.cpp
src/Charts/PowerHist.cpp
src/Charts/PythonChart.cpp
src/Charts/RCanvas.cpp
src/Charts/RChart.cpp
src/Charts/ReferenceLineDialog.cpp
src/Charts/RideEditor.cpp
src/Charts/RideMapWindow.cpp
src/Charts/RideSummaryWindow.cpp
src/Charts/ScatterPlot.cpp
src/Charts/ScatterWindow.cpp
src/Charts/SmallPlot.cpp
src/Charts/SummaryWindow.cpp
src/Charts/TreeMapPlot.cpp
src/Charts/TreeMapWindow.cpp
src/Cloud/AddCloudWizard.cpp
src/Cloud/BodyMeasuresDownload.cpp
src/Cloud/CalDAV.cpp
src/Cloud/CalDAVCloud.cpp
src/Cloud/CalendarDownload.cpp
src/Cloud/CloudDBChart.cpp
src/Cloud/CloudDBCommon.cpp
src/Cloud/CloudDBCurator.cpp
src/Cloud/CloudDBStatus.cpp
src/Cloud/CloudDBTelemetry.cpp
src/Cloud/CloudDBVersion.cpp
src/Cloud/CloudService.cpp
src/Cloud/CyclingAnalytics.cpp
src/Cloud/Dropbox.cpp
src/Cloud/GoogleDrive.cpp
src/Cloud/HrvMeasuresDownload.cpp
src/Cloud/KentUniversity.cpp
src/Cloud/LocalFileStore.cpp
src/Cloud/OAuthDialog.cpp
src/Cloud/OpenData.cpp
src/Cloud/PolarFlow.cpp
src/Cloud/RideWithGPS.cpp
src/Cloud/Selfloops.cpp
src/Cloud/SixCycle.cpp
src/Cloud/SportTracks.cpp
src/Cloud/SportsPlusHealth.cpp
src/Cloud/Strava.cpp
src/Cloud/TodaysPlan.cpp
src/Cloud/TodaysPlanBodyMeasures.cpp
src/Cloud/TrainingsTageBuch.cpp
src/Cloud/Velohero.cpp
src/Cloud/Withings.cpp
src/Cloud/WithingsDownload.cpp
src/Cloud/Xert.cpp
src/Core/Athlete.cpp
src/Core/BlinnSolver.cpp
src/Core/BodyMeasures.cpp
src/Core/Context.cpp
src/Core/DataFilter.cpp
src/Core/FreeSearch.cpp
src/Core/GcUpgrade.cpp
src/Core/HrvMeasures.cpp
src/Core/ICalendar.cpp
src/Core/IdleTimer.cpp
src/Core/IntervalItem.cpp
src/Core/Measures.cpp
src/Core/NamedSearch.cpp
src/Core/RideCache.cpp
src/Core/RideCacheModel.cpp
src/Core/RideItem.cpp
src/Core/Route.cpp
src/Core/RouteParser.cpp
src/Core/Season.cpp
src/Core/SeasonParser.cpp
src/Core/Settings.cpp
src/Core/Specification.cpp
src/Core/TimeUtils.cpp
src/Core/Units.cpp
src/Core/UserData.cpp
src/Core/Utils.cpp
src/Core/main.cpp
src/FileIO/ArchiveFile.cpp
src/FileIO/AthleteBackup.cpp
src/FileIO/Bin2RideFile.cpp
src/FileIO/BinRideFile.cpp
src/FileIO/BodyMeasuresCsvImport.cpp
src/FileIO/CommPort.cpp
src/FileIO/Computrainer3dpFile.cpp
src/FileIO/CsvRideFile.cpp
src/FileIO/DataProcessor.cpp
src/FileIO/Device.cpp
src/FileIO/FilterHRV.cpp
src/FileIO/FitRideFile.cpp
src/FileIO/FitlogParser.cpp
src/FileIO/FitlogRideFile.cpp
src/FileIO/FixAeroPod.cpp
src/FileIO/FixDeriveDistance.cpp
src/FileIO/FixDeriveHeadwind.cpp
src/FileIO/FixDerivePower.cpp
src/FileIO/FixDeriveTorque.cpp
src/FileIO/FixElevation.cpp
src/FileIO/FixFreewheeling.cpp
src/FileIO/FixGPS.cpp
src/FileIO/FixGaps.cpp
src/FileIO/FixHRSpikes.cpp
src/FileIO/FixLapSwim.cpp
src/FileIO/FixMoxy.cpp
src/FileIO/FixPower.cpp
src/FileIO/FixRunningCadence.cpp
src/FileIO/FixRunningPower.cpp
src/FileIO/FixSmO2.cpp
src/FileIO/FixSpeed.cpp
src/FileIO/FixSpikes.cpp
src/FileIO/FixTorque.cpp
src/FileIO/GcRideFile.cpp
src/FileIO/GpxParser.cpp
src/FileIO/GpxRideFile.cpp
src/FileIO/HrvMeasuresCsvImport.cpp
src/FileIO/JouleDevice.cpp
src/FileIO/LapsEditor.cpp
src/FileIO/LocationInterpolation.cpp
src/FileIO/MacroDevice.cpp
src/FileIO/ManualRideFile.cpp
src/FileIO/MoxyDevice.cpp
src/FileIO/PolarRideFile.cpp
src/FileIO/PowerTapDevice.cpp
src/FileIO/PowerTapUtil.cpp
src/FileIO/PwxRideFile.cpp
src/FileIO/QuarqParser.cpp
src/FileIO/QuarqRideFile.cpp
src/FileIO/RawRideFile.cpp
src/FileIO/RideAutoImportConfig.cpp
src/FileIO/RideFile.cpp
src/FileIO/RideFileCache.cpp
src/FileIO/RideFileCommand.cpp
src/FileIO/RideFileTableModel.cpp
src/FileIO/Serial.cpp
src/FileIO/SlfParser.cpp
src/FileIO/SlfRideFile.cpp
src/FileIO/SmfParser.cpp
src/FileIO/SmfRideFile.cpp
src/FileIO/SmlParser.cpp
src/FileIO/SmlRideFile.cpp
src/FileIO/Snippets.cpp
src/FileIO/SrdRideFile.cpp
src/FileIO/SrmRideFile.cpp
src/FileIO/SyncRideFile.cpp
src/FileIO/TacxCafRideFile.cpp
src/FileIO/TcxParser.cpp
src/FileIO/TcxRideFile.cpp
src/FileIO/TxtRideFile.cpp
src/FileIO/WkoRideFile.cpp
src/FileIO/XDataDialog.cpp
src/FileIO/XDataTableModel.cpp
src/Gui/AboutDialog.cpp
src/Gui/AddIntervalDialog.cpp
src/Gui/AnalysisSidebar.cpp
src/Gui/BatchExportDialog.cpp
src/Gui/ChooseCyclistDialog.cpp
src/Gui/ColorButton.cpp
src/Gui/Colors.cpp
src/Gui/CompareDateRange.cpp
src/Gui/CompareInterval.cpp
src/Gui/ComparePane.cpp
src/Gui/ConfigDialog.cpp
src/Gui/DiarySidebar.cpp
src/Gui/DownloadRideDialog.cpp
src/Gui/DragBar.cpp
src/Gui/EditUserMetricDialog.cpp
src/Gui/EstimateCPDialog.cpp
src/Gui/GProgressDialog.cpp
src/Gui/GcCrashDialog.cpp
src/Gui/GcScopeBar.cpp
src/Gui/GcSideBarItem.cpp
src/Gui/GcToolBar.cpp
src/Gui/GcWindowLayout.cpp
src/Gui/GcWindowRegistry.cpp
src/Gui/GenerateHeatMapDialog.cpp
src/Gui/HelpWhatsThis.cpp
src/Gui/HelpWindow.cpp
src/Gui/IntervalTreeView.cpp
src/Gui/LTMSidebar.cpp
src/Gui/MainWindow.cpp
src/Gui/ManualRideDialog.cpp
src/Gui/MergeActivityWizard.cpp
src/Gui/NewCyclistDialog.cpp
src/Gui/Pages.cpp
src/Gui/RideImportWizard.cpp
src/Gui/RideNavigator.cpp
src/Gui/SaveDialogs.cpp
src/Gui/SearchBox.cpp
src/Gui/SearchFilterBox.cpp
src/Gui/SolveCPDialog.cpp
src/Gui/SolverDisplay.cpp
src/Gui/SplitActivityWizard.cpp
src/Gui/Tab.cpp
src/Gui/TabView.cpp
src/Gui/ToolsRhoEstimator.cpp
src/Gui/Views.cpp
src/Metrics/AerobicDecoupling.cpp
src/Metrics/Banister.cpp
src/Metrics/BasicRideMetrics.cpp
src/Metrics/BikeScore.cpp
src/Metrics/CPSolver.cpp
src/Metrics/Coggan.cpp
src/Metrics/DanielsPoints.cpp
src/Metrics/Estimator.cpp
src/Metrics/ExtendedCriticalPower.cpp
src/Metrics/GOVSS.cpp
src/Metrics/HrTimeInZone.cpp
src/Metrics/HrZones.cpp
src/Metrics/HrvMetrics.cpp
src/Metrics/LeftRightBalance.cpp
src/Metrics/PDModel.cpp
src/Metrics/PMCData.cpp
src/Metrics/PaceTimeInZone.cpp
src/Metrics/PaceZones.cpp
src/Metrics/PeakHr.cpp
src/Metrics/PeakPace.cpp
src/Metrics/PeakPower.cpp
src/Metrics/PowerProfile.cpp
src/Metrics/RideMetadata.cpp
src/Metrics/RideMetric.cpp
src/Metrics/RunMetrics.cpp
src/Metrics/SpecialFields.cpp
src/Metrics/Statistic.cpp
src/Metrics/SustainMetric.cpp
src/Metrics/SwimMetrics.cpp
src/Metrics/SwimScore.cpp
src/Metrics/TRIMPPoints.cpp
src/Metrics/TimeInZone.cpp
src/Metrics/UserMetric.cpp
src/Metrics/UserMetricParser.cpp
src/Metrics/VDOT.cpp
src/Metrics/VDOTCalculator.cpp
src/Metrics/WPrime.cpp
src/Metrics/WattsPerKilogram.cpp
src/Metrics/Zones.cpp
src/Metrics/aBikeScore.cpp
src/Metrics/aCoggan.cpp
src/Planning/PlanningWindow.cpp
src/R/REmbed.cpp
src/R/RGraphicsDevice.cpp
src/R/RLibrary.cpp
src/R/RSyntax.cpp
src/R/RTool.cpp
src/Train/EzUsb.c
src/Train/AddDeviceWizard.cpp
src/Train/BT40Controller.cpp
src/Train/BT40Device.cpp
src/Train/CalibrationData.cpp
src/Train/Computrainer.cpp
src/Train/ComputrainerController.cpp
src/Train/Daum.cpp
src/Train/DaumController.cpp
src/Train/DeviceConfiguration.cpp
src/Train/DeviceTypes.cpp
src/Train/DialWindow.cpp
src/Train/ErgDB.cpp
src/Train/ErgDBDownloadDialog.cpp
src/Train/ErgFile.cpp
src/Train/ErgFilePlot.cpp
src/Train/Fortius.cpp
src/Train/FortiusController.cpp
src/Train/GarminServiceHelper.cpp
src/Train/Imagic.cpp
src/Train/ImagicController.cpp
src/Train/Kettler.cpp
src/Train/KettlerConnection.cpp
src/Train/KettlerController.cpp
src/Train/KettlerRacer.cpp
src/Train/KettlerRacerConnection.cpp
src/Train/KettlerRacerController.cpp
src/Train/LibUsb.cpp
src/Train/Library.cpp
src/Train/LibraryParser.cpp
src/Train/MeterWidget.cpp
src/Train/MonarkConnection.cpp
src/Train/MonarkController.cpp
src/Train/NullController.cpp
src/Train/PhysicsUtility.cpp
src/Train/RealtimeController.cpp
src/Train/RealtimeData.cpp
src/Train/RealtimePlot.cpp
src/Train/RealtimePlotWindow.cpp
src/Train/RemoteControl.cpp
src/Train/SpinScanPlot.cpp
src/Train/SpinScanPlotWindow.cpp
src/Train/SpinScanPolarPlot.cpp
src/Train/TodaysPlanWorkoutDownload.cpp
src/Train/TrainBottom.cpp
src/Train/TrainDB.cpp
src/Train/TrainSidebar.cpp
src/Train/VideoLayoutParser.cpp
src/Train/VideoSyncFile.cpp
src/Train/VideoWindow.cpp
src/Train/WebPageWindow.cpp
src/Train/WorkoutPlotWindow.cpp
src/Train/WorkoutWidget.cpp
src/Train/WorkoutWidgetItems.cpp
src/Train/WorkoutWindow.cpp
src/Train/WorkoutWizard.cpp
src/Train/ZwoParser.cpp
levmar/Axb.c
levmar/lmlec.c levmar/misc.c
levmar/lm.c levmar/lmbc.c levmar/lmblec.c levmar/lmbleic.c
lmfit/lmcurve.c
lmfit/lmmin.c
qtsolutions/codeeditor/codeeditor.cpp
qtsolutions/json/mvjson.cpp
qtsolutions/qwtcurve/qwt_plot_gapped_curve.cpp
qtsolutions/segmentcontrol/qtsegmentcontrol.cpp
qxt/src/qxtspanslider.cpp
qxt/src/qxtstringspinbox.cpp
qzip/zip.cpp
"""


DEFINES = [
    'NOWEBKIT',
    '_REENTRANT',
    'GC_VIDEO_VLC',
    'GC_DROPBOX_CLIENT_ID=\"9jrhrk7vxnq3o34\"',
    'GC_DROPBOX_CLIENT_SECRET=\"ez5nwdyp39fjqwb\"',
    'GC_WANT_ALLDEBUG',
    'GC_DEBUG',
    'DEBUG',
    'STRAVA_DEBUG',
    'QXT_STATIC',
    'GC_HAVE_SRMIO',
    'GC_HAVE_ICAL',
    'GC_HAVE_LIBUSB',
    'GC_HAVE_VLC',
    'GC_HAVE_SAMPLERATE',
    'GC_HAVE_OVERVIEW',
]


CXXFLAGS = [
    '-Wall',
    '-Wextra',
    '-O3',
    '-ggdb3',
    '-fPIC',
    '-L ./qwt/lib/'
]


INCLUDE_DIRS = [
    '.',
    './src/',
    './src/ANT/',
    './src/Core/',
    './src/Charts',
    './src/Cloud',
    './src/FileIO/',
    './src/Gui/',
    './src/Metrics',
    './src/Python',
    './src/Planning',
    './src/R',
    './src/Train',
    '../qwt/src/',
    '../qxt/src/',
    '../qtsolutions/json',
    '../qtsolutions/qwtcurve',
    '../lmfit',
    '../levmar',
    '/usr/lib/qt/mkspecs/linux-g++/include/',
    '/usr/include/R/',
]


PACKAGES = [
    'QT5BLUETOOTH',
    'QT5CONCURRENT',
    'QT5CORE',
    'QT5CHARTS',
    'QT5GUI',
    'QT5MULTIMEDIA',
    'QT5NETWORK',
    'QT5OPENGL',
    'QT5SERIALPORT',
    'QT5SQL',
    'QT5SVG',
    'QT5WEBENGINE',
    'QT5WEBENGINEWIDGETS',
    'QT5WIDGETS',
    'QT5XML',
    'PYTHON',
    'LIBUSB',
    'LIBZIP',
]


DEFERRES = [
    'src/Core/RouteWindow.h',
    'src/Core/RouteWindow.cpp',
    'src/Core/RouteItem.h',
    'src/Core/RouteItem.cpp',
    'src/Gui/QtMacVideoWindow.h'
]


def build(bld):
    headers = bld.path.ant_glob('src/**/*.h') + bld.path.ant_glob('qtsolutions/**/*.h') \
            + bld.path.ant_glob('levmar/**/*.h') \
            + ['qxt/src/qxtspanslider.h', 'qxt/src/qxtspanslider_p.h', \
             'qxt/src/qxtstringspinbox.h',  'qzip/zipreader.h']
    bld.logger = Logs.make_logger('build.log', '')
    bld(
        features='qt5 cxx cxxprogram',
        uselib=PACKAGES,
        source=SOURCES,
        includes=' '.join(INCLUDE_DIRS),
        lang=bld.path.ant_glob('linguist/*.ts'),
        cppflags=' '.join(CXXFLAGS),
        defines=DEFINES,
        lib=['m', 'z', 'qwt'],
        moc=list(set(headers) - set(DEFERRES)),
        target=APPNAME,
    )
    # Logs.free_logger(bld.logger)
    bld.logger = None
