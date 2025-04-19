// let h1 = document.getElementById("heading");

// function changeColor(color ,delay , callback){
//     setTimeout(()=>{
//     h1.style.color = color;
//     if(callback){
//         callback();
//     }
//     },2000)
// }

// changeColor("red",1000,()=>{
//     changeColor("orange",1000,()=>{
//         changeColor("yellow",1000,()=>{
//             changeColor("purple",1000)
//         })
//     })
// });



// function saveToDb(data,succes,failure){
//     let internetSpeed = Math.floor(Math.random()*10+1);
//     if(internetSpeed>4){
//         console.log("connection is ok");
//         succes(data);
//     }else{
//         console.log("low Connection");
//         failure(data);
//     }
// }

// saveToDb("apnaCollege",(data)=>{
//     console.log("Succes Data Saved",data);
//     saveToDb("Sharadha khapra",(data)=>{
//         console.log(data,"Data2 is saved ");
//         saveToDb("shobhandeb Adak Student",(data)=>{
//             console.log(data,"Data3 is saved");
//         },()=>{
//             console.log(data,"Data 3 is not saved ");
//         })
//     },()=>{
//         console.log(data,"Data2 is not saved");
//     })
// },(data)=>{
//     console.log("Failure Data not Saved",data);
// });


// function saveToDb(data){
//     return new Promise((success,failure)=>{
//         let internetSpeed = Math.floor(Math.random()*10+1);
//         if(internetSpeed>4){
//             success("success : data was saved ");
//         }
//         else{
//             failure("failure : weak connection");
//         }
//     })
// }

// let request = saveToDb("apnaCollege");
// //request is a promise object

// request.then(()=>{
//     console.log("Promise was resolved");
//     console.log(request);
// })

// .catch(()=>{
//     console.log(request);
//     console.log("Promise was rejected");
// })

// //to directly attach it ot saveToDb function
// saveToDb("apnaCollege")
// .then(()=>{
//     console.log("Promise was resolved");
//     console.log(request);
// })

// .catch(()=>{
//     console.log(request);
//     console.log("Promise was rejected");
// })


// let pizzaOrder =new Promise((resolve,reject)=>{
//     let pizzaReady = false;
//     if(pizzaReady){
//         reject( "Sorry,we ran out of ingredients.");
        
//     }
//     else{
//         resolve("Pizza is Ready!");
//     }
// });

// pizzaOrder
// .then((bal)=>console.log(bal))//if pizza is ready , this runs 
// .catch((error)=> console.log("l;l;"));


///suppose

// function saveToDb(data){
//     return new Promise((resolve,reject)=>{
//         let internetSpeed = Math.floor(Math.random*10+1);
//         if(internetSpeed>4){
//             resolve("Data1 Saved ");
            
//         }
//         else{
//             reject()
//         }
//     })
// }





// let h1 = document.querySelector("body");

// function changeColor(color, delay,callback){
    
//     setTimeout(()=>{
//     h1.style.backgroundColor = color;
//     if(callback){
//         callback();
//     }},delay);
// }

// changeColor("red",2000,()=>{
//     changeColor("green",2000,()=>{
//         changeColor("yellow",2000,()=>{
//             changeColor("black",2000,()=>{
//                 changeColor("purple",2000);
//             })
//         })
//     })
// })









//call back hell : 

// //red - blue - green - yellow - pink - purple 
//set timeout call back
// setTimeout(()=>{
//     changeColor("red",1000);

//     setTimeout(()=>{
//         changeColor("blue",1000);

//         setTimeout(()=>{
//             changeColor("green",1000);

//             setTimeout(()=>{
//                 changeColor("yellow",1000);
//                 setTimeout(()=>{
//                     changeColor("pink",1000);
//                     setTimeout(()=>{
//                         changeColor("purple",1000);
//                     },1000);
//                 },1000);
//             },1000);
//         },1000);
//     },1000);
// },1000);


// function saveToDb(data){
//     return new Promise((resolve, reject)=>{
//         let internetSpeed = Math.floor(Math.random()*10 +1 );
//         if(internetSpeed > 4){
//             resolve(data,);
//         }
//         else{
//             reject(data);
//         }
//     })
// }


// saveToDb("Shobhandeb Adak")
//     .then((value)=>{
//         console.log("Data1 is saved ", value);
//         saveToDb("Debabrata Adak")
//         .then((value)=>{
//             console.log("Data2 is saved",value);
//             saveToDb("Monika Adak")
//             .then((value)=>{
//                 console.log("Data3 is saved",value);
//                 saveToDb("Debasmita Adak")
//                 .then((value)=>{
// //                     console.log("Data 4 is saved ",value);
// //                 })
// //             })
// //         })

// //     })
// //     .catch((value)=>{
// //         console.log("Data not saved " , value);
        
// //     });


// //promise chaining
// saveToDb("Shobhandeb Adak")
//     .then((value)=>{
//         console.log("Data1 is saved ", value);
//         return saveToDb("Debabrata Adak");})
//         .then((value)=>{
//             console.log("Data2 is saved",value);
//             return saveToDb("Monika Adak");})
//             .then((value)=>{
//                 console.log("Data3 is saved",value);
//                 return saveToDb("Debasmita Adak");})
//                 .then((value)=>{
//                     console.log("Data 4 is saved ",value);})
                
            
    

    
//     .catch((value)=>{
//         console.log("Data not saved " , value);
        
//     });




// let h1 = document.querySelector("body");

// function ChangeColor(color,delay){
//     return new Promise((resolve,reject)=>{
//         setTimeout(()=>{
//             h1.style.backgroundColor = color;
//             resolve(color);
//         },delay);
//     });
// };

// ChangeColor("red",1000)
// .then((value)=>{
//     console.log("Color change to ",value);
//     return ChangeColor("green",1000);
// })
// .then((value)=>{
//     console.log("Color change to ",value);
//     return ChangeColor("yellow",1000);
// })
// .then((value)=>{
//     console.log("Color change to ",value);
//     return ChangeColor("blue",1000);
// })
// .then((value)=>{
//     console.log("Color change to ",value);
//     return ChangeColor("purple",1000);
// })
// .then((value)=>{
//     console.log("Color change to ",value);
//     return ChangeColor("white",1000);
// })
// .then((value)=>{
//     console.log("Color change to ",value);
//     return ChangeColor("black",1000);
// })
// .then((value)=>{
//     console.log("Color change to ",value);
//     return ChangeColor("red",1000);
// })
// .then((value)=>{
//     console.log("Color change to ",value);
// });


// async function divide(a, b) {
//     if (b === 0) {
//         throw "Cannot divide by zero!";  // Manually throwing an error
//     }
//     return a / b;
// }

// console.log(divide(10, 2));  
// console.log(divide(5, 0));   


// function getNum(){
//      return new Promise((resolve , reject) =>{
//         setTimeout(()=>{
//             let num = Math.floor(Math.random()*10)+1;
//             console.log(num);
//             resolve();
//         },2000);
//     });
// // }
 
// // async function demo() {
// //     await getNum();
// //     await getNum();
// // }

// // demo();

// let h1 = document.querySelector("body");

// function changeColor(color,delay){
//     return new Promise((resolve,reject)=>{
//         setTimeout(()=>{
//             h1.style.backgroundColor = color;
//             resolve();
//         },delay);
//     })
// }


// async function color() {
//     try{
//     await changeColor("red",2000);
//     TreeWalketr();
//     await changeColor("green",2000);}
//     catch(erroer){
//         console.log(erroer);
//     }
//     changeColor("blue",2000);
// }

// color();


//api calls  : 

// let h1 = document.querySelector("h1");
// let pcat = document.getElementById("cat");


// let body = document.querySelector("body");//selects body 
// let dogImage = document.createElement("img");
// dogImage.style.width = "400px";
// dogImage.style.height = "400px";

// let buttonDog = document.createElement("button");
// body.append(buttonDog);//first button 
// buttonDog.innerText = "Get Dog Images";
// body.append(dogImage);//next images 

// buttonDog.addEventListener("click",async ()=>{
//     let random = await GetDogImage();
//     dogImage.src = random;
// })


// async function GetDogImage() {
//     try{
//         let x = await axios.get(url2);
//         return x.data.message;
//     }
//     catch(e){
//         return "No images of dog found "
//     }
// }




// //function for showing dog image
// let url2 = "https://dog.ceo/api/breeds/image/random";






// let url = "https://catfact.ninja/fact";
// let button = document.querySelector("button");//button for cat 

// button.addEventListener("click",async()=>{
//     let data = await catFacts();
//     pcat.innerText = data;
// })

// async function catFacts(){
//     try{
//         let a = await axios.get(url);
//         // console.log(a);
//         return a.data.fact;
//     }
//     catch(e){
//         return "No facts found ! ";
//     }
// };



// const url = "https://icanhazdadjoke.com";

// async function getJokes() {
//     const config = {headers:{Accept:"application/json"}};
//     let res = await axios.get(url,config);
//     console.log(res.data);
// }


let h1 = document.querySelector("h1");
let search = document.querySelector("button");
let collegespara = document.getElementById("college");

let url = "http://universities.hipolabs.com/search?name=";

let input = document.querySelector("input");


search.addEventListener("click",async()=>{
  let x = [];
     x  = x.concat(await getCollegeName());
  let k =" ";
  for(i=x.length;i>0;i--){
    k=`College ${i} is ${x[i]}
    ` +k;
  }
  console.log(k);
console.log(x);
    collegespara.innerText = k;
});


async function getCollegeName(){
    let arr = [];
    try{
        let dataR = await axios.get(url+input.value);
        console.log(dataR.data);
        for(i=0 ;i<dataR.data.length;i++){
            arr.push(dataR.data[i].name);
        }
        return arr;

    }
    catch(e){
        return "No Data found";
    }
}