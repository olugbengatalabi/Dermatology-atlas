// const logout = document.getElementById("logout")
const logout = document.getElementsByClassName("logout")
const logoutForm = document.getElementById("logoutform")
const upvoter = document.getElementsByClassName("upvote");
const hamburger = document.getElementById("hamburger");
const dropdown = document.getElementById("dropdown");
const closeBtn = document.getElementById("close");
const emptySpace = document.getElementById("empty-space")
const msgCloseBtn = document.getElementById("close-btn") 
const message = document.getElementById("message")

if (hamburger) {
  hamburger.addEventListener(("click"), () => {
    dropdown.classList.remove("display-sm");
  });
  
  closeBtn.addEventListener(("click"), () => {
    dropdown.classList.add("display-sm");
  
  })
  emptySpace.addEventListener("click", () => {
    dropdown.classList.add("display-sm")
  })
  
}


const logoutc = [...logout]
const upvoterList = [...upvoter]
for (let index = 0; index < logoutc.length; index++) {
  let selected = logoutc[index];
  selected.addEventListener("click", () => {
    logoutForm.submit()
  })
  
}

// for (let index = 0; index < upvoterList.length; index++) {
//   let selected = upvoterList[index] 
//   selected.addEventListener(("click"), () => {
//       selected.innerText === "upvote" ? selected.innerText = "upvoted" : selected.innerText = "upvote";
//   })
// }
// for (let index = 0; index < upvoterList.length; index++) {
//   let selected = upvoterList[index] 
//   selected.addEventListener(("click"), () => {
//     console.log(selected);
//       selected.innerHTML === "<span><i class ='fas fa-thumbs-up'></i></span>" ? selected.innerHTML = "<span><i class='upvoter-background fas fa-thumbs-up'>hhh</i></span>" : selected.innerHTML = "<span><i class='fas fa-thumbs-up'></i></span>";
//   })
// }
// for (let index = 0; index < upvoterList.length; index++) {
//   let selected = upvoterList[index];
//   selected.addEventListener("click", () => {
//     if (selected.innerText === ' upvote') {
//       selected.innerHTML = "<i class ='fas fa-thumbs-up'></i> upvoted";
//       selected.classList.add("upvote-background")
//       console.log(selected.classList);
//     }
//     else {
//       selected.innerHTML = "<i class ='fas fa-thumbs-up'></i> upvote"
//     }
//   })
  
// }
for (let index = 0; index < upvoterList.length; index++) {
  let selected = upvoterList[index];
  selected.addEventListener("click", () => {
    console.log("1");
    if (selected.textContent === '..') {
      console.log("2");
      selected.innerHTML = "<i class ='fas fa-star upvote-background'></i>...";
    }
    else {
      selected.innerHTML = "<i class ='fas fa-star'></i>.."
      console.log("3");
    }
  })
  
}
// close message
const closer = () => {
  message.classList.add("display-lg")
  message.classList.add("display-sm")
};
if (msgCloseBtn) {
  setTimeout(closer,3500)
  msgCloseBtn.addEventListener("click", closer); 
}


// {% if diseases %}
      
//       {% for disease in diseases %}
//         const upvote = document.getElementById("upvote")
//         upvote.addEventListener(("click"), () => {
//           if (upvote.innerText === "upvote") {
//             console.log("anything");
//             upvote.innerText = "upvoted"
//           }
//           else {
//             upvote.innerText = "upvote"
//           }
//       })
//       {% endfor %}
        
//     {% endif %}
// 
// console.log(upvoterList)