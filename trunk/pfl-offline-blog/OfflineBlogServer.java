import org.vertx.java.core.Handler;
import org.vertx.java.core.http.HttpServerRequest;
import org.vertx.java.platform.Verticle;

/**
 * OfflineBlogServer.
 *  
 * @author Jiji_Sasidharan
 */
public class OfflineBlogServer extends Verticle {

	public void start() {
    	getVertx()
            .createHttpServer()
            .requestHandler(new Handler<HttpServerRequest>(){
                @Override
                public void handle(HttpServerRequest req) {
                    System.out.println("Request: " + req.path());
                	if (req.path().equals("/v")) {
                		String template = getVertx().fileSystem().readFileSync("index.htm").toString();
                		String postName = req.params().get("p");
                		String post = getVertx().fileSystem().readFileSync("drafts/" + postName + ".html").toString();
                		String postTitle = postName;
                		if (post.indexOf("<h1>") == 0) {
                			int endIndx = post.indexOf("</h1>");
                			postTitle = post.substring(4, endIndx);
                			post = post.substring(endIndx + 5, post.length());
                		}
                		req.response().end(template.replace("$BLOG_ENTRY_BODY$", post)
                								   .replace("$BLOG_ENTRY_TITLE$", postTitle));
                	} else {
                		req.response().sendFile('.' + req.path());
                	}
                }
            })
            .listen(80);
    }
}