#include <jni.h>
#include <string.h>
#include <android/log.h>

#define LOG_TAG "ANTI_EMULATOR"
#define LOGI(...)  __android_log_print(ANDROID_LOG_INFO, LOG_TAG, __VA_ARGS__)

JNIEXPORT jboolean JNICALL
Java_com_obfutils_EmuDetect_isEmulator(JNIEnv *env, jclass clazz) {
    jclass buildClass = (*env)->FindClass(env, "android/os/Build");
    jfieldID productField = (*env)->GetStaticFieldID(env, buildClass, "PRODUCT", "Ljava/lang/String;");
    jstring productString = (jstring)(*env)->GetStaticObjectField(env, buildClass, productField);
    
    const char *product = (*env)->GetStringUTFChars(env, productString, NULL);

    LOGI("Product: %s", product);

    if (strstr(product, "sdk") || strstr(product, "emulator") || strstr(product, "genymotion") || strstr(product, "nox")) {
        (*env)->ReleaseStringUTFChars(env, productString, product);
        return JNI_TRUE;
    }

    (*env)->ReleaseStringUTFChars(env, productString, product);
    return JNI_FALSE;
}
