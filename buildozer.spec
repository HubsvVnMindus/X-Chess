[app]

# (str) Tiêu đề ứng dụng
title = X-Chess

# (str) Tên gói (Package name)
package.name = xchess

# (str) Tên miền (Domain)
package.domain = org.example

# (str) Đường dẫn đến mã nguồn
source.dir = .

# (list) Các thư viện Python cần thiết
requirements = python3,kivy,plyer,pyjnius,android

# (str) Hướng màn hình
orientation = all

# (str) Phiên bản OS tối thiểu
android.minapi = 21

# (str) Phiên bản SDK dùng để biên dịch
android.api = 30

# (str) Phiên bản NDK
android.ndk = 23b

# (list) Cấp quyền cho ứng dụng
android.permissions = INTERNET

# (bool) Cho phép gỡ lỗi (debug)
android.debug = 1
