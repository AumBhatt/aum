SYSROOT_DIR=
MISC_DIR=${SYSROOT_DIR}/usr/local/misc

INCLUDES = -I$(MISC_DIR)/include \
	   -I$(SYSROOT_DIR)/usr/include/arm-linux-gnueabihf \

LIB_DIRS = -L$(MISC_DIR)/lib \
        -L$(SYSROOT_DIR)/usr/lib/arm-linux-gnueabihf \
        -L$(SYSROOT_DIR)/opt/vc/lib -L$(SYSROOT_DIR)/usr/local/lib

#LFLAGS = \
#        -Wl,-rpath-link,$(SYSROOT_DIR)/opt/vc/lib \
#        -Wl,-rpath-link,$(SYSROOT_DIR)/usr/lib/arm-linux-gnueabihf \
#        -Wl,-rpath-link,$(SYSROOT_DIR)/lib/arm-linux-gnueabihf

LIBS = \
	-Wl,--start-group \
        -lpthread \
	-lboost_system \
	-Wl,--end-group


all:
	g++ $(INCLUDES) ${LIB_DIRS} ${LFLAGS} $(LIBS) -o i1 i1.cpp 
