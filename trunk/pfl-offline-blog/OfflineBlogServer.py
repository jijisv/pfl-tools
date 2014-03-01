'''
OfflineBlogServer

Created on Oct 12, 2012
@author: Jiji_Sasidharan
'''

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import sys
import urllib

class OfflineBlogRequestHandler(SimpleHTTPRequestHandler):
    
    def do_GET(self):
        pr = urllib.parse.urlparse(self.path)
        if pr.path == '/v':
            params = urllib.parse.parse_qs(pr.query)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.getPost(pr.path, params['p'][0]).encode())
            self.wfile.flush()
        else:
            SimpleHTTPRequestHandler.do_GET(self)
    
    def getPost(self, path, post_name):
        template = open(os.path.join(os.getcwd(), 'index.htm'), 'r').read()

        post_title = post_name
        try:
            post = open(os.path.join(os.getcwd(), 'drafts', post_name + '.html'), 'r').read().strip()
    
            start = post.find('<title>')
            if (start == 0):
                end = post.find('</title>')
                post_title = post[(start+7):end]
        except:
            post = "<p style=\"text-align: center;margin: 3em;\">The post <b>%s.html</b>" + \
                "not found in drafts.</p>" % (post_name)

        return template.replace('$BLOG_ENTRY_BODY$', post).replace('$BLOG_ENTRY_TITLE$', post_title)

if __name__ == '__main__':
    httpd = HTTPServer(('', int(sys.argv[1])), OfflineBlogRequestHandler)
    try:
        print("Serving HTTP on", httpd.server_address , "port", httpd.server_port, "...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        sys.exit()
        
