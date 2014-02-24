var vertx = require('vertx');
var console = require('vertx/console');

var port = 80;

vertx.http.createHttpServer().requestHandler(function(req) {
	console.log('Request: ' + req.path())

	if (req.path() === '/v') {
		var template = vertx.fileSystem.readFileSync('index.htm').toString();
		var post_name = req.params().get("p");
		var post = vertx.fileSystem.readFileSync('drafts/' + post_name + '.html').toString();
		var post_title = post_name;
		if (post.indexOf('<h1>') === 0) {
			var endIndx = post.indexOf('</h1>');
			post_title = post.slice(4, endIndx);
			post = post.slice(endIndx + 5, post.length)
		}
		req.response.end(template.replace('$BLOG_ENTRY_BODY$', post)
								 .replace('$BLOG_ENTRY_TITLE$', post_title));
	} else {
		req.response.sendFile('.' + req.path());
	}
}).listen(port)
console.log('Server listening at ' + port)