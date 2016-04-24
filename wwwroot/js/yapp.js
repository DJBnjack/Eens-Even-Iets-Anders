$(document).ready(function() {
    var getLocalURI = function() {
        var loc = window.location, new_uri;
        if (loc.protocol === "https:") {
            new_uri = "wss:";
        } else {
            new_uri = "ws:";
        }
        new_uri += "//" + loc.host;
        new_uri += "/websocket";
        return new_uri;   
    };
    var ws = new WebSocket(getLocalURI());
    var loggedIn = false;

    ws.onopen = function() {
        console.log("Websocket opened");
    };

    ws.onmessage = function (evt) {
        console.log("Got message: " + evt.data);
        $("#log").append(evt.data + "\n\r");
        if (!loggedIn)
        {
            loggedIn = true;
            $("#login").hide();
            $("#room").show();
        }
    };

    var logIn = function() {
        var inlogNaam = $("#naam").val();
        ws.send(inlogNaam);
    };
    
    $("#inlog").click(function() {
        logIn();
    });
    
    $("#naam").keypress(function(e) {
        if(e.which == 13) logIn();
    });
});