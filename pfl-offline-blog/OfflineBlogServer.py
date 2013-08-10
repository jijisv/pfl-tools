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
            self.createFile(pr.path, params['p'][0])
        SimpleHTTPRequestHandler.do_GET(self)
    
    def createFile(self, path, post_name):
        template = open(os.path.join(os.getcwd(), 'index.htm'), 'r').read()
        
        (post_title, post) = self.getPost(post_name)
        
#         post = open(os.path.join(os.getcwd(), 'drafts', post_name + '.html'), 'r').read().strip()
# 
#         start = post.find('<h1>')
#         if (start == 0):
#             end = post.find('</h1>')
#             post_title = post[:end]
#             post = post[end + 5:]
#         else :
#             post_title = post_name    

        f = open(os.path.join(os.getcwd(), 'v'), 'w')
        f.write(template.replace('$BLOG_ENTRY_BODY$', post).replace('$BLOG_ENTRY_TITLE$', post_title))
        f.close()

    def getPost(self, post_name):
        post_title = post_name
        try:
            post = open(os.path.join(os.getcwd(), 'drafts', post_name + '.html'), 'r').read().strip()
    
            start = post.find('<h1>')
            if (start == 0):
                end = post.find('</h1>')
                post_title = post[:end]
                post = post[end + 5:]
        except:
            post = "<center><br/><br/>The post <b>%s.html</b> not found in drafts.<br/><br/><br/><br/></center>" % (post_name)
                
        return (post_title, post)
        
    def guess_type(self, path):
        if path.endswith('/v'):
            return 'text/html'
        else: 
            SimpleHTTPRequestHandler.guess_type(self, path);

if __name__ == '__main__':
    httpd = HTTPServer(('', int(sys.argv[1])), OfflineBlogRequestHandler)
    try:
        print("Serving HTTP on", httpd.server_address , "port", httpd.server_port, "...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        sys.exit()
        
