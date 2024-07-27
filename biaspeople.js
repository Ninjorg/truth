const http = require('https');

const options = {
	method: 'GET',
	hostname: 'website-social-scraper-api.p.rapidapi.com',
	port: null,
	path: '/contacts?website=your-link.',
	headers: {
		'x-rapidapi-key': 'your-key',
		'x-rapidapi-host': 'website-social-scraper-api.p.rapidapi.com'
	}
};

const req = http.request(options, function (res) {
	const chunks = [];

	res.on('data', function (chunk) {
		chunks.push(chunk);
	});

	res.on('end', function () {
		const body = Buffer.concat(chunks);
		console.log(body.toString());
	});
});

req.end();
