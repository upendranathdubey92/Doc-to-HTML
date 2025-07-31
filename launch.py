#!/usr/bin/env python3
import os
import http.server
import socketserver
import webbrowser

# Change to the correct directory
os.chdir('/home/sotsys-252/Desktop/page-content-update')

PORT = 8080

print("🚀 Starting Page Content Update IDE...")
print("📁 Current directory:", os.getcwd())
print("📋 Available files:")
files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in files:
    print(f"   • {f}")

try:
    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"\n✅ Server started successfully!")
        print(f"🌐 Access URLs:")
        print(f"   • Main page: http://localhost:{PORT}")
        print(f"   • Web IDE: http://localhost:{PORT}/web_ide_final.html")
        print(f"   • Standalone: http://localhost:{PORT}/standalone_ide.html")
        print(f"\n🎯 RECOMMENDED: Use standalone_ide.html (works offline)")
        print(f"⚡ Press Ctrl+C to stop")
        print("=" * 60)
        
        httpd.serve_forever()
        
except OSError as e:
    print(f"❌ Error: {e}")
    if "Address already in use" in str(e):
        print(f"💡 Port {PORT} is busy. Try:")
        print(f"   sudo lsof -i :{PORT}")
        print(f"   kill <process_id>")
except KeyboardInterrupt:
    print("\n👋 Server stopped by user")