LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE    := anti_emulator
LOCAL_SRC_FILES := anti_emulator.c

# ✅ This line is critical to fix your linker issue
LOCAL_LDLIBS    := -llog

include $(BUILD_SHARED_LIBRARY)
