.class public Lcom/obfutils/EmuDetect;
.super Ljava/lang/Object;

.method static constructor <clinit>()V
    .registers 1

    const-string v0, "anti_emulator"

    invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V

    return-void
.end method

.method public static native isEmulator()Z
.end method
