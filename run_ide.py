#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os
import time
import threading

# Change to correct directory
os.chdir('/home/sotsys-252/Desktop/page-content-update')

# Kill any existing servers
os.system('pkill -f "python.*http.server" 2>/dev/null')
time.sleep(1)

PORT = 8080

print("🚀 Starting Page Content Update IDE...")
print(f"📁 Directory: {os.getcwd()}")
print(f"📋 Files available:")
for f in ['web_ide_v2.html', 'web_ide.html', 'test_content.txt']:
    if os.path.exists(f):
        print(f"   ✅ {f}")
    else:
        print(f"   ❌ {f}")

print(f"\n🌐 Starting server on port {PORT}...")

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"📡 {format % args}")

try:
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"✅ Server running at: http://localhost:{PORT}")
        print(f"🎯 Access IDE at: http://localhost:{PORT}/web_ide_v2.html")
        print(f"📋 Or try: http://localhost:{PORT}/web_ide.html")
        print(f"\n📋 Press Ctrl+C to stop the server")
        print("="*60)
        
        def open_browser():
            time.sleep(2)
            try:
                webbrowser.open(f'http://localhost:{PORT}/web_ide_v2.html')
            except:
                pass
        
        threading.Thread(target=open_browser, daemon=True).start()
        httpd.serve_forever()
        
except KeyboardInterrupt:
    print("\n🛑 Server stopped")
except Exception as e:
    print(f"❌ Error: {e}")
    print(f"💡 Try manually: python3 -m http.server {PORT}")