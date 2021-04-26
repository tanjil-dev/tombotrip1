var endpoint = ''
var socket = new WebSocket(endpoint)

socket.onmessage = new function(e){
    console.log("message", e)
}
socket.onopen = new function(e){
    console.log("open", e)
}
socket.onerror = new function(e){
    console.log("error", e)
}
socket.onclose = new function(e){
    console.log("close", e)
}