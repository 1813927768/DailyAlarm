from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import os
import sys
from urllib.parse import urlparse
import json

mimedic = [
    (".html", "text/html"),
    (".htm", "text/html"),
    (".js", "application/javascript"),
    (".css", "text/css"),
    (".json", "application/json"),
    (".png", "image/png"),
    (".jpg", "image/jpeg"),
    (".gif", "image/gif"),
    (".txt", "text/plain"),
    (".avi", "video/x-msvideo"),
]

repo_path = "/root/repos/DailyAlarm/web"


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        send_reply = False
        query_path = urlparse(self.path)
        file_path, query = query_path.path, query_path.query
        if file_path.endswith("/"):
            file_path += "index.html"
        file_name, file_ext = os.path.splitext(file_path)
        for e in mimedic:
            if e[0] == file_ext:
                mime_type = e[1]
                send_reply = True
                break

        if send_reply:
            try:
                with open("%s/%s" % (repo_path, file_path), "rb") as f:
                    content = f.read()
                    self.send_response(200)
                    self.send_header("Content-type", mime_type)
                    self.end_headers()
                    self.wfile.write(content)
            except IOError:
                self.send_error(404, "File Not Found: %s" % self.path)

    def do_POST(self):
        try:
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            for pairs in str(body)[1:].strip("'").split("&"):
                key, val = pairs.split("=")
                config_json = json.load(open("%s/config.json" % (repo_path), "r"))
                config_json[key] = val
                json.dump(config_json, open("%s/config.json" % (repo_path), "w"))

        except OSError as e:
            print(e)
        finally:
            self.send_response(200)
            self.end_headers()
            response = BytesIO()
            response.write(b"This is POST request. ")
            response.write(b"Received: ")
            response.write(body)
            self.wfile.write(response.getvalue())


httpd = HTTPServer(("", 8081), SimpleHTTPRequestHandler)
httpd.serve_forever()