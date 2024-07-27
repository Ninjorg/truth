const http = require('https');

const link = 'foxnews.com'; // The website to check bias for

const options = {
	method: 'GET',
	hostname: 'political-bias-database.p.rapidapi.com',
	port: null,
	path: '/MBFCdata',
	headers: {
		'x-rapidapi-key': 'key',
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
            console.log(`The the reporting quality is of ${link} is: ${siteData.factual}`);
            console.log(`The credibility bias of ${link} is: ${siteData.credibility}`);
		} else {
			console.log(`No data found for ${link}`);
		}
	});
});

req.end();
