(function($) {
	$.fn.janeslider = function(options) {
		
		
		// Set default autoplay timeout settings
		
		options = options || {};
		
		if (options.initial == null) options.initial = 5000;
		if (options.autoplay == null) options.autoplay = 5000;
		if (options.pause == null) options.pause = 5000;
		
		
		// Initialise slideshow
		
		$(this).each(function() {
			
			var $this = $(this);
			
			// Set up styles
			
			$(this).css({
				'width' : '99999px',
				'position' : 'relative',
				'padding' : 0
			});
		
			$this.children().css({
				'float' : 'left',
				'list-style' : 'none'
			});
	
			
			// Create the slideshow container and size it to the first image in the list
			
			var $container = $this.wrap('<div class="slider-wrap" style="overflow: hidden;"/>');
			
			$container.css({
				'width' : imageWidth + ' px',
				'height' : imageHeight + ' px'
			});
			
			var $items = $($container.children());
			
			var $firstImage = $($items.find('img').get(0));
			
			var imageWidth = $firstImage.width();
			var imageHeight = $firstImage.height();
			
			// Create the controls for the slideshow
			
			var selectedIndex = 0;
			
			$controlsContainer = $('<div class="controls"></div>');
		

			var buttons = [];
			$items.each(
				function(index) {
					$button = $('<a href="#"></a>').click(function() { setSelectedIndex(index, true); return false; });
					$controlsContainer.append($button);
					buttons.push($button);
				}
			);
		
			
			$container.before($controlsContainer);
			
			// Start slideshow
			
			buttons[0].addClass('selected');
			if (options.initial > 0) var autoplayTimeout = setTimeout(autoplay, options.initial);
			
			
			// Slideshow helper functions
			
			function setSelectedIndex(index, pause) {
				if (selectedIndex == index) return; // Don't do anything if it's already selected
				
				$(buttons[selectedIndex]).removeClass('selected'); // Remove the 'selected' class from the last selected button
				selectedIndex = index; // Update the current selection index
				$(buttons[selectedIndex]).addClass('selected'); // Add the 'selected' class to the new selected button
				
				var newPosition = (-selectedIndex * imageWidth);
				$this.animate({'left' : newPosition}); // Slide the slider to the right position				 
				
				clearTimeout(autoplayTimeout); // Clear the last autoplay timeout (if user interruted autoplay)
				var interval = (pause ? options.pause : options.autoplay); // Get the next autoplay interval length
				if (interval) autoplayTimeout = setTimeout(autoplay, interval);
			}
			
			
			function autoplay() {
				setSelectedIndex(selectedIndex == $items.length - 1 ? 0 : selectedIndex + 1, false); // Move to the next image, or cycle to the beginning it it's on the last image
			}
		});
	
		
	}

})(jQuery);