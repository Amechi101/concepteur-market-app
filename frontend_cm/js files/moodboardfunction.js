/* Place any script tag within the head of the final html document for deployment,

Like so: <script type="text/javascript" src=""></script>
and source the file URL from the database
*/

/* I will add this script to the head document. Delete the script with the '-->'arrow pointing to it
in this file when ready for deployment, only use this
script for testing --> <script src="http://d3lp1msu2r81bx.cloudfront.net/kjs/js/lib/kinetic-v4.6.0.min.js"></script> */
    

    <script>
	uni_width = 120;
	var stage = new Kinetic.Stage({
		container: 'container',
		width: 450,
		height: 450
	});
    var layer = new Kinetic.Layer();
	stage.add(layer);

	function allowDrop(ev)
	{
		ev.preventDefault();
	}

	function drag(ev)
	{
		ev.dataTransfer.setData("Text", ev.target.id);
	}
	
	function drop(ev)
	{
		ev.preventDefault();
		data = ev.dataTransfer.getData("Text");
		img_received = document.getElementById(data);
		ratio = img_received.height / img_received.width;
		
		var c=document.getElementById("container");
		drop_x=event.pageX-c.offsetLeft;
		drop_y=event.pageY-c.offsetTop;
		
		var imageObj = new Image();
		imageObj.src = img_received.src;
		imageObj.onload = function() {
			var new_image = new Kinetic.Image({
			x: drop_x - uni_width / 2,
			y: drop_y - uni_width * ratio / 2,
			image: imageObj,
			src: img_received.src,
			name: "pic",
			width: uni_width,
			height: uni_width * ratio,
			draggable: true
			});
		new_image.on('mouseover', function() {
            document.body.style.cursor = 'move';
          });
        new_image.on('mouseout', function() {
            document.body.style.cursor = 'default';
          });
        // add the shape to the layer
        layer.add(new_image);
		layer.draw();
      };
	}
	
	document.getElementById('save').addEventListener('click', function() {
            json = stage.toJSON();
			console.log(json);
			var new_stage = Kinetic.Node.create(json, 'displayMoodBoard');
			
			//set image
			var images = new_stage.get('.pic');

			for(i=0;i<images.length;i++)
			{  
			//function to induce scope
			(function() {
				var new_image = images[i];
				var new_imageObj = new Image();
				new_imageObj.onload = function() {
				new_image.setImage(new_imageObj);
				new_image.getLayer().draw();
				};
				new_imageObj.src = new_image.attrs.src;
			})();
}
			
    }, false);
	  
    </script>