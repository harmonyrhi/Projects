const PORT = 8000
const express = require('express')
const axios = require('axios')
const cheerio = require('cheerio')
const res = require('express/lib/response')

// const Twit = require('twit')

// const apikey = 'LwHgI5h0rhHYXzU6r12uERoBa'
// const apiSecretKey = 'dmobx5daJZopDIu2FB6MwMubrlMTacDYjt5m3gKQqwRbOupLnO'
// const accessToken = '798232109546672128-tNLiY4bM2mXu4NQnp6A2LDfJI8UIyLm'
// const accessTokenSecret = 'rC1SQVczOBUQSAzt45GMimyK3auA8fzgt8crUAbez4F3n'

// var T = new Twit({
//     consumer_key:         apikey,
//     consumer_secret:      apiSecretKey,
//     access_token:         accessToken,
//     access_token_secret:  accessTokenSecret,
// });

const app = express()

const articles=[]
const tweets=[]

app.get('/', (req, res)=>{
    res.json('Welcome to our basketball statistics API')
})

app.get('/stats', (req, res)=>{
    axios.get('https://www.theguardian.com/sport/nba')
        .then((response)=>{
            const html = response.data
            const $ = cheerio.load(html)

            $('a:contains("Warriors")', html).each(function(){
                const title = $(this).text()
                const url = $(this).attr('href')
                articles.push({
                    title,
                    url
                })
            })
            res.json(articles)
        }).catch((err)=> console.log(err))
})

// var options = {
//   method: 'GET',
//   url: 'https://twitter32.p.rapidapi.com/getSearch',
//   params: {hashtag: 'hawks', start_date: '2018-01-01', end_date: '2020-10-10', lang: 'en'},
//   headers: {
//     'x-rapidapi-host': 'twitter32.p.rapidapi.com',
//     'x-rapidapi-key': '35a48f3ed1msh83eb079c5e5dbb3p188bd2jsn107870724fa5'
//   }
// };

// axios.request(options).then(function (response) {
// 	res.json(response.data);
// }).catch(function (error) {
// 	console.error(error);
// });

app.listen(PORT, ()=> console.log(`server running on PORT ${PORT}`))