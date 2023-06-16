var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');

// Set canvas size to match the window
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Set up raindrop properties
var drops = [];
for (var i = 0; i < 500; i++) {
	drops.push({
		x: Math.random() * canvas.width,
		y: Math.random() * canvas.height,
		width: Math.random() * 2 + 1,
		height: Math.random() * 50 + 10,
		speed: Math.random() * 3 + 1,
		color1: 'hsl(' + (Math.random() * 360) + ', 100%, 80%)',
		color2: 'hsl(' + (Math.random() * 360) + ', 100%, 70%)'
	});
}

// Set up animation loop
function draw() {
	// Clear the canvas
	ctx.clearRect(0, 0, canvas.width, canvas.height);

	// Draw the raindrops
	for (var i = 0; i < drops.length; i++) {
		// Move the raindrop down the screen
		drops[i].y += drops[i].speed;

		// If the raindrop goes off the screen, reset it at the top
		if (drops[i].y > canvas.height) {
			drops[i].y = 0;
			drops[i].x = Math.random() * canvas.width;
		}

		// Create gradient for the raindrop
		var gradient = ctx.createLinearGradient(drops[i].x, drops[i].y - drops[i].height / 2, drops[i].x, drops[i].y + drops[i].height / 2);
		gradient.addColorStop(0, 'rgba(0, 0, 255, 1)'); // blue
		gradient.addColorStop(1, 'rgba(255, 255, 255, 1)');

		// Draw the raindrop
		ctx.beginPath();
		ctx.moveTo(drops[i].x, drops[i].y);
		ctx.bezierCurveTo(drops[i].x + drops[i].width / 2, drops[i].y + drops[i].height / 4, drops[i].x, drops[i].y + drops[i].height, drops[i].x - drops[i].width / 2, drops[i].y + drops[i].height / 4);
		ctx.fillStyle = gradient;
		ctx.fill();
	}

	// Request another animation frame
	requestAnimationFrame(draw);
}

// Start the animation loop
draw();
