// let btn = document.querySelector('button');
// let box = document.getElementById('cg');
// box.style.width="500px";
// box.style.height = "200px";
// box.style.border = "2px solid black";
// box.style.padding = "20px";
// box.style.marginLeft="200px";
// box.style.marginTop = "50px";

// btn.style.padding = "10px";
// btn.style.marginLeft="410px";
// btn.style.marginTop = "20px";


// changeColor = ()=>{
//     r = Math.floor(Math.random()*256);
//     g = Math.floor(Math.random()*256);
//     b = Math.floor(Math.random()*256);

//     r = String(r);
//     g = String(g);
//     b = String(b);

//     str = (`rgb(${r},${g},${b})`);
//     console.log(str);
//     box.innerText = `This is Your new Color ${str}.`
//     // console.log(typeof(str));

//     box.style.backgroundColor = str;

// }

// btn.addEventListener("click",changeColor);

// box.addEventListener("mouseenter",changeColor);

// function changeName(){
//     this.innerText = "montu sona";
// }

// function changeNameOriginal(){
//     this.innerText = "Click";
// }

// btn.addEventListener("mouseenter",changeName);
// btn.addEventListener("click",changeNameOriginal);

// let space = document.querySelector('input');
// space.style.padding = "5px";

// function keyPress(event){
//     console.log("key is pressed");
//     console.log(event.code);
// }

// space.addEventListener("keyup",keyPress);

// let form = document.querySelector("form");

// function GetValue(){
//     let input = document.querySelector("input");
//     console.log(input.value);

// }

// // form.addEventListener("submit",function GetValue(event){
// //     event.preventDefault();
// //     let input = document.querySelector("#user");
// //     let pass = document.querySelector("#pass");
// //     alert(`Your username : ${input.value} is set to Password : ${form.elements[1].value}`);

// // });

// form.elements[0].addEventListener("input", function ChangeEvent(){
//     console.log("Vale is change to ",this.value );
// })

// let editor = document.querySelector("textarea");
// let para = document.querySelector("#editor");
// editor.addEventListener("input",function(event){
//     event.preventDefault();
//     para.innerText = this.value;
// })

// window.addEventListener("load",()=>{
//     console.log("Screen is loaded ");
// })

// let buttonColor = document.createElement("button");
// let body = document.querySelector("body");
// body.appendChild(buttonColor);
// buttonColor.innerText = "Click And See!";
// buttonColor.addEventListener("click",()=>{
//     buttonColor.style.backgroundColor = "lightgreen";
//     buttonColor.style.padding="20px";
// })


//<----------------Correct it----->
// let editor = document.querySelector("textarea");
// let para = document.querySelector("#editor");
// editor.addEventListener("in",function(event){
//     event.preventDefault();
//     let charCode =event.key.charCodeAt(0);
//     if((charCode>=65 && charCode <=90)||(charCode >=97 && charCode <=122) ||charCode ==32){
//         this.value = `${this.value}${event.key}`;
        
//     }
//     para.innerText = this.value;
// })

// let div = document.getElementById("test");
// let p = document.querySelector("#intest");

// p.addEventListener("click",function(){
//     console.log("Child was Clicked");
// });

// div.addEventListener("click",function(){
//     console.log("Parent was Clicked");
// });


let input = document.querySelector("input");
let button = document.querySelector("button");

let ul = document.querySelector(".test");
button.addEventListener("click",function(event){
    event.preventDefault();
    let li = document.createElement("li");
    // li.style.listStyleType="decimal";
    li.style.padding="10px";
    li.innerText = input.value;
    ul.appendChild(li);


    let buttonnew = document.createElement("button");
    buttonnew.innerText="Remove";
    buttonnew.classList.add("delete");
    li.appendChild(buttonnew);
    // buttonnew.addEventListener("click", function(){
    //     buttonnew.parentElement.remove();
    //     console.log("Button removed");
    // })

    ul.addEventListener("click",function(event){
        // console.log(event.target);
        if(event.target.tagName==="BUTTON"){
            event.target.parentElement.remove();
        }
            

    })

    // for(btn of btns){
    //     btn.addEventListener("click", function(){
    //         console.log("button clicked delete");
    //         console.dir(btn.parentElement);
    //         btn.parentElement.remove();
            
    //     });
    // console.dir(btns);

    input.value="";
    

})

