var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

/* GET Hello World page. */
router.get('/helloworld', function(req, res) {
    res.render('helloworld', { title: 'Hello, World!' })
});
module.exports = router;
/* GET Userlist page. */

router.get('/userlist', function(req, res) {
    var db = req.db;
    var collection = db.get('t2');
    collection.find({ },{ limit : 20, sort : { $natural : -1 } },function(e,docs){
        res.render('userlist', {
            "userlist" : docs
        });
    });
});