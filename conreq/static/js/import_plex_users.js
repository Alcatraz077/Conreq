// This somehow needs to pass token with header "X-Plex-Token" into https://plex.tv/pms/friends/all to list all friends of user, 
// then we can list usernames out and import from that. 

const { readFile } = require("fs");
const Token = readFile('data/plex.token');



function importPlexUsers() {
    $.ajax({
        url: '"https://plex.tv/pms/friends/all',
        beforeSend: function(xhr) {
             xhr.setRequestHeader("X-Plex-Token", Token)
        }, success: function(data){
            alert(data);
            //process the JSON data etc
        }
    })
};

document.getElementById('import').onclick = function () {
    importPlexUsers();
};
