
///
/// MapReduce for WordCounts
///


    map_book = function(){
      emit(this.url, this.votes_average);
      this.story.split(' ').forEach(
        function(word) {
            var patt1 = /[a-z]+/i;
            var result = word.match(patt1);
            if(result!==null ){
               if(result instanceof Array){
                    if(erotic.indexOf(result[0]) !== -1){
                        emit(url: this.url, count: 1);
                    }
                }
                if(result instanceof String){
                    if(exclude.indexOf(result[0]) !== -1){
                        emit(url: this.url, count: 1);
                    }
                }
            }
        }
      );
    };

/** We're going to give a few selected words a value
*   Then we inspect the document and emit by the url (URLs are very good IDs, aren't they, Google?)
*   We emit url and count with value 1 if it's in our list of erotic words plus the rounded average votes.
*
*
*/

db.reroticos_top10.drop();

    map_erotic_load = function(){
        erotic = ["labios", "caricias", "erótico", "sensual", "besos", "lamer", "lengua", "polla","coño", "culo", "vagina", "pene", "follar", "orgasmo", "correr", "semen", "tetas", "pechos", ]
        var votes = Math.round(this.votes_average);
        this.content.split(' ').forEach(
            function(word) {
                    if(erotic.indexOf(word) !== -1){
                      votes += 1;
                    }
            }
        );
        emit({url: this.url}, {count: votes});
    };


reduce_erotic_load = function(key, values) {
    // var total = 0;
    // for (var i = 0; i < values.length; i++) {
    //     total += values[i];
    // }
    // return  {total: total, average: values.length };
}


//res = db.marqueze.mapReduce(map_erotic_load, reduce, {out: 'marqueze_top10'});
res = db.reoticos.mapReduce(map_erotic_load, reduce_erotic_load, {out: 'reroticos_top10'});

