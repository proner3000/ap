const links = document.querySelectorAll("#passive");
const link = document.querySelectorAll("#progess");
function linka(links){
        links.forEach(function(link) {
        link.addEventListener("click", function(event) {
            event.preventDefault();
        });
        });
} 
if (links.length > 0) {linka(links);}
if(link.length>0){
linka(link);}
const disclamer = document.getElementById("disclamer");
if(disclamer){disclamer.innerHTML = "Green for active, Yellow for in progress and red means unactive link/page";}
function openNav() {
    document.getElementById("mySidenav").style.width = "160px";
    document.getElementById("main").style.marginLeft = "250px";
    document.getElementById("z").style.display = "none";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
    }
  
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.getElementById("z").style.display = "inline";
    document.body.style.backgroundColor = "white";
    }
 const a = '/header.html'
    function replaceheaderContent() {
        fetch(a)
            .then(response => response.text())
            .then(data => {
                document.getElementById('header').innerHTML = data;
            })
            .catch(error => console.error(error));
    }
    replaceheaderContent();
const b = '/footer.html'
    function replaceContent() {
        fetch(b)
            .then(response => response.text())
            .then(data => {
                document.getElementById('footer').innerHTML = data;
            })
            .catch(error => console.error(error));
    }
    replaceContent();
