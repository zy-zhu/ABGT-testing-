




function closeWindow(){

   var modal=document.getElementById('myModal');
   var span=document.getElementById('close');
   var instruction=document.getElementById('instruction');


    modal.style.display='none';
    instruction.style.display='inline';

    // span.onclick=function(){
    //     modal.style.display='none';
    // }

    // window.onclick=function(event){
    //     if(event.target==modal)modal.style.display='none';
    // }
 
}

function openIntro(){

    var introbutton=document.getElementById('intro');
    var introvideo=document.getElementById('video-intro');
    var modal=document.getElementById('myModal');
    modal.style.display='none';
    introvideo.style.display='inline';  

}

function closeVideo(){
    var skip=document.getElementById('skip');
    var introvideo=document.getElementById('video-intro');
    var instruction=document.getElementById('instruction');

    introvideo.style.display='none';  
    instruction.style.display='inline';
}



function openInstru(){
    var instruction=document.getElementById('instruction');
    var introvideo=document.getElementById('video-intro');

    introvideo.style.display='inline';  
    instruction.style.display='none';

    
}