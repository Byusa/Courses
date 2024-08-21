const express = require('express');
const app = express(); // create express app

app.use(express.static("public")) // Static files
app.use(express.urlencoded({ extended: true })) // parse application/x-www-form-urlencoded
app.use(express.json()) // parse application/json

app.set('view engine', 'ejs'); // set the view engine to ejs
// app.use(logger) // middleware [top to buttom](everything that comes after the middleware it uses it)


app.get('/', logger, (req, res) => {
    // res.send('Hello World'); // send text response
    res.sendStatus(200).send('Hi') // send status code and text response
    // res.sendStatus(200).json({ message: 'error' }) // send status code and json response
    // res.status(500).json({ message: 'error' }) // send status code and json response
    // res.download('server.js') // download file
    console.log('Hello World');
    // res.render('index', { name: 'John' }); // render a view
    }
);

const userRouter = require('./routes/users');
// const postRouter = require('./routes/posts');

app.use('/users', userRouter);
// app.use("/posts", postRouter);

function logger(req, res, next) {
    console.log(req.originalUrl)
    next()
}

app.listen(3001) // server listens on port 3000