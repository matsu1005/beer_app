var app = new Vue ({
    delimiters: ['[[', ']]'],
    el: "#app",
    data: {
        beers: [],
        review: [],
        pickup_beer: [],
        tmp_beer_list: [],
        noneBeer: false,
        },
        mounted: function() {
            axios.get('/get')
                .then(function (response) {
                for(var d in response.data.beers) {
                    var item = response.data.beers[d];
                    app.beers.push(item);
                }
                })
                .catch(function (error) {
                console.log(error);
                })
                .then(function () {
                });
        },
        computed: {
            pickupBeer: function() {
                for (var i = 0; i < 3; i++) {
                    if (this.tmp_beer_list.length != 0) {
                    k = Math.floor(Math.random() * this.tmp_beer_list.length)
                    this.pickup_beer.push(this.tmp_beer_list[k])
                    this.tmp_beer_list.splice(k, 1)
                }}
                return _.orderBy(this.pickup_beer, 'beer_name', 'asc')
            }
        },
        methods : {
            kireRecommend: function() { 
                this.pickup_beer = []
                this.tmp_beer_list = []
                this.noneBeer = false
                for(var d in this.beers) {
                if (this.beers[d].kire_avg > 4) {
                    this.tmp_beer_list.push(this.beers[d])
                }}
                if (this.tmp_beer_list.length === 0) {
                    this.noneBeer = true
                }
            },
            sannmiRecommend: function() {
                this.pickup_beer = []
                this.tmp_beer_list = []
                this.noneBeer = false
                for(var d in this.beers) {
                if (this.beers[d].sannmi_avg > 4) {
                    this.tmp_beer_list.push(this.beers[d])
                }}
                if (this.tmp_beer_list.length === 0) {
                    this.noneBeer = true
                }
            },
            nigamiRecommend: function() {
                this.pickup_beer = []
                this.tmp_beer_list = []
                this.noneBeer = false
                for(var d in this.beers) {
                if (this.beers[d].nigami_avg > 4) {
                    this.tmp_beer_list.push(this.beers[d])
                }}
                if (this.tmp_beer_list.length === 0) {
                    this.noneBeer = true
                }
            },
            amamiRecommend: function() {
                this.pickup_beer = []
                this.tmp_beer_list = []
                this.noneBeer = false
                for(var d in this.beers) {
                if (this.beers[d].amami_avg >= 4) {
                    this.tmp_beer_list.push(this.beers[d])
                }}
            },
            kokuRecommend: function() {
                this.pickup_beer = []
                this.tmp_beer_list = []
                this.noneBeer = false
                for(var d in this.beers) {
                if (this.beers[d].koku_avg > 4) {
                    this.tmp_beer_list.push(this.beers[d])
                }}
                if (this.tmp_beer_list.length === 0) {
                    this.noneBeer = true
                }
            }
            },
            filters: {
                roundScore: function(value) {
                    value = Math.round(value * 10) / 10
                    return parseFloat(value).toFixed(1)
                }
            }
})