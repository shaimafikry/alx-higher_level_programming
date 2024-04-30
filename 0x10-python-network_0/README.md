
What a URL is?
	A URL (Uniform Resource Locator) is the address of a unique resource on the internet, such as a webpage, image, or document. It is a key mechanism used by browsers to retrieve published resources
	
What HTTP is?
	HTTP (Hypertext Transfer Protocol) is an application layer protocol used for transmitting hypermedia documents, such as HTML, over the internet.
How to read a URL?
	A URL typically consists of several parts, including the scheme, network location, path, query, and fragment identifier. Here's a breakdown of these components:

	Scheme: The protocol used to access the resource, such as http, https, ftp, etc.
	Network Location (Netloc): The domain name or IP address of the server hosting the resource.
	Path: The hierarchical path to the resource on the server.
	Query: The query string, which starts with a ? and contains parameters that are sent to the server.
	Fragment Identifier: The fragment identifier, which starts with a # and points to a specific part of the resource.
	For example, consider the URL https://www.example.com/docs/books/tutorial/index.html?name=networking#downloading.

	Scheme: https
	Netloc: www.example.com
	Path: /docs/books/tutorial/index.html
	Query: name=networking
	Fragment Identifier: downloading

The scheme for a HTTP URL?
	protocol used  ex http

What a domain name is?
	tha name that holds the ip adresses to look for
	ex:googl.com

What a sub-domain is?
	A subdomain is an additional part of a domain name that is used to organize and separate different sections of a website
	ex : www., doc.gmail.com, info.gmail.com

How to define a port number in a URL?
	To define a port number in a URL, you append it to the hostname or IP address, separated by a colon (:). The port number is an optional part of a URL, used to specify a particular service or application running on a server. If the port number is not specified, the default port for the protocol is used. For example, the default port for HTTP is 80, and for HTTPS, it's 443.

	Here's how you can include a port number in a URL:

	http://www.example.com:8080 - This URL specifies that the HTTP service is running on port 8080 of the server www.example.com.
	https://localhost:8443 - This URL specifies that the HTTPS service is running on port 8443 of the local machine.
	If the URL uses the default port for the protocol, you can omit the port number. For instance, http://www.example.com implies port 80, and https://www.example.com implies port 443.


What a query string is?
	For example, in the URL https://www.example.com/search?query=books&category=fiction, the query string is query=books&category=fiction. Here, query and category are keys, and books and fiction are their corresponding values. This query string could be used to filter a search page to show only books in the fiction category.


What an HTTP request is?

What an HTTP response is?

What HTTP headers are?

What the HTTP message body is?

What an HTTP request method is?

What an HTTP response status code is?

What an HTTP Cookie is?
	represents informations, headers
How to make a request with cURL?
	curl -option ip

What happens when you type google.com in your browser (Application level)?
	sends a request finds the ip in dns,then sends it to the server, come back with a response
