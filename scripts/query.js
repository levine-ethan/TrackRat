const sqlite3 = require("sqlite3").verbose();
let db = new sqlite3.Database("./databases/trackrat.db", (err) => {
	if (err) {
		console.error(err.message);
	}
	console.log("Connected to the trackrat database.");
});

db.serialize(() => {
	db.each(
		`SELECT origin, current_location, destination FROM tracking WHERE tracking_num = 1`,
		(err, row) => {
			if (err) {
				console.error(err.message);
			}
			console.log(row);
		}
	);
});

db.close((err) => {
	if (err) {
		console.error(err.message);
	}
	console.log("Close the database connection.");
});
