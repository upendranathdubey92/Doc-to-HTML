#!/usr/bin/env python3
"""
Simple launcher for the Page Content Update IDE
"""

import http.server
import socketserver
import webbrowser
import os
import time
import threading

def start_server():
    """Start the web server"""
    PORT = 8080
    
    # Change to the project directory
    os.chdir('/home/sotsys-252/Desktop/page-content-update')
    
    # Create server
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"🚀 Page Content Update IDE started!")
            print(f"📡 Server running at: http://localhost:{PORT}")
            print(f"🌐 Opening IDE at: http://localhost:{PORT}/web_ide_final.html")
            print(f"⚡ Press Ctrl+C to stop the server")
            print("="*60)
            
            # Open browser after a short delay
            def open_browser():
                time.sleep(2)
                webbrowser.open(f'http://localhost:{PORT}/web_ide_final.html')
            
            threading.Thread(target=open_browser, daemon=True).start()
            
            # Start server
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Server stopped!")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {PORT} is already in use.")
            print("Try stopping other servers or wait a moment.")
        else:
            print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    start_server()