ABIs = [
    ABI("2", "armeabi-v7a", None, 26, cmake_vars=dict(ANDROID_SDK_TARGET=30, ANDROID_ABI='armeabi-v7a with NEON', OPENCV_ENABLE_NONFREE='ON', BUILD_TESTS='OFF', INSTALL_TESTS='OFF', BUILD_ANDROID_EXAMPLES='OFF', INSTALL_ANDROID_EXAMPLES='OFF')),
    ABI("3", "arm64-v8a",   None, 26, cmake_vars=dict(ANDROID_SDK_TARGET=30, OPENCV_ENABLE_NONFREE='ON', BUILD_TESTS='OFF', INSTALL_TESTS='OFF', BUILD_ANDROID_EXAMPLES='OFF', INSTALL_ANDROID_EXAMPLES='OFF')),
    ABI("5", "x86_64",      None, 26, cmake_vars=dict(ANDROID_SDK_TARGET=30, OPENCV_ENABLE_NONFREE='ON', BUILD_TESTS='OFF', INSTALL_TESTS='OFF', BUILD_ANDROID_EXAMPLES='OFF', INSTALL_ANDROID_EXAMPLES='OFF')),
    ABI("4", "x86",         None, 26, cmake_vars=dict(ANDROID_SDK_TARGET=30, OPENCV_ENABLE_NONFREE='ON', BUILD_TESTS='OFF', INSTALL_TESTS='OFF', BUILD_ANDROID_EXAMPLES='OFF', INSTALL_ANDROID_EXAMPLES='OFF')),
]
