const http = require('https');

const link = 'cnn.com'; // The website to check bias for

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
		const data = JSON.parse(body.toString());

		// Find the bias for the given link
		const siteData = data.find(site => site.url.includes(link));

		if (siteData) {
			console.log(`The political bias of ${link} is: ${siteData.bias}`);
		} else {
			console.log(`No data found for ${link}`);
		}
	});
});

req.end();
