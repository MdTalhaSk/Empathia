let waiting = false;



async function sendMessage(){


if(waiting)

return;



const input =
document.getElementById("user-input");



const button =
document.getElementById("send-button");



let message =
input.value.trim();



if(message==="")

return;



addMessage(message,"user-message");



input.value="";



waiting=true;

button.disabled=true;



let loading =
addMessage(
"Empathia is thinking...",
"bot-message typing"
);



try{


let response =
await fetch("/chat",{


method:"POST",


headers:{

"Content-Type":"application/json"

},


body:JSON.stringify({

message:message

})


});




let data =
await response.json();



loading.remove();



addMessage(

data.response,

"bot-message"

);



}



catch(error){


loading.remove();



addMessage(

"Sorry, I am unable to respond right now.",

"bot-message"

);


console.log(error);


}




waiting=false;

button.disabled=false;

input.focus();


}





function addMessage(text,className){


let chatWindow =
document.getElementById("chat-window");



let message =
document.createElement("div");



message.className =
"message "+className;



message.innerText=text;



chatWindow.appendChild(message);



chatWindow.scrollTop =
chatWindow.scrollHeight;



return message;


}




function handleKeyPress(event){


if(event.key==="Enter"){

sendMessage();

}


}