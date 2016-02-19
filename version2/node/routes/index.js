var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'test01' });
});

/* GET Hello World page. */
router.get('/helloworld', function(req, res) {
    res.render('helloworld', { title: 'Hello, World!' })
});
module.exports = router;
/* GET Userlist page. */

router.get('/dashboard', function(req, res) {
    var db = req.db;
    var allTweets = db.get('allTweets');
	var topTweets = db.get('topTweets');
	var glob;
    allTweets.find({ },{ limit : 20, sort : { $natural : -1 } },function(e,docs){
		topTweets.find({ },{ limit : 20, sort : { $natural : -1 } },function(e,top){
			res.render('dashboard', {"allTweets" : docs,"topTweets":top });
		});
	});

});