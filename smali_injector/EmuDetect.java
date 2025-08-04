package com.obfutils;

public class EmuDetect {

    static {
        System.loadLibrary("anti_emulator");
    }

    public static native boolean isEmulator();
}
