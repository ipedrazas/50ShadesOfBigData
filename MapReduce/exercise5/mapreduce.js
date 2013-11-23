///
/// MapReduce for WordCounts
///
map = function(){
  this.story.split(' ').forEach(
    function(word) {
        if(word!==null && word.length>2){
            emit(word, 1);
        }
    }
  );
};

reduce = function reduce(key, values) {
  return values.length; /* == sum(values) */
};

res = db.books.mapReduce(map, reduce, {out: 'book_word_count'});


// mapreduce.js

///
/// MapReduce for WordCounts
///

map_book = function(){
  exclude = ["cuando", "nos", "poco", "mientras", "ten", "sin", "sent", "sobre", "fue",  "ese", "dije",  "casa", "solo",  "dos", "que", "con", "por", "una", "para","como","los","ella","las","sus","pero","mis","estaba","hab","muy","del","dijo","hasta","era","vez","esa", "momento", "despu",  "cada", "dice", "algo", "eso",  "empez", "mucho", "ser", "hac",  "est",  "tan", "nada",  "unos", "tambi", "Ilonka", "hacia", "pod",  "quer", "ver", "entonces",  "otra",  "empec", "pues", "casi", "porque", "iba", "esta", "esto",  "donde", "les", "luego",  "ahora",  "qued", "desde",  "mismo", "nunca", "segu", "dej", "tom",  "comenz",  "dec", "nuevo", "met", "pude",  "uno",  "she",  "estar", "cual", "mejor", "tanto",  "antes", "sab", "voy", "dio", "tarde", "levant", "puerta", "pregunt", "ellos", "este", "fuera", "decir", "tener", "hombre", "llegar", "mir", "soy", "unas",  "estaban",  "bastante", "baj", "dedo", "hace", "par",  "eran", "fui"];
  this.story.split(' ').forEach(
    function(word) {
        var patt1 = /[a-z]+/i;
        var result = word.match(patt1);
        if(result!==null ){
            if(result instanceof Array){
                if(result[0].length >2){
                    // add if not in excluded
                    if(exclude.indexOf(result[0]) == -1){
                        emit(result[0].toLowerCase(), 1);
                    }
                }
            }
            if(result instanceof String){
                if(result[0].length >2){
                    if(exclude.indexOf(result[0]) == -1){
                        emit(result.toLowerCase(), 1);
                    }
                }
            }
        }
    }
  );
};

map_marqueze = function(){
  exclude = ["cuando", "nos", "poco", "mientras", "ten", "sin", "sent", "sobre", "fue",  "ese", "dije",  "casa", "solo",  "dos", "que", "con", "por", "una", "para","como","los","ella","las","sus","pero","mis","estaba","hab","muy","del","dijo","hasta","era","vez","esa", "momento", "despu",  "cada", "dice", "algo", "eso",  "empez", "mucho", "ser", "hac",  "est",  "tan", "nada",  "unos", "tambi", "Ilonka", "hacia", "pod",  "quer", "ver", "entonces",  "otra",  "empec", "pues", "casi", "porque", "iba", "esta", "esto",  "donde", "les", "luego",  "ahora",  "qued", "desde",  "mismo", "nunca", "segu", "dej", "tom",  "comenz",  "dec", "nuevo", "met", "pude",  "uno",  "she",  "estar", "cual", "mejor", "tanto",  "antes", "sab", "voy", "dio", "tarde", "levant", "puerta", "pregunt", "ellos", "este", "fuera", "decir", "tener", "hombre", "llegar", "mir", "soy", "unas",  "estaban",  "bastante", "baj", "dedo", "hace", "par",  "eran", "fui"];
  this.content.split(' ').forEach(
    function(word) {
        var patt1 = /[a-z]+/i;
        var result = word.match(patt1);
        if(result!==null ){
            if(result instanceof Array){
                if(result[0].length >2){
                    // add if not in excluded
                    if(exclude.indexOf(result[0]) == -1){
                        emit(result[0].toLowerCase(), 1);
                    }
                }
            }
            if(result instanceof String){
                if(result[0].length >2){
                    if(exclude.indexOf(result[0]) == -1){
                        emit(result.toLowerCase(), 1);
                    }
                }
            }
        }
    }
  );
};


reduce = function reduce(key, values) {
  return values.length;
};

res = db.marqueze.mapReduce(map_marqueze, reduce, {out: 'marqueze_wc'});
res = db.books.mapReduce(map_book, reduce, {out: 'books_wc'});


{
    "result" : "books_wc",
    "timeMillis" : 8285,
    "counts" : {
        "input" : 3,
        "emit" : 226156,
        "reduce" : 12009,
        "output" : 20982
    },
    "ok" : 1,
}

> db.books_wc.find().sort({value: -1});
