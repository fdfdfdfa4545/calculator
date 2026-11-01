[app]
title = MyCalculator
package.name = mycalculator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Важные строки для GitHub Actions:
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.api = 33
android.minapi = 21
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
