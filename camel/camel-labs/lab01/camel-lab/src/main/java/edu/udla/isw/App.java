package edu.udla.isw;

import java.nio.file.Paths;

import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.main.Main;

public class App extends RouteBuilder {

    public static void main(String[] args) throws Exception {
        Main main = new Main();
        main.configure().addRoutesBuilder(new App());
        main.run(args);
    }

    @Override
    public void configure() {
        String baseDir = Paths.get("").toAbsolutePath().getParent().getParent().toString(); // Two folders up
        from("file:" + baseDir + "/lab01/camel-lab/input?noop=true")
                .log("Procesando archivo: ${file:name}")
                .to("file:" + baseDir + "/lab01/camel-lab/output")
                .log("procesado.");

    }
}
