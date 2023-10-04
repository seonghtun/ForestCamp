const express = require('express');
// const bodyParser = require('body-parser');
const axios = require('axios');

const router = express.Router()

// request 1, query 0
router.get('/camp/total', (req, res) => {
    axios
        .get('http://54.180.186.96:3000/camp/collection', {
        })
        .then(response => {
            console.log(`statusCode : ${response.status}`)
            // console.log(typeof (response.data.count))
            // console.log(response.data.datas[0].information_use)
            console.log(response.data)
            res.send(response.data)
        })
        .catch(error => {
            console.log(error)
        })

})

router.get('/camp/search/:id', (req, res, next) => {
    console.log(req.query.name)
    // const url = 'http://54.180.186.96:3000/camp/resource/:id'
    // // const url = `http://localhost:3000/camp/resource/${req.query.name}`
    // axios
    //     .get(url, {
    //     })
    //     .then(response => {
    //         console.log(`statusCode : ${response.status}`)
    //         res.send(response.data)
    //     })
    //     .catch(error => {
    //         console.log(error)
    //     })
})

// router.post('/selectQuery', (req, res) => {
//     // const { id , password } = req.query;
//     const id = req.body.id;

//     // const result = connection.query(`select * from user where id = ${id}`);
//     const result = connection.query("select * from user where userid=?", [id]);
//     console.log(result);
//     res.send(result);
// })

// router.post('/insert', (req, res) => {
//     const { id, pw } = req.body;
//     const result = connection.query("insert into user values (?,?)", [id, pw]);
//     console.log(result);
//     res.redirect('/selectQuery?id=' + id);
// })

// router.post('/update', (req, res) => {
//     const { id, pw } = req.body;
//     const result = connection.query("update user set passwd=? where userid=?", [pw, id]);
//     console.log(result);
//     res.redirect('/selectQuery?id=' + id);
// })


module.exports = router;