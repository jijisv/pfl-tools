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
                		String postTitle = postName;
                		String postFile = "drafts/" + postName + ".html";
                		String post = "";
                		if (getVertx().fileSystem().existsSync(postFile)) {
	                		post = getVertx().fileSystem().readFileSync(postFile).toString();
	                		if (post.indexOf("<title>") == 0) {
	                			int endIndx = post.indexOf("</title>");
	                			postTitle = post.substring(7, endIndx);
	                		}
                		} else {
                			post = "<p style=\"text-align: center;margin: 3em;\">The post <b>" + postFile + "</b> not found in drafts.</p>";
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