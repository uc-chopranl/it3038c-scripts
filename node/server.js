var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res){
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
	var uptime = os.uptime();

	var days = Math.floor(uptime / 86400);
	uptime -= days * 86400;

	var hours = Math.floor(uptime / 3600);
	uptime -= hours * 3600;

	var minutes = Math.floor(uptime / 60);
	var seconds = Math.floor(uptime % 60);

	var memoryFree = (os.freemem() / (1024 * 1024)).toFixed(2);
	var memoryTotal = (os.totalmem() / (1024 * 1024)).toFixed(2);
	var numCPU = os.cpus().length;
        myHostName=os.hostname();
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${days} Days, ${hours} Hours, ${minutes} Minutes, ${seconds} Seconds</p>
            <p>Total Memory: ${memoryTotal} MB</p>
            <p>Free Memory: ${memoryFree} MB</p>
            <p>Number of CPUs: ${numCPU}</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");