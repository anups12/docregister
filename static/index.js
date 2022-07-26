console.log("working");


const summary = document.querySelectorAll(".summary")
for(let x of summary){
    if(x.textContent. match(/(\w+)/g). length>15){
        p=x.textContent.split(' ').slice(0, 15).join(' ') + "..."
        x.textContent=p
    }
   
}

console.log("THisis also working");