from http.server import BaseHTTPRequestHandler, HTTPServer
import json


def response(handler, status, payload):
    body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    handler.send_response(status)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(body)


class App(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            response(self, 200, {'status': 'ok', 'service': 'task-automation-api'})
            return
        response(self, 404, {'error': 'not found'})

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        data = json.loads(self.rfile.read(length) or b'{}')

        if self.path == '/plan/organize':
            files = data.get('files', [])
            plan = [{'file': name, 'action': 'classify'} for name in files]
            response(self, 200, {'total': len(plan), 'plan': plan})
            return

        if self.path == '/plan/rename':
            files = data.get('files', [])
            prefix = data.get('prefix', 'file')
            plan = [{'from': name, 'to': f'{prefix}_{i + 1}'} for i, name in enumerate(files)]
            response(self, 200, {'total': len(plan), 'plan': plan})
            return

        response(self, 404, {'error': 'not found'})


if __name__ == '__main__':
    HTTPServer(('localhost', 8000), App).serve_forever()
