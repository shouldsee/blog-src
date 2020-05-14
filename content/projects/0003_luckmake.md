---
title: "github.com/shouldsee/luck"
date: 2020-05-13T23:02:36-04:00
draft: false
---
  - LUCKmake: the LUcky Compiling Kit for pdb-debuggable builds.
  - http://github.com/shouldsee/luck
  - Below is the fetched README.md for this project.

  <!--more-->

  <div id="md-content">
  	Loading
  </div>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script>
  	var oReq = new XMLHttpRequest();
  	var url = "https://raw.githubusercontent.com/shouldsee/luck/master/README.md"
  	const div = document.getElementById('md-content');
  	// div.innerHTML = `Loading <a href="${url}">${url}</a>`
  	// div.innerHTML = `Loading <a href="${url}">${url}</a>`
	oReq.addEventListener("load", function(event){
        div.innerHTML = marked(oReq.responseText);
	});
	oReq.addEventListener("error", function(event){
		div.innerHTML= `Error ${oReq.responseText}`
	});
	oReq.open("GET", url);
	oReq.send();
  </script>

