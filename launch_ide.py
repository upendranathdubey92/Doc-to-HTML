#!/usr/bin/env python3
"""
Simple web server to launch the Page Content Update IDE
"""

import http.server
import socketserver
import webbrowser
import os
import sys

def launch_ide():
    """Launch the web-based IDE"""
    PORT = 8000
    
    # Change to the directory containing the IDE
    ide_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(ide_dir)
    
    # Create server
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"🚀 Page Content Update IDE")
            print(f"📡 Server running at: http://localhost:{PORT}")
            print(f"🌐 Opening IDE at: http://localhost:{PORT}/web_ide.html")
            print(f"")
            print(f"✨ Features:")
            print(f"   • Drag & drop document files")
            print(f"   • Real-time HTML generation")
            print(f"   • Copy & download generated code")
            print(f"   • Support for 6 section types")
            print(f"")
            print(f"📋 Press Ctrl+C to stop the server")
            print(f"{'='*50}")
            
            # Try to open browser automatically
            try:
                webbrowser.open(f'http://localhost:{PORT}/web_ide.html')
            except:
                pass
                
            # Serve forever
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print(f"\n🛑 Server stopped")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {PORT} is already in use")
            print(f"💡 Try opening: http://localhost:{PORT}/web_ide.html")
        else:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    launch_ide()