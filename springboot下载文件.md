```java
import java.io.FileInputStream;
import java.io.InputStream;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.core.io.InputStreamResource;
import org.springframework.core.io.Resource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@SpringBootApplication
public class DownloadTestApplication {

	public static void main(String[] args) {
		SpringApplication.run(DownloadTestApplication.class, args);
	}

	@GetMapping("/")
	public ResponseEntity<Resource> downloadFile(String filename) throws Exception {
		InputStream inputStream = new FileInputStream(filename);
		return ResponseEntity.ok()
				.header(HttpHeaders.ACCESS_CONTROL_EXPOSE_HEADERS, HttpHeaders.CONTENT_DISPOSITION)
				.header(HttpHeaders.CONTENT_DISPOSITION,
						"attachment; filename=" + URLEncoder.encode(filename, StandardCharsets.UTF_8))
				.contentType(MediaType.APPLICATION_OCTET_STREAM)
				.contentLength(inputStream.available())
				.body(new InputStreamResource(inputStream));
	}

}
```
