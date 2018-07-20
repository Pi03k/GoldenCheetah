TEMPLATE = subdirs
SUBDIRS = qwt
SUBDIRS += src
CONFIG += ordered debug
QMAKE_CXXFLAGS = -O0 -ggdb3 -Wall -Wextra -std=c++11
