var test = document.querySelectorAll(".description");

  
  
  for(i = 0; i < test.length; i++) {
   test[i].addEventListener('mouseenter', function(event) {
        event.target.innerHTML="this is the description of the winown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lore";
        event.target.style.color="#CFB86B";
   });
}

for(i = 0; i < test.length; i++) {
   test[i].addEventListener('mouseleave', function(event) {
       event.target.innerHTML="placeholder";
       event.target.style.color="black";
   });
}
  
  