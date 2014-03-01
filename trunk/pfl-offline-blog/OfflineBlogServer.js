var vertx = require('vertx');
var console = require('vertx/console');

var port = 80;

vertx.http.createHttpServer().requestHandler(function(req) {
	console.log('Request: ' + req.path())

	if (req.path() === '/v') {
		var template = vertx.fileSystem.readFileSync('index.htm').toString(), 
			post_name = req.params().get("p"),
			post_title = post_name,
			post_file = 'drafts/' + post_name + '.html',
			post = "";
		if (vertx.fileSystem.existsSync(post_file)) {
			post = vertx.fileSystem.readFileSync(post_file).toString();
			if (post.indexOf('<title>') === 0) {
				var endIndx = post.indexOf('</title>');
				post_title = post.slice(7, endIndx);
			}
		} else {
			post = '<p style="text-align: center; margin: 3em;">The post <b>' + post_file + '</b> not found in drafts.</p>';
		}
		req.response.end(template.replace('$BLOG_ENTRY_BODY$', post)
								 .replace('$BLOG_ENTRY_TITLE$', post_title));
	} else {
		req.response.sendFile('.' + req.path());
	}
}).listen(port);
console.log('Server listening at ' + port);