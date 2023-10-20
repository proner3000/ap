const day ="M150 0 L75 200 L225 200 Z";
const night = "M150 0 L75 200 L225 4400 Z";

const a = document.getElementById("app");
var toggle = true;
if(a!=null){
a.addEventListener("click",()=>{
   const time = anime.timeline({
      duration : 750,
      easing:"easeOutExpo"
    });
 time.add({
    targets: ".dark",
    d:[
        {value: toggle ? day : night}
    ],
     });
}); 
}