from http.server import HTTPServer, CGIHTTPRequestHandler
port = 8081
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("服务已启动，端口：", port)
httpd.serve_forever()
