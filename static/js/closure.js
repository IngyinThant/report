$(document).ready(function(){
	for (var i=0; i<3; i++)
		$('body')
			.append($('<button/>',{text:i})
				.click(function(){
					alert(i);
				}));

		}); 