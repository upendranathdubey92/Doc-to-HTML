#!/usr/bin/env python3
import http.server
import socketserver
import socket
import os

def start_server():
    PORT = 8081
    
    # Use current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    
    # Get local IP address
    hostname = socket.gethostname()
    try:
        local_ip = socket.gethostbyname(hostname)
        # Try to get the actual network IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except:
        local_ip = "127.0.0.1"
    
    class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            super().end_headers()
    
    Handler = MyHTTPRequestHandler
    
    try:
        # Bind to all interfaces (0.0.0.0)
        with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
            print(f"Page Content Update IDE Server Started!")
            print(f"Serving from: {os.getcwd()}")
            print(f"Local access: http://localhost:{PORT}")
            print(f"Network access: http://{local_ip}:{PORT}")
            print(f"")
            print(f"DIRECT LINKS:")
            print(f"   Main Page: http://localhost:{PORT}/index.html")
            print(f"   Web IDE: http://localhost:{PORT}/web_ide_final.html")
            print(f"   Sample Doc: http://localhost:{PORT}/Content_File_Web_Development_Consulting_FINAL.txt")
            print(f"")
            print(f"Press Ctrl+C to stop")
            print("=" * 70)
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\nServer stopped!")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"Port {PORT} is already in use.")
            print("Try running: netstat -ano | findstr :8080")
            print("Then kill the process or use a different port")
        else:
            print(f"Error starting server: {e}")

if __name__ == "__main__":
    start_server()