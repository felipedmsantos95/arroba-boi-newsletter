from utils.email_ox.body import body
import http.server
import socketserver

PORT = 5000
Handler = http.server.SimpleHTTPRequestHandler

page = open('./index.html','w')
page.write(body)
page.close()

with socketserver.TCPServer(("", PORT), Handler) as http:
    print("Server running at port", PORT)
    print("You can see a email preview acessing http://localhost:5000/ in your local web browser.")
    http.serve_forever()