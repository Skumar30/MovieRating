var http = require('http');
var fs = require('fs');

//create a server object
http.createServer(function (req, res) {
  fs.readFile('homepage.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    res.end();
  });

// The port to listen to
}).listen(8080);
