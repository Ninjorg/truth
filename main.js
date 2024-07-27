const http = require('https');

const options = {
	method: 'GET',
	hostname: 'political-bias-database.p.rapidapi.com',
	port: null,
	path: '/MBFCdata',
	headers: {
		'x-rapidapi-key': 'your-key',
		'x-rapidapi-host': 'political-bias-database.p.rapidapi.com'
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
