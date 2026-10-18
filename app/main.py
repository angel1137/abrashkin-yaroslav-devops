import os
from http.server import BaseHTTPRequestHandler, HTTPServer

def student_info():
    return (
        "================================\n"
        "DevOps Student Application\n"
        "================================\n"
        f"Name: {os.getenv('STUDENT_NAME', 'Yaroslav')}\n"
        f"Surname: {os.getenv('STUDENT_SURNAME', 'Abrashkin')}\n"
        f"Group: {os.getenv('STUDENT_GROUP', 'IT2-2304')}\n"
        f"Student ID: {os.getenv('STUDENT_ID', '37035')}\n"
        "Application is running successfully!\n"
    )

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = student_info().encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(data)

if __name__ == "__main__":
    print(student_info(), flush=True)
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
