"""
Exercise 51: Getting Input from a Browser

While it's exciting to see the browser display "Hello Wrold", it's
even more exciting to let the user submit text to your application
from a form. In this exercise we'll improve our starter web
application by using forms and storing information about users into
their "sessions".


How the Web Works

Time for some boring stuff. You need to understand a bit more about
how the web works before you can make a form. This description isn't
complete, but it's accurate and will help you figure out what might be
going wrong with your application. Also, creating forms will be easier
if you know what they do.

I'll start with a simple diagram that shows you the different parts of
a web request and how the information flows:

   Your Browser                        Web App's
   http://test.com/                    index.GET
       |(A)                              (D)|
    Network   <--(B)--Internet--(C)-->    My
   Interface                            Server

I've labeled the lines with letters so I can walk you through a regular
request process:
    1. You type in the url http://test.com// into your browser and it
    sends the request on line(A) to your computer's network interface.
    2. Your request goes out over the internet on the line(B) and then
    to the remote computer on line(C) where my server accepts the
    request.
    3. Once my computer accepts it, my web application gets it on
    line(D), and my Python code runs the index.GET handler.
    4. The response comes out of my Python server when I return it, and
    it goes back to your browser over line(D) again.
    5. The server running this site takes the response off line(D) then
    sends it back over the internet on line(C).
    6. The response from the server then comes off the internet on
    line(B), and your computer's network interface hands it to your
    browser on line(A).
    7. Finally, your browser then displays the response.

In this description there are a few terms you should know so that you
have a common vocabulary to work with when talking about your web
application:
    Browser
        The software that you're probably using every day. Most people
        don't know that a browser really does. They just call browsers
        "the internet". Its job is to take address (like
        http://test.com//) you type into the URL bar, then use that
        information to make requests to the server at that address.
    Address
        This is normally a URL (Uniform Resource Locator) like
        http://test.com// and indicates where a browser should go. The
        first part http indicates the protocol you want to use, in
        this case "Hyper-Text Transport Protocol". You can also try
        ftp://ibiblio.org/ to see how "File Transport Protocol" works.
        The http://test.com// part is the "hostname", or a human
        readable address you can remember and which maps to a number
        called an IP address, similar to a telephone number for a
        computer on the Internet. Finally, URLs can have a trailing
        path like the /book/ part of http://test.com//book/ , which
        indicates a file or some resource on the server to retrieve
        with a request. There are many other parts, but those are the
        main ones.
    Connection
        Once a browser knows what protocol you want to use (http), what
        server you want to talk to (http://test.com//), and what
        resource on that server to get, it must make a connection. The
        browser simply asks your operating system (OS) to open a "port"
        to the computer, usually port 80. When it works the OS hands
        back to your program something that works like a file, but is
        actually sending and receiving bytes over the network wires
        between your computer and the other computer at
        http://test.com//. This is also the same thing that happens
        with http://localhost:8080/ but in this case you're telling
        the browser to connect to your own computer (localhost) and
        use port 8080 rather than the default of 80. You could also do
        http://test.com:80/ and get the same result, except you're
        explicitly saying to use port 80 instead of letting it be that
        by default.
    Request
        Your browser is connected using the address you gave. Now it
        needs to ask for the resource it wants (or you want) on the
        remotes server. If you gave /book/ at the end of the URL, then
        you want the file (resource) at /book/, and most servers will
        use the real life /book/index.html but pretend it doesn't
        exist. What the browser does to get this resource is send a
        request to the server. I won't get into exactly how it does
        this, but just understand that it has to send something to
        query the server for the request. The interesting thing is
        that these "resources" don't have to be files. For instance,
        when the browser in your application asks for something, the
        server is returning something your Python code generated.
    Server
        The server is the computer at the end of a browser's connection
        that knows how to answer your browser's requests for files/
        resources. Most web servers


"""