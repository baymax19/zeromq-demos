var express = require("express")
var app = express()

let Parser = require("rss-parser")
let parser = new Parser()

var searchURL = "https://github.com/baymax19/zeromq-demos/commits/master.atom"
var sentinelFeed = "https://medium.com/feed/sentinel"

app.listen(9000, ()=> console.log("App listening on 9000"))

app.get("/feed",function(req, res){
    (async () => {
        let feed = await parser.parseURL(searchURL)
        console.log(feed.items[0])
    })()

})
