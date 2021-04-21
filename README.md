# landing_project1

# new Way to get Active section
```
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
<style>
.your-active-class {background:blue;}
</style>
</head>
<body>

<section style="height:300px;border:2px solid gold;">This is a Heading</section>
<section style="height:300px;border:2px solid gold;">This is a Heading</section>
<section style="height:300px;border:2px solid gold;">This is a Heading</section>
<section style="height:300px;border:2px solid gold;">This is a Heading</section>

<script>
const sections = document.querySelectorAll("section");
let advanced = [];

const remover = ()=> {
   sections.forEach( (mysec)=> {
      if(mysec.classList.contains("your-active-class")){
         mysec.classList.remove("your-active-class");
      }
   })
}

    const checklast = ()=> {
    if ((window.innerHeight + window.pageYOffset) >= document.body.offsetHeight) {
        return true;
    }else {
        return false;
    }
    };
window.addEventListener("scroll",  ()=> {
   advanced = [];
sections.forEach( (sec, index)=> {
   
   let rect = sec.getBoundingClientRect();
   
   if (rect.top >= -100) {
     advanced.push(sec);
   }
   
})

if (checklast()){
   remover();
   advanced[advanced.length-1].classList.add("your-active-class");
} else {
remover();
advanced[0].classList.add("your-active-class");
console.log(advanced);

}


});
</script>
</body>
</html>
```
