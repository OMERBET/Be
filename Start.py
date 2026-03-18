import os
import subprocess

# 1. إعداد البيئة
print("📥 جاري تجهيز المحرك... يرجى الانتظار")
if not os.path.exists('/content/BitCrack'):
    os.chdir('/content')
    subprocess.run(['git', 'clone', 'https://github.com'])
    os.chdir('/content/BitCrack')
    subprocess.run(['make'])

# 2. التأكد من وجود ملف العناوين المرفوع
if os.path.exists('/content/my-repo/targets.txt'):
    subprocess.run(['cp', '/content/my-repo/targets.txt', '/content/BitCrack/targets.txt'])

# 3. تشغيل الهجوم
os.chdir('/content/BitCrack')
print("🚀 إطلاق الهجوم الكمي...")
subprocess.run(['./BitCrack', '-f', 'targets.txt', '-c', '-g', '128,256', '--keyspace', '1:ffffffffff'])
